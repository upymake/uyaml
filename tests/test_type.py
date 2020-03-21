import pytest
from uyaml.type import List


@pytest.fixture(scope="module")
def list_() -> List:
    yield List("123")


def test_invoke(list_: List) -> None:
    assert list_._invoke(index=1) == "2"


def test_first(list_: List) -> None:
    assert list_.first() == "1"


def test_last(list_: List) -> None:
    assert list_.last() == "3"
