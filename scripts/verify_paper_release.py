"""Verify the public Astra paper bundle without network access or model calls."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
astra=root/'experiments/reciprocal-simplex-astra6'
m=json.loads((astra/'provenance/paper_release_manifest.json').read_text())
for f in m['files']:
    p=root/f['path']
    assert p.is_file(),f['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f['path']
rows=[json.loads(s) for s in (astra/'02_writing_record/accounting/agent_turns.jsonl').read_text().splitlines()]
assert len(rows)==5
for r in rows:
    u=r['usage']
    assert u['input_tokens']+u['output_tokens']==u['total_tokens']
    assert 0<=u['cached_input_tokens']<=u['input_tokens']
    assert 0<=u['reasoning_output_tokens']<=u['output_tokens']
    assert r['model']=='gpt-6-astra' and r['effort']=='xhigh'
results=json.loads((astra/'01_simulation/data/results.json').read_text())
assert len(results['results'])==18
print(f"Verified {len(m['files'])} published file hashes, 5 writing turns and 18 simulation bins.")
