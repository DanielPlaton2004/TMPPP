
from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")

class RepositoryBase(ABC, Generic[T]):
    """DIP: servicii depind de această abstracție."""

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def update(self, item: T) -> None:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def remove(self, item_id: int) -> bool:
        pass


class InMemoryRepository(RepositoryBase[T], Generic[T]):
    def __init__(self):
        self._data: Dict[int, T] = {}

    def add(self, item: T) -> None:
        self._data[getattr(item, "id")] = item

    def update(self, item: T) -> None:
        self._data[getattr(item, "id")] = item

    def get_by_id(self, item_id: int) -> Optional[T]:
        return self._data.get(item_id)

    def get_all(self) -> List[T]:
        return list(self._data.values())

    def remove(self, item_id: int) -> bool:
        return self._data.pop(item_id, None) is not None
