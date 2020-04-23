"""Module represents API to load data from specific YAML steam."""
from abc import ABC, abstractmethod
from types import TracebackType
from typing import Any, IO, Dict, Optional, Type
from punish.type import AbstractContextManager
from yaml import safe_load
from uyaml.file import YamlFile
from uyaml.type import List

YamlType = Dict[Any, Any]


class Yaml(ABC):
    """Represents an interface to operate YAML files."""

    @abstractmethod
    def content(self) -> YamlType:
        """Returns whole content from the YAML file as a dictionary."""
        pass

    @abstractmethod
    def section(self, name: str) -> YamlType:
        """Returns top section of a data from YAML file as a dictionary.

        Args:
            name (str): name of a section
        """
        pass


class YamlFromStream(Yaml):
    """Represents stream of `Yaml` object."""

    def __init__(self, stream: IO[str]) -> None:
        self._stream: YamlType = safe_load(stream)

    def content(self) -> YamlType:
        return self._stream

    def section(self, name: str) -> YamlType:
        return self._stream[name]


class YamlFromPath(Yaml):
    """Represents a filepath as a `YAML` object."""

    def __init__(self, path: str) -> None:
        self._path: str = path
        self._content: List = List()

    def content(self) -> YamlType:
        return self._parsed.content()

    def section(self, name: str) -> YamlType:
        return self._parsed.section(name)

    @property
    def _parsed(self) -> Yaml:
        """Returns parsed YAML content."""
        if not self._content:
            with YamlFile(self._path) as file:  # type: IO[str]
                self._content.append(YamlFromStream(file))
        return self._content.first()


class ContextYamlFromPath(AbstractContextManager, Yaml):
    """Represents a filepath as a `YAML` context manager object."""

    def __init__(self, path: str) -> None:
        self._path: str = path
        self._content: List = List()

    def __enter__(self) -> Yaml:
        """Returns YAML content itself."""
        if not self._content:
            with YamlFile(self._path) as file:  # type: IO[str]
                self._content.append(YamlFromStream(file))
        return self

    def content(self) -> YamlType:
        return self._head.content()

    def section(self, name: str) -> YamlType:
        return self._head.section(name)

    @property
    def _head(self) -> Yaml:
        """Returns head of yaml content."""
        return self._content.first()

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Clears YAML content."""
        self._content.clear()
