"""Publish only the managed export files; never change dataset visibility."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.request

SOURCE = 'Double-FW/Accessible-Chatbots'
DESTINATION = 'GarethFW/accessible-chatbots'
MANAGED = ('README.md', 'LICENSE', 'documents.jsonl', 'knowledge_chunks.jsonl',
           'provenance.json', 'record_schema.json', 'validation_report.json')

def public_source():
    # Deliberately anonymous: private repository content cannot pass this check.
    request = urllib.request.Request('https://api.github.com/repos/' + SOURCE,
                                     headers={'User-Agent': 'Double-FW-dataset-export'})
    with urllib.request.urlopen(request, timeout=30) as response:
        info = json.load(response)
    if info.get('private') is not False or info.get('visibility') != 'public' or info.get('full_name') != SOURCE:
        raise RuntimeError('Source must remain the approved public repository.')

def publish(folder, token, api=None, download=None):
    public_source()
    if not token:
        raise RuntimeError('Add the HF_TOKEN repository secret before publishing.')
    if api is None:
        from huggingface_hub import HfApi, hf_hub_download
        from huggingface_hub.errors import EntryNotFoundError
        api = HfApi(token=token)
        download = hf_hub_download
        missing_error = EntryNotFoundError
    else:
        missing_error = FileNotFoundError
    from huggingface_hub import CommitOperationAdd
    folder = Path(folder)
    report = json.loads((folder/'validation_report.json').read_text())
    provenance = json.loads((folder/'provenance.json').read_text())
    if report.get('status') != 'passed' or report['source_commit'] != provenance['source_commit']:
        raise RuntimeError('Export validation failed or provenance is inconsistent.')
    # Use the existing repository only. No creation or visibility-setting calls.
    info = api.repo_info(repo_id=DESTINATION, repo_type='dataset')
    parent = info.sha
    changes = []
    for name in MANAGED:
        local = (folder/name).read_bytes()
        try:
            old = Path(download(repo_id=DESTINATION, filename=name, repo_type='dataset',
                                revision=parent, token=token)).read_bytes()
        except missing_error:
            old = None
        if old != local:
            changes.append(CommitOperationAdd(path_in_repo=name, path_or_fileobj=local))
    if not changes:
        return 'No changes; the dataset is already up to date.'
    api.create_commit(repo_id=DESTINATION, repo_type='dataset', operations=changes,
        parent_commit=parent,
        commit_message='Sync accessible chatbot knowledge from GitHub',
        commit_description='Source commit: ' + provenance['source_commit'])
    return f'Updated {len(changes)} managed files. Dataset visibility is unchanged.'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', required=True)
    args = parser.parse_args()
    try:
        result = publish(args.folder, os.environ.get('HF_TOKEN'))
    except Exception as exc:
        # Avoid logging HTTP bodies, credentials or signed download URLs.
        print('Publishing failed (' + type(exc).__name__ + '). Check source visibility, HF_TOKEN permissions and dataset access.', file=sys.stderr)
        return 1
    print(result)
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as handle:
            handle.write('## Hugging Face dataset update\n\n' + result + '\n')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
