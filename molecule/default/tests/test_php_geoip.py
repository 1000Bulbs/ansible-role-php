# molecule/default/tests/test_php_geoip.py

# Define variables as used in your role
php_version = "5.6"


def test_geoip_extension_file_exists(host):
    cmd = host.run(f"php{php_version} -r 'echo ini_get(\"extension_dir\");'")
    ext_dir = cmd.stdout.strip()
    geoip_so = host.file(f"{ext_dir}/geoip.so")

    assert geoip_so.exists, f"geoip.so not found in {ext_dir}"
    assert geoip_so.is_file
    assert geoip_so.user == "root"
    assert geoip_so.group == "root"
    assert geoip_so.mode & 0o444, "geoip.so is not readable"


def test_geoip_extension_enabled(host):
    cmd = host.run(f"php{php_version} -m")
    assert "geoip" in cmd.stdout, f"geoip extension not enabled in php{php_version}"
