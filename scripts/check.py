"""Check published schema syntax and the shared Resource conformance contract."""
from pathlib import Path
import base64
import json
from jsonschema import Draft202012Validator, FormatChecker

root = Path(__file__).resolve().parents[1]
for path in (root / "schemas").glob("*.json"):
    value = json.loads(path.read_text(encoding="utf8"))
    assert value["$schema"] and value["$id"]
    Draft202012Validator.check_schema(value)
for path in (root / "specification").glob("*.md"):
    assert path.read_text(encoding="utf8").strip()
for path in (root / "conformance/v1").glob("*.json"):
    value = json.loads(path.read_text(encoding="utf8"))
    assert value["profile"] and value["cases"]
    names = [case["name"] for case in value["cases"]]
    assert len(names) == len(set(names))
    if path.stem == "containers":
        for case in value["cases"]:
            assert len(base64.b64decode(case["archive"], validate=True)) >= 144
    if path.stem == "resources":
        schema = json.loads((root / "schemas/resource.schema.json").read_text())
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for case in value["cases"]:
            assert validator.is_valid(case["value"]) == case["valid"], case["name"]
assert (root / "VERSION").read_text().strip()
print("Specification schemas and shared conformance contracts verified.")
