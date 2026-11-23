from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
for path in (root/'schemas').glob('*.json'):
    value=json.loads(path.read_text());assert value['$schema'] and value['$id']
for path in (root/'specification').glob('*.md'):
    assert path.read_text().strip()
print('Specification documents and JSON schemas verified.')

for path in (root/'conformance/v1').glob('*.json'):
    value=json.loads(path.read_text());assert value['profile'] and value['cases']
    names=[case['name'] for case in value['cases']];assert len(names)==len(set(names))
    if path.stem=='containers':
        import base64
        for case in value['cases']:assert len(base64.b64decode(case['archive'],validate=True))>=144
assert (root/'VERSION').read_text().strip()
