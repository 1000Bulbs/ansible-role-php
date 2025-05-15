# molecule/default/tests/test_php_geoip.py
from utils import load_yaml

vars = load_yaml("../vars/all.yml")

php_version = vars["php_version"]


def test_geoip_extension_file_exists(host):
    """
    Test that the geoip PHP extension file exists in the extension directory,
    is a regular file, owned by root, and is readable.
    """
    cmd = host.run(f"php{php_version} -r 'echo ini_get(\"extension_dir\");'")
    ext_dir = cmd.stdout.strip()
    geoip_so = host.file(f"{ext_dir}/geoip.so")

    assert geoip_so.exists, f"geoip.so not found in {ext_dir}"
    assert geoip_so.is_file
    assert geoip_so.user == "root"
    assert geoip_so.group == "root"
    assert geoip_so.mode & 0o444, "geoip.so is not readable"


def test_geoip_extension_enabled(host):
    """
    Test that the geoip extension is enabled in the PHP installation.
    """
    cmd = host.run(f"php{php_version} -m")
    assert "geoip" in cmd.stdout, f"geoip extension not enabled in php{php_version}"
