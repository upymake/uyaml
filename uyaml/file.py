"""Module contains interfaces to to work with general usage files."""
from abc import abstractmethod
from typing import Any, Optional, Type, IO
from types import TracebackType
from uyaml.connection import Friendly


class Content(Friendly):
    """Represent abstraction a content."""

    @abstractmethod
    def write(self, content: str) -> None:
        """Writes data into content.

        Args:
            content (str): content to write
        """
        pass

    @abstractmethod
    def read(self) -> str:
        """Reads a content."""
        pass


class File(Content):
    """Represents text file object."""

    def __init__(self, file: str, mode: str = "r") -> None:
        self._stream: IO[str] = open(file, mode)

    def write(self, content: str) -> None:
        self._stream.write(content)

    def read(self) -> str:
        return "".join(self._stream.readlines())

    def __enter__(self) -> Any:
        """Returns file itself."""
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Closes file stream itself."""
        pass
