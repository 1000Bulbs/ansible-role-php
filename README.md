# Ansible Role: php

[![CI](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml/badge.svg)](https://github.com/1000Bulbs/ansible-role-php/actions/workflows/ci.yml)

This role installs and configures PHP with a customizable set of extensions, per-SAPI `php.ini` configuration, and support for deploying the `phing` build tool.

---

## Requirements

- Ansible 2.13+
- Python 3.9+ (for Molecule + testinfra)
- Tested on Ubuntu 22.04+

---

## Role Variables

These variables can be overridden in your inventory, playbooks, or `group_vars`.

### `defaults/main.yml`

```yaml
php_version: "5.6"

php_base_packages:
  - php-pear
  - php-php-gettext

php_extensions:
  - bcmath
  - curl
  - dev
  - gd
  - geoip
  - gmp
  - igbinary
  - imagick
  - mbstring
  - mcrypt
  - mysql
  - redis
  - soap
  - xdebug
  - xml
  - xmlrpc
  - yaml
  - zip

php_ini_sapi_configs:
  - sapi: apache2
    disable_functions:
      - pcntl_alarm
      - pcntl_fork
      - pcntl_waitpid
      - pcntl_wait
      - pcntl_wifexited
      - pcntl_wifstopped
      - pcntl_wifsignaled
      - pcntl_wexitstatus
      - pcntl_wtermsig
      - pcntl_wstopsig
      - pcntl_signal
      - pcntl_signal_dispatch
      - pcntl_get_last_error
      - pcntl_strerror
      - pcntl_sigprocmask
      - pcntl_sigwaitinfo
      - pcntl_sigtimedwait
      - pcntl_exec
      - pcntl_getpriority
      - pcntl_setpriority
    expose_php: "Off"
    memory_limit: "128M"

  - sapi: cli
    disable_functions: ""
    expose_php: "On"
    memory_limit: "-1"
```

---

## Dependencies

None.

---

## Installing the Role

To include this role in your project using a `requirements.yml` file:

```yaml
roles:
  - name: okb.php
    src: git@github.com:1000bulbs/ansible-role-php.git
    scm: git
    version: master
```

Then install it with:

```bash
ansible-galaxy role install -r requirements.yml
```

---

## Example Playbook

```yaml
- name: Install PHP
  hosts: all
  become: true
  roles:
    - role: okb.php
```

---

## Testing

This role uses [Molecule](https://molecule.readthedocs.io/) with `pytest-testinfra` for integration testing.

### Run tests locally

```bash
pip install -r requirements.txt
molecule test
```

Tests cover:

- PHP package installation (`php-pear`, `php-gettext`, dynamic extensions)
- PHP INI file configuration per SAPI (`cli`, `apache2`)
- Ondřej PHP PPA configuration
- `phing` binary copied to `/usr/local/bin/phing`
