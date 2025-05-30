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

php_ini_sapi_configs = [
    {
        "sapi": "fpm",
        "disable_functions": ["pcntl_alarm", "pcntl_fork"],
        "expose_php": "Off",
        "memory_limit": "128M",
    },
    {"sapi": "cli", "disable_functions": "", "expose_php": "On", "memory_limit": "-1"},
]


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
