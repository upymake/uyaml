import os
import pytest
from uyaml.file import File, Content, safe_path

_file: str = "file.txt"
_content: str = "test content"


@pytest.fixture(scope="session")
def file() -> Content:
    with File(_file, mode="a+") as file:  # type: Content
        yield file
    os.remove(_file)


def test_file_write(file: Content) -> None:
    assert file.write(_content) == len(_content)


def test_file_read(file: Content) -> None:
    assert not file.read()


def test_safe_path() -> None:
    assert safe_path("file.txt", extensions=("txt", "jpeg"))


def test_not_safe_path() -> None:
    with pytest.raises(ValueError):
        safe_path("file.txt", extensions=("img",))
