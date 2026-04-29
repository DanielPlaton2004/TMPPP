from dataclasses import dataclass
from typing import List
from patterns.iterator import ShipmentCollection

@dataclass(frozen=True)
class ShipmentMemento:
    state: List[str]

class ShipmentCaretaker:
    def __init__(self, collection: ShipmentCollection):
        self._c = collection
        self._initial = ShipmentMemento(collection.snapshot())
    def restore_initial(self) -> None:
        self._c._items = list(self._initial.state)  # demo simplu
