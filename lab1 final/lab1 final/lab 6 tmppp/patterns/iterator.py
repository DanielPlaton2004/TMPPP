from typing import List, Iterator

class ShipmentCollection:
    def __init__(self, items: List[str] | None = None):
        self._items = list(items or [])
    def add(self, code: str) -> None:
        self._items.append(code)
    def remove(self, code: str) -> None:
        if code in self._items: self._items.remove(code)
    def snapshot(self) -> List[str]:
        return list(self._items)
    def iterator(self) -> "ShipmentCollectionIterator":
        return ShipmentCollectionIterator(self._items)

class ShipmentCollectionIterator:
    def __init__(self, items: List[str]):
        self._items = items; self._i=0
    def __iter__(self) -> Iterator[str]: return self
    def __next__(self) -> str:
        if self._i>=len(self._items): raise StopIteration
        v=self._items[self._i]; self._i+=1; return v
