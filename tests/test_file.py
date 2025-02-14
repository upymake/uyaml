# pylint: disable-all
import os
import pytest
from _pytest.tmpdir import TempdirFactory
from py._path.local import LocalPath
from uyaml.file import File, Content, _safe_path, safe_yaml_path

_file: str = "file.txt"
_content: str = "test"


@pytest.fixture(scope="session")
def file(tmpdir_factory: TempdirFactory) -> Content:
    path: LocalPath = tmpdir_factory.mktemp(_content).join(_file)
    with File(path, mode="a+") as file:  # type: Content
        yield file
    if os.path.exists(path):
        os.remove(path)


def test_file_write(file: Content) -> None:
    assert file.write(_content) == len(_content)


def test_file_read(file: Content) -> None:
    assert not file.read()


def test_safe_path() -> None:
    assert _safe_path(_file, extensions=("txt", "jpeg"))


def test_not_safe_path() -> None:
    with pytest.raises(ValueError):
        _safe_path(_file, extensions=("img",))


def test_safe_yaml_path() -> None:
    assert safe_yaml_path("file.yaml")


def test_not_safe_yaml_path() -> None:
    with pytest.raises(ValueError):
        safe_yaml_path("file.png")
