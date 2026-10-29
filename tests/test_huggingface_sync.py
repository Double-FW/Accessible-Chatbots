"""Exercise faithful exports and failure paths without publishing to a live dataset."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('publisher', ROOT/'scripts/publish_huggingface.py')
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)

class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base/'repo'
        self.repo.mkdir()
        config = json.loads((ROOT/'huggingface/export-config.json').read_text())
        for name in config['files']:
            result = subprocess.run(['git','-C',str(ROOT),'show','HEAD:'+name], capture_output=True)
            if result.returncode == 0:
                (self.repo/name).write_bytes(result.stdout)
        for name in ['scripts','huggingface']:
            shutil.copytree(ROOT/name,self.repo/name,ignore=shutil.ignore_patterns('__pycache__'))
        self.git('init','-q')
        self.git('config','user.name','Exporter test')
        self.git('config','user.email','test@example.invalid')
        self.commit()
        self.out=self.base/'output'

    def git(self,*args):
        return subprocess.check_output(['git','-C',str(self.repo),*args],stderr=subprocess.DEVNULL)
    def commit(self):
        self.git('add','.')
        self.git('commit','-qm','Test fixture')
    def export(self, ok=True):
        r=subprocess.run(['python3',str(self.repo/'scripts/export_huggingface.py'),'--output',str(self.out)],capture_output=True,text=True)
        if ok: self.assertEqual(r.returncode,0,r.stderr)
        else: self.assertNotEqual(r.returncode,0)
        return r

    def test_exact_documents_dependency_integrity_and_repeatability(self):
        self.export()
        before={p.name:p.read_bytes() for p in self.out.iterdir()}
        docs=[json.loads(x) for x in (self.out/'documents.jsonl').read_text().splitlines()]
        for doc in docs:
            self.assertEqual(doc['text'].encode(), self.git('show','HEAD:'+doc['source_path']))
        chunks=[json.loads(x) for x in (self.out/'knowledge_chunks.jsonl').read_text().splitlines()]
        self.assertEqual(len(chunks),24)
        ids={r['id'] for r in chunks}
        self.assertTrue(all(set(r['dependencies'])<=ids for r in chunks))
        self.export()
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.out.iterdir()})

    def test_invalid_dependency_blocks_export(self):
        p=self.repo/'chatbot_RAG.md'
        p.write_text(p.read_text().replace('Dependencies: none.','Dependencies: C99.',1))
        self.commit();self.export(ok=False)

    def test_deleted_optional_document_is_removed(self):
        (self.repo/'Inclusive_Chatbot_Interface_Reference.md').unlink()
        self.commit();self.export()
        docs=[json.loads(x) for x in (self.out/'documents.jsonl').read_text().splitlines()]
        self.assertFalse(any(r['source_path']=='Inclusive_Chatbot_Interface_Reference.md' for r in docs))

    def test_missing_required_source_and_changed_license_block(self):
        (self.repo/'AGENTS.md').unlink()
        self.commit();self.export(ok=False)
        self.git('reset','--hard','HEAD~1')
        (self.repo/'LICENSE').write_text('Unapproved licence')
        self.commit();self.export(ok=False)

    def test_unapproved_file_is_not_exported(self):
        (self.repo/'private-notes.md').write_text('Not approved for export')
        self.commit();self.export()
        self.assertNotIn('private-notes.md',(self.out/'documents.jsonl').read_text())

    def test_publisher_skips_identical_files_and_preserves_unmanaged_files(self):
        self.export()
        api=Mock();api.repo_info.return_value.sha='destination-head'
        def download(**kw): return str(self.out/kw['filename'])
        with patch.object(publisher,'public_source'):
            result=publisher.publish(self.out,'test-token',api,download)
        self.assertIn('No changes',result)
        api.create_commit.assert_not_called()
        def absent(**kw): raise FileNotFoundError()
        with patch.object(publisher,'public_source'):
            publisher.publish(self.out,'test-token',api,absent)
        args=api.create_commit.call_args.kwargs
        self.assertEqual(args['parent_commit'],'destination-head')
        self.assertEqual({op.path_in_repo for op in args['operations']},set(publisher.MANAGED))
        self.assertNotIn('.gitattributes',{op.path_in_repo for op in args['operations']})
        api.update_repo_settings.assert_not_called()

    def test_private_source_and_missing_token_block(self):
        with patch.object(publisher,'public_source',side_effect=RuntimeError('Private')):
            with self.assertRaises(RuntimeError): publisher.publish(self.out,'test-token')
        with patch.object(publisher,'public_source'):
            with self.assertRaises(RuntimeError): publisher.publish(self.out,None)

if __name__ == '__main__': unittest.main()
