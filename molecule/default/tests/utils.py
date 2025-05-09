# molecule/default/tests/utils.py
import yaml
from pathlib import Path


def load_yaml(relative_path, default=None):
    try:
        full_path = (Path(__file__).resolve().parent / relative_path).resolve()
        with open(full_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return default or {}
