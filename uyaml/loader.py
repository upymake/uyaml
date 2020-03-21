"""Module represents API to load data from specific YAML steam."""
from abc import ABC, abstractmethod
from typing import Dict, Any, IO
from yaml import safe_load
from uyaml.file import File, safe_path
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
        self._path: str = safe_path(path, extensions=("yaml",))
        self._content: List = List()

    def content(self) -> YamlType:
        return self._parsed.content()

    def section(self, name: str) -> YamlType:
        return self._parsed.section(name)

    @property
    def _parsed(self) -> Yaml:
        """Returns parsed YAML content."""
        if not self._content:
            with File(self._path) as file:  # type: IO[str]
                self._content.append(YamlFromStream(file))
        return self._content.first()
