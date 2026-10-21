"""Verify released byte hashes and the internal token arithmetic. Offline."""
from pathlib import Path
import hashlib,json
from decimal import Decimal

root=Path(__file__).resolve().parent
m=json.loads((root/'provenance/release_manifest.json').read_text())
for entry in m['files']:
    p=root/entry['path']
    assert p.is_file(),f'Missing: {p}'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],f'Changed: {p}'
agents=json.loads((root/'accounting/agents.json').read_text())
turns=json.loads((root/'accounting/turns.json').read_text())
assert len(agents)==25 and len(turns)==37
assert len(list((root/'archive/tracks').glob('*/submissions/*.md')))==16
for a in agents:
    tt=[t for t in turns if t['role']==a['role']]
    for key in ['input_tokens','cached_input_tokens','output_tokens','reasoning_tokens','total_tokens']:
        assert sum(t[key] for t in tt)==a[key],(a['role'],key)
    assert a['input_tokens']+a['output_tokens']==a['total_tokens']
    estimated=(Decimal(a['input_tokens']-a['cached_input_tokens'])*10+Decimal(a['cached_input_tokens'])+Decimal(a['output_tokens'])*50)/1000000
    assert estimated==Decimal(a['standard_usd_estimate'])
assert sum(a['total_tokens'] for a in agents)==99078174
assert sum(Decimal(a['standard_usd_estimate']) for a in agents)==Decimal('181.154884')
print(f"Verified {len(m['files'])} file hashes, 16 submissions, 25 sessions and 37 turns.")
