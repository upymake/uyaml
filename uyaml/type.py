"""Module contains interfaces to work with types."""
from typing import Any


class List(list):  # type: ignore
    """Represents custom list object."""

    def first(self) -> Any:
        """Returns first element of a list."""
        return self._invoke(index=0)

    def last(self) -> Any:
        """Returns last element of a list."""
        return self._invoke(index=-1)

    def _invoke(self, index: int) -> Any:
        """Returns nth element of a list."""
        return self[index]
