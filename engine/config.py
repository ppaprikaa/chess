from typing import Any, Dict
import json

def load_config(filepath: str) -> Dict[Any, Any]:
    with open(filepath, "r") as f:
        config = json.load(f)

    return config
