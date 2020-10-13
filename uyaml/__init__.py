"""Provides user-friendly interface for YAML data stream serialization with OOP support."""
from typing import Tuple
from uyaml.file import File, Content, safe_yaml_path
from uyaml.loader import YamlFromPath, Yaml, YamlFromStream, ContextYamlFromPath

__author__: str = "Volodymyr Yahello"
__email__: str = "vyahello@gmail.com"
__version__: str = "0.0.7"

__all__: Tuple[str, ...] = (
    "File",
    "Content",
    "safe_yaml_path",
    "YamlFromPath",
    "Yaml",
    "YamlFromStream",
    "ContextYamlFromPath",
)
