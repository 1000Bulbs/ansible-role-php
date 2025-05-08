# molecule/default/tests/test_php_packages.py
import pytest

# Define variables as used in your role
php_version = "5.6"

php_base_packages = [
    "php-pear",
    "php-php-gettext",
]

php_extensions = [
    "bcmath",
    "curl",
    "dev",
    "gd",
    "gmp",
    "igbinary",
    "imagick",
    "mbstring",
    "mcrypt",
    "mysql",
    "redis",
    "soap",
    "xdebug",
    "xml",
    "xmlrpc",
    "yaml",
    "zip",
]

# Build full expected package list
expected_packages = php_base_packages + [
    f"php{php_version}-{ext}" for ext in php_extensions
]


@pytest.mark.parametrize("pkg", expected_packages)
def test_php_package_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
