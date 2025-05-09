# molecule/default/tests/test_php_ppa.py
import pytest
from utils import load_yaml

vars = load_yaml("../vars/php.yml")

php_ppa_dependencies = vars["php_ppa_dependencies"]


@pytest.mark.parametrize("pkg", php_ppa_dependencies)
def test_php_ppa_dependencies_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


def test_php_ppa_source_file_exists(host):
    list_result = host.run("grep -l 'ondrej/php' /etc/apt/sources.list.d/*.list")
    sources_result = host.run("grep -l 'ondrej/php' /etc/apt/sources.list.d/*.sources")

    if list_result.rc == 0:
        print("Matched .list file(s):\n", list_result.stdout)
    if sources_result.rc == 0:
        print("Matched .sources file(s):\n", sources_result.stdout)

    assert list_result.rc == 0 or sources_result.rc == 0, (
        "No apt source (.list or .sources) references the Ondřej PHP PPA."
    )


def test_php_ppa_present_in_sources(host):
    list_result = host.run("grep '^deb .*ondrej/php' /etc/apt/sources.list.d/*.list")
    sources_result = host.run("grep 'ondrej/php' /etc/apt/sources.list.d/*.sources")

    if list_result.rc == 0:
        print("Found 'deb' entries in .list files:\n", list_result.stdout)
    if sources_result.rc == 0:
        print("Found entries in .sources files:\n", sources_result.stdout)

    assert list_result.rc == 0 or sources_result.rc == 0, (
        "Ondřej PHP PPA not found in APT sources (neither .list nor .sources files)."
    )
