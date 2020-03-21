import pytest


@pytest.mark.parametrize(
    "name",
    (pytest.param("foo", marks=pytest.mark.fake, id="foo"), pytest.param("bar", marks=pytest.mark.fake, id="bar")),
)
def test_fake(name: str) -> None:
    assert isinstance(name, str)
