"""Module contains interfaces to work with general usage files."""
from abc import abstractmethod
from types import TracebackType
from typing import Any, IO, List, Optional, Tuple, Type
from punish.type import AbstractContextManager


def _safe_path(path: str, extensions: Tuple[str, ...]) -> str:
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


def safe_yaml_path(path: str) -> str:
    """Returns safe `YAML` filename.

    Args:
        path (str): filepath
    """
    return _safe_path(path, extensions=("yml", "yaml"))


class Content(AbstractContextManager):
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
    def read(self, number: int = -1) -> str:
        """Reads a content."""
        pass

    @abstractmethod
    def readlines(self, hint: int = -1) -> List[str]:
        """Reads line by line."""
        pass


class File(Content):
    """Represents text file object."""

    def __init__(self, path: str, mode: str = "r") -> None:
        self._stream: IO[str] = open(path, mode)

    def write(self, content: str) -> int:
        return self._stream.write(content)

    def read(self, number: int = -1) -> str:
        return self._stream.read(number)

    def readlines(self, hint: int = -1) -> List[str]:
        return self._stream.readlines(hint)

    def __enter__(self) -> Any:
        """Returns file itself."""
        return self._stream

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Closes file stream itself."""
        self._stream.close()


class YamlFile(Content):
    """Represents `YAML` file object."""

    def __init__(self, path: str, mode: str = "r") -> None:
        self._file: Content = File(safe_yaml_path(path), mode)

    def write(self, content: str) -> int:
        return self._file.write(content)

    def read(self, number: int = -1) -> str:
        return self._file.read(number)

    def readlines(self, hint: int = -1) -> List[str]:
        return self._file.readlines(hint)

    def __enter__(self) -> Any:
        """Returns YAML file itself."""
        return self._file.__enter__()

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Closes YAML file stream itself."""
        self._file.__exit__(exception_type, exception_value, traceback)
