import json, re
def evaluate_extraction(model_output: str) -> bool:
    try:
        json_str = re.search(r'```json(.*?)```', model_output, re.DOTALL)
        data = json.loads(json_str.group(1).strip()) if json_str else json.loads(model_output)
        assert "target_entity" in data
        return True
    except (json.JSONDecodeError, AssertionError):
        return False
