import os
from typing import IO
import pytest
from _pytest.tmpdir import TempdirFactory
from py._path.local import LocalPath
from uyaml.file import File
from uyaml.loader import YamlFromPath, Yaml, YamlFromStream, ContextYamlFromPath


@pytest.fixture(scope="session")
def path(tmpdir_factory: TempdirFactory) -> LocalPath:
    path: LocalPath = tmpdir_factory.mktemp("test").join("file.yaml")
    path.write(
        """
top:
  foo:
    content: empty
    priority: 0
  bar:
    content: empty
    priority: 1 
"""
    )
    yield path
    os.remove(path)


@pytest.fixture(scope="session")
def yaml_from_path(path: LocalPath) -> YamlFromPath:
    yield YamlFromPath(str(path))


@pytest.fixture(scope="session")
def context_yaml_from_path(path: LocalPath) -> YamlFromPath:
    with ContextYamlFromPath(str(path)) as yaml:  # type: IO[str]
        yield yaml


@pytest.fixture(scope="session")
def yaml_from_stream(path: LocalPath) -> YamlFromStream:
    with File(str(path)) as file:  # type: IO[str]
        yield YamlFromStream(file)


def test_parsed(yaml_from_path: YamlFromPath) -> None:
    assert isinstance(yaml_from_path._parsed, Yaml)


def test_from_path_content(yaml_from_path: Yaml) -> None:
    assert yaml_from_path.content() == {
        "top": {"foo": {"content": "empty", "priority": 0}, "bar": {"content": "empty", "priority": 1}}
    }


def test_from_path_section(yaml_from_path: Yaml) -> None:
    assert yaml_from_path.section("top") == {
        "foo": {"content": "empty", "priority": 0},
        "bar": {"content": "empty", "priority": 1},
    }


def test_from_stream_content(yaml_from_stream: Yaml) -> None:
    assert yaml_from_stream.content() == {
        "top": {"foo": {"content": "empty", "priority": 0}, "bar": {"content": "empty", "priority": 1}}
    }


def test_from_stream_section(yaml_from_stream: Yaml) -> None:
    assert yaml_from_stream.section("top")["foo"] == {"content": "empty", "priority": 0}


def test_context_from_path_content(context_yaml_from_path: Yaml) -> None:
    assert context_yaml_from_path.content() == {
        "top": {"foo": {"content": "empty", "priority": 0}, "bar": {"content": "empty", "priority": 1}}
    }


def test_context_from_path_section(context_yaml_from_path: Yaml) -> None:
    assert context_yaml_from_path.section("top") == {
        "foo": {"content": "empty", "priority": 0},
        "bar": {"content": "empty", "priority": 1},
    }


def test_context_from_path_head(context_yaml_from_path: ContextYamlFromPath) -> None:
    assert isinstance(context_yaml_from_path._head, Yaml)
