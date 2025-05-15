# molecule/default/tests/test_php_packages.py
import pytest
from utils import load_yaml

vars = load_yaml("../vars/all.yml")

php_version = vars["php_version"]
php_base_packages = vars["php_base_packages"]
php_extensions = vars["php_extensions"]


expected_packages = php_base_packages + [
    f"php{php_version}-{ext}" for ext in php_extensions
]


@pytest.mark.parametrize("pkg", expected_packages)
def test_php_package_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
