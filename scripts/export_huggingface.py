import hashlib, json, re
from pathlib import Path
from urllib.parse import quote
import yaml

import argparse, subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--output', required=True)
args = parser.parse_args()
OUT = Path(args.output).resolve()
if OUT == ROOT or ROOT in OUT.parents:
    raise RuntimeError('Output must be outside the source repository.')
OUT.mkdir(parents=True, exist_ok=True)
config = json.loads((ROOT/'huggingface/export-config.json').read_text())
if config['source_repository'] != 'Double-FW/Accessible-Chatbots' or config['destination_dataset'] != 'GarethFW/accessible-chatbots':
    raise RuntimeError('Unapproved repository configuration.')
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])
SHA = git('rev-parse','HEAD').decode().strip()
DATE = git('show','-s','--format=%cs','HEAD').decode().strip()
REPO = 'https://github.com/' + config['source_repository']
VERSION = config['dataset_version']
# Read committed blobs, never untracked files or workflow secrets.
meta = {'files': []}
for path in config['files']:
    if '/' in path or path.startswith('.'):
        raise RuntimeError('Only approved root documentation may be exported.')
    result = subprocess.run(['git','-C',str(ROOT),'ls-tree','HEAD','--',path], capture_output=True, check=True)
    if not result.stdout:
        if path in config['required_files']:
            raise RuntimeError('Required source is absent: ' + path)
        continue
    mode, kind, blob = result.stdout.decode().split('\t',1)[0].split()
    if mode != '100644' or kind != 'blob':
        raise RuntimeError('Source must be a regular documentation file: ' + path)
    data = git('cat-file','blob',blob)
    meta['files'].append({'path':path,'blob_sha':blob,'size':len(data)})
def sha256(b): return hashlib.sha256(b).hexdigest()
def write_json(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def write_jsonl(name, rows):
    (OUT/name).write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows), encoding='utf-8')

manifest=[]
texts={}
for f in meta['files']:
    b=git('cat-file','blob',f['blob_sha'])
    blob=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
    assert len(b)==f['size'], (f['path'],len(b),f['size'])
    assert blob==f['blob_sha'], f['path']
    texts[f['path']]=b.decode('utf-8')
    manifest.append({**f,'sha256':sha256(b)})

def record(path, identifier, title, text, kind, start, end, deps=None):
    return dict(id=identifier,title=title,text=text,record_type=kind,
                source_repository=REPO,source_path=path,source_commit=SHA,
                source_url=f'{REPO}/blob/{SHA}/{quote(path)}',
                source_start_line=start,source_end_line=end,
                language='en-GB',license='MIT',author='Double FW',
                dataset_version=VERSION,export_date=DATE,
                text_sha256=sha256(text.encode('utf-8')),
                dependencies=deps or [],always_retrieve_ids=['C00','C01','C02','C20'],
                review_status='extraction_checked_content_not_independently_reviewed')

documents=[]
for path,t in texts.items():
    if path=='LICENSE': continue
    kind=('agent_instructions' if path=='AGENTS.md' else
          'retrieval_knowledge_base' if path=='chatbot_RAG.md' else
          'orientation' if path=='README.md' else
          'prompt_template' if 'prompt' in path.lower() else
          'testing_guidance' if 'Testing' in path else 'reference_guidance')
    documents.append(record(path,'document:'+path,path,t,kind,1,len(t.splitlines())))

t=texts['chatbot_RAG.md']
matches=list(re.finditer(r'(?m)^(?:##\s+)?(C\d{2})\s*\|[^\n]*',t))
assert [m[1] for m in matches]==[f'C{i:02}' for i in range(24)]
chunks=[]
for i,m in enumerate(matches):
    end=matches[i+1].start() if i+1<len(matches) else len(t)
    body=t[m.start():end]
    dep=re.search(r'Dependencies:\s*([^\.\n]*)',body)
    assert dep,m[1]
    deps=re.findall(r'C\d{2}',dep[1])
    chunks.append(record('chatbot_RAG.md',m[1],m[0].strip(),body,'knowledge_chunk',
                         t[:m.start()].count('\n')+1,t[:end].count('\n')+(not t[:end].endswith('\n')),deps))
assert ''.join(c['text'] for c in chunks)==t[matches[0].start():]
ids={c['id'] for c in chunks}
assert all(set(c['dependencies'])<=ids for c in chunks)
prefix=t[:matches[0].start()]
write_jsonl('documents.jsonl',documents)
write_jsonl('knowledge_chunks.jsonl',chunks)
license_bytes=texts['LICENSE'].encode('utf-8')
if sha256(license_bytes)!=config['approved_license_sha256']:
    raise RuntimeError('Licence changed; review the licence and configuration before exporting.')
(OUT/'LICENSE').write_bytes(license_bytes)
write_json('provenance.json',dict(dataset_version=VERSION,export_date=DATE,
    source_repository=REPO,source_commit=SHA,files=manifest,
    rag_preamble=prefix,conversion='Exact UTF-8 document copies and anchored C00-C23 slices; no model rewriting.',
    omitted_from_document_rows=['LICENSE (provided separately)'],
    external_linked_content_fetched=False,weekly_sync_enabled=True))

schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object',
        'required':list(documents[0]),'additionalProperties':False,'properties':{}}
for k,v in documents[0].items():
    schema['properties'][k]={'type':'array','items':{'type':'string'}} if isinstance(v,list) else {'type':'integer' if isinstance(v,int) else 'string'}
write_json('record_schema.json',schema)

card=f'''---
pretty_name: Double FW Accessible Chatbots
language:
- en
license: mit
tags:
- accessibility
- inclusive-design
- chatbots
- retrieval-augmented-generation
- agent-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Accessible Chatbots

Version {VERSION} — source snapshot {DATE}. Automated extraction; content approval is separate.

A source-traceable English-language knowledge corpus for accessible chatbot design, delivery, testing and agent governance. Authored by Double FW; hosted by GarethFW. Source: [Double-FW/Accessible-Chatbots]({REPO}).

## Contents

| Configuration | Records | Purpose |
| --- | ---: | --- |
| `knowledge_chunks` (default) | {len(chunks)} | Complete source sections C00–C23, retaining rules, exceptions, acceptance checks and dependency links |
| `documents` | {len(documents)} | Complete Markdown documents, including agent instructions, prompts, RAG guidance, delivery methodologies, testing brief and repository orientation |

These are alternative views with overlapping content. Do not concatenate them blindly: the full RAG document duplicates the chunk view, and supporting documents cover related material. `train` is a loader split name only; this export is not an independently validated fine-tuning or benchmark dataset. It contains no generated question/answer pairs and no held-out evaluation split.

## Intended use

Use for retrieval, source-grounded design assistance, governance integration and preparation of subsequently reviewed training examples. Applicable deployment instructions and checks must still be implemented by the adopting organisation. Merely training on this corpus does not establish reliable policy adherence, accessibility, usability or legal compliance.

## Retrieval contract

Always include C00, C01, C02 and C20; retrieve task-relevant sections and recursively include their dependencies with cycle detection and deduplication. Do not rely on semantic top-k alone. Preserve full rules, applicability, exceptions and acceptance checks together. C23 describes feature routes. C24 is a separate prompt in `Reusable generation prompt.md`, available in the documents view; it is not a missing knowledge chunk. Consult full testing guidance for detailed procedures.

## Provenance and preparation

The explicitly approved root source files were read from committed Git blobs at commit `{SHA}`. {len(documents)} Markdown files are represented as full document rows; LICENSE is supplied separately. See provenance.json for the exact current file inventory. Every fetched file's byte length and Git blob hash were checked against the repository tree. This export does not fetch external links, private repositories, issues, discussions or commit-author personal data.

The converter copies complete documents without rewriting. It recognises anchored `Cnn |` labels (optionally preceded by `##`) and slices the RAG file into exact source spans. Only metadata such as dependencies, record type, provenance and checksums is added. The RAG preamble is retained in the complete document and provenance file. An AI assistant prepared the conversion and documentation; no new instructional answers were generated. Existing source content may itself be AI-assisted, as indicated in its own metadata. No independent subject-matter review has been performed for this export.

## Record fields

Each row contains `id`, `title`, `text`, `record_type`, repository/path/commit/URL, source start/end lines, language, licence, author, dataset version, export date, text checksum, dependencies, mandatory core IDs and review status. See `record_schema.json` for types and required fields. IDs are namespaced document paths or the existing C00–C23 IDs; source revisions are separate from record identity. Language is recorded as `en-GB` per row and `en` in Hub discovery metadata.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("GarethFW/accessible-chatbots", "knowledge_chunks", split="train")
documents = load_dataset("GarethFW/accessible-chatbots", "documents", split="train")
```

Private repositories require authenticated access. Pin a Hugging Face revision for reproducible use. Loading these rows does not implement dependency-aware retrieval automatically.

## Limitations and known source issues

- The compact RAG's declared heading-based boundary format differs from its plain Cnn labels; this exporter explicitly handles that difference. Flattened source metadata is retained as text rather than misrepresented as valid parsed YAML.
- AGENTS.md flags stale filenames in the README and standalone prompt. These are retained faithfully; actual source paths in this dataset's provenance are authoritative for locating the exported files.
- Source metadata describes agent instructions as proposed for adoption. Export validation does not imply maintainer approval of those instructions or this dataset.
- The guidance distinguishes applicable WCAG baseline requirements, additional delivery rules and research outcomes. Preserve those distinctions; a MUST is not automatically a WCAG requirement.
- The material primarily concerns web chatbots and contains conditional vendor guidance. Do not generalise vendor behaviour or treat guidance as actual product test evidence.
- The corpus is a curated organisational viewpoint, not a representative sample of all disabled people, languages, technologies or accessibility practices. Research with affected people and human accountability remain necessary.
- No model training, runtime enforcement, model performance evaluation or external-link validation was performed.

## Licence and attribution

MIT; copyright (c) 2026 Double FW. The original licence is included unchanged. Preserve its notice when redistributing copies or substantial portions. External references are links, not incorporated external corpora; the dataset licence does not grant rights to third-party linked materials.

## Updates and corrections

GitHub remains the authoring source. The GitHub workflow is configured for Mondays at 07:23 UTC (07:23 UK winter time / 08:23 UK summer time), with a manual Run workflow option. Runs may be delayed by GitHub; public-repository schedules may be disabled after 60 days without repository activity. Review the Actions page for failures or disabled runs. Only explicitly allowlisted files are exported. Deleted optional documents disappear from the next snapshot; missing required files or changed chunk identities stop publishing for review. Dataset visibility is never changed by the publisher. Future releases should track additions, modifications and deletions, preserve source provenance, validate dependencies and publish only approved public sources. Report content corrections through the [source repository]({REPO}/issues). Source deletion can remove material from future exports but cannot recall downloaded copies or automatically remove historical releases or trained model knowledge.

## Changelog

- 0.1.0 (2026-10-29): Initial manual pilot export.\n- 0.2.0 (2026-10-29): Repeatable weekly exporter and publisher. Each snapshot records its exact source revision and file hashes.
'''
(OUT/'README.md').write_text(card,encoding='utf-8')
parsed=yaml.safe_load(card.split('---',2)[1])
assert parsed['configs'][0]['default'] is True
for name in ['documents.jsonl','knowledge_chunks.jsonl']:
    rows=[json.loads(line) for line in (OUT/name).read_text().splitlines()]
    assert len({r['id'] for r in rows})==len(rows)
    for row in rows:
        assert set(row)==set(schema['required'])
        for key,definition in schema['properties'].items():
            value=row[key]
            expected={'array':list,'integer':int,'string':str}[definition['type']]
            assert type(value) is expected,(key,value)
            if expected is list: assert all(type(item) is str for item in value)
        assert sha256(row['text'].encode())==row['text_sha256']
write_json('validation_report.json',dict(status='passed',scope='extraction and packaging only',
    source_files_verified=len(manifest),document_records=len(documents),knowledge_chunk_records=len(chunks),
    expected_chunk_ids_present=True,dependency_targets_valid=True,
    exact_document_byte_preservation=True,exact_rag_chunk_reconstruction=True,
    jsonl_schema_validation=True,dataset_card_yaml_parse=True,
    hugging_face_viewer_verified=False,human_content_review_completed=False,
    source_commit=SHA))
print(json.dumps({'files':[p.name for p in OUT.iterdir()], 'documents':len(documents), 'chunks':len(chunks),'validation':'passed'}))
