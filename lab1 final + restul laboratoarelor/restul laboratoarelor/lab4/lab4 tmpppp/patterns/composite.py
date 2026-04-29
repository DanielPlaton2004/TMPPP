from abc import ABC, abstractmethod
from typing import List

class ShipmentComponent(ABC):
    @abstractmethod
    def total_cost(self) -> float: ...

    @abstractmethod
    def name(self) -> str: ...


class ShipmentLeaf(ShipmentComponent):
    def __init__(self, code: str, weight_kg: float, price_per_kg: float):
        self._code = code
        self._weight = weight_kg
        self._ppk = price_per_kg

    def total_cost(self) -> float:
        return self._weight * self._ppk

    def name(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return f"ShipmentLeaf(code={self._code}, weight_kg={self._weight}, price_per_kg={self._ppk})"


class ShipmentGroup(ShipmentComponent):
    def __init__(self, group_name: str):
        self._name = group_name
        self._children: List[ShipmentComponent] = []

    def add(self, component: ShipmentComponent) -> None:
        self._children.append(component)

    def remove(self, component: ShipmentComponent) -> None:
        self._children.remove(component)

    def total_cost(self) -> float:
        return sum(c.total_cost() for c in self._children)

    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"ShipmentGroup(name={self._name}, items={len(self._children)})"
