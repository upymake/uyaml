![Screenshot](icon.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/uyaml.svg?branch=master)](https://travis-ci.org/vyahello/uyaml)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/uyaml/badge.svg?branch=master)](https://coveralls.io/github/vyahello/uyaml?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with pydocstyle](https://img.shields.io/badge/pydocstyle-checked-yellowgreen)](http://www.pydocstyle.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![PyPI version shields.io](https://img.shields.io/pypi/v/uyaml.svg)](https://pypi.python.org/pypi/uyaml/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/uyaml.svg)](https://pypi.python.org/pypi/uyaml/)
[![Downloads](https://pepy.tech/badge/uyaml)](https://pepy.tech/project/uyaml)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/uyaml/badge)](https://www.codefactor.io/repository/github/vyahello/uyaml)

# uYAML

> Provides user-friendly interface for YAML data stream serialization with OOP support.
>
> Basically it is a wrapper over **pyyaml** python library.

## Tools

- python 3.6 | 3.7 | 3.8
- [pyyaml](https://github.com/yaml/pyyaml) library
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)

## Usage

### Installation

Please run following script to obtain latest package from PYPI:
```bash
➜ pip install uyaml
✨ 🍰 ✨
```
### Quick start

```python
>>> from uyaml.loader import Yaml, YamlFromPath
>>>
>>> yaml: Yaml = YamlFromPath("path/to/config.yaml")
>>> yaml.content()
{"top": 
  {
    "foo": {"content": "empty", "priority": 0}, 
    "bar": {"content": "empty", "priority": 1}
  }
}
>>> yaml.section(name="top")
{
  "foo": {"content": "empty", "priority": 0}, 
  "bar": {"content": "empty", "priority": 1}
}
```
### Source code

```bash
➜ git clone git@github.com:vyahello/uyaml.git
➜ pip install -e .
```

Or using direct source:
```bash
➜ pip install git+https://github.com/vyahello/uyaml@0.0.1
```
**[⬆ back to top](#uyaml)**

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`, `mypy`, `pydocstyle`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
➜ ./analyse-source-code.sh
```
### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies

**[⬆ back to top](#uyaml)**
