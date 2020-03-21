"""Module contains interfaces to to work with general usage files."""
from abc import abstractmethod
from typing import Optional, Type, IO, Tuple
from types import TracebackType
from uyaml.connection import Friendly


def safe_path(path: str, extensions: Tuple[str, ...]) -> str:
    """Returns safe filename based on given extensions.

    Args:
        path (str): filepath
        extensions (tuple[str, ...]): a list of allowed extensions

    Raises:
        `ValueError` if path is invalid
    """
    if not path.endswith(extensions):
        raise ValueError(f"Given {path} does not match with allowed {extensions} extensions!")
    return path


class Content(Friendly):
    """Represent abstraction a content."""

    @abstractmethod
    def write(self, content: str) -> int:
        """Writes data into content.

        Args:
            content (str): content to write

        Returns amount of written characters
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

    def write(self, content: str) -> int:
        return self._stream.write(content)

    def read(self) -> str:
        return "".join(self._stream.readlines())

    def __enter__(self) -> Content:
        """Returns file itself."""
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Closes file stream itself."""
        self._stream.close()
