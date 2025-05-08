# molecule/default/tests/test_php_ini.py

import pytest
import yaml
from pathlib import Path

with open(Path(__file__).resolve().parent / "../vars/php.yml") as f:
    vars = yaml.safe_load(f)

php_version = vars["php_version"]
php_ini_sapi_configs = vars["php_ini_sapi_configs"]


@pytest.mark.parametrize("config", php_ini_sapi_configs, ids=lambda x: x["sapi"])
def test_php_ini_contains_expected_values(host, config):
    path = f"/etc/php/{php_version}/{config['sapi']}/php.ini"
    ini = host.file(path).content_string

    # Basic settings
    assert f"memory_limit = {config['memory_limit']}" in ini
    assert f"expose_php = {config['expose_php']}" in ini

    # Disable functions may be a list or string
    if isinstance(config["disable_functions"], list):
        expected_disabled = ",".join(config["disable_functions"])
    else:
        expected_disabled = config["disable_functions"]

    assert f"disable_functions = {expected_disabled}" in ini
