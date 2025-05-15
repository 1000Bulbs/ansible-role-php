# molecule/default/tests/test_php_ppa.py
import pytest
from utils import load_yaml

vars = load_yaml("../vars/all.yml")

php_ppa_dependencies = vars["php_ppa_dependencies"]
php_repo = vars["php_repo"]


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
