# molecule/default/tests/test_default.py
import pytest

php_ppa_dependencies = ["software-properties-common", "gnupg", "gpg-agent"]

php_repo = "ondrej/php"

php_version = "5.6"

php_base_packages = ["php-pear", "php-php-gettext"]

php_extensions = [
    "bcmath",
    "curl",
    "dev",
    "gd",
    "geoip",
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

expected_packages = php_base_packages + [
    f"php{php_version}-{ext}" for ext in php_extensions
]

php_fpm_systemd_service_name = "php5.6-fpm"


@pytest.mark.parametrize("pkg", php_ppa_dependencies)
def test_php_ppa_dependencies_installed(host, pkg):
    """
    Test that the specified PHP PPA dependency package is installed.
    """
    package = host.package(pkg)
    assert package.is_installed


def test_php_ppa_source_file_exists(host):
    """
    Test that at least one APT source file (.list or .sources) references the Ondřej PHP PPA.
    """
    list_result = host.run("grep -l 'ondrej/php' /etc/apt/sources.list.d/*.list")
    sources_result = host.run("grep -l 'ondrej/php' /etc/apt/sources.list.d/*.sources")

    assert list_result.rc == 0 or sources_result.rc == 0, (
        "No apt source (.list or .sources) references the Ondřej PHP PPA."
    )


def test_php_ppa_present_in_sources(host):
    """
    Test that the Ondřej PHP PPA is present in the APT sources.
    """
    list_result = host.run("grep '^deb .*ondrej/php' /etc/apt/sources.list.d/*.list")
    sources_result = host.run("grep 'ondrej/php' /etc/apt/sources.list.d/*.sources")

    assert list_result.rc == 0 or sources_result.rc == 0, (
        "Ondřej PHP PPA not found in APT sources (neither .list nor .sources files)."
    )


@pytest.mark.parametrize("pkg", expected_packages)
def test_php_package_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


def test_php_fpm_service_is_enabled(host):
    svc = host.service(php_fpm_systemd_service_name)
    assert svc.is_enabled


def test_php_fpm_service_is_running(host):
    svc = host.service(php_fpm_systemd_service_name)
    assert svc.is_running
