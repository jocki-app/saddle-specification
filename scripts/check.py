from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
for path in (root/'schemas').glob('*.json'):
    value=json.loads(path.read_text());assert value['$schema'] and value['$id']
for path in (root/'specification').glob('*.md'):
    assert path.read_text().strip()
print('Specification documents and JSON schemas verified.')
