"""Module contains interfaces to work with connections."""
from abc import abstractmethod
from types import TracebackType
from typing import Any, ContextManager, Optional, Type


class Friendly(ContextManager["Friendly"]):
    """An interface describing a friendly context manager connection."""

    @abstractmethod
    def __enter__(self) -> Any:
        """Returns connection itself."""
        pass

    @abstractmethod
    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Closes connection itself."""
        pass
