# molecule/default/tests/test_phing.py
from utils import load_yaml

vars = load_yaml("../vars/php.yml")

php_phing_file = vars["php_phing_file"]


def test_phing_file_exists(host):
    f = host.file(php_phing_file)
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
