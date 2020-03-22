import os
import pytest
from _pytest.tmpdir import TempdirFactory
from py._path.local import LocalPath
from uyaml.file import File, Content, safe_path

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
    assert safe_path("file.txt", extensions=("txt", "jpeg"))


def test_not_safe_path() -> None:
    with pytest.raises(ValueError):
        safe_path("file.txt", extensions=("img",))
