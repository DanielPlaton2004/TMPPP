from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, code: str, status: str) -> None: ...

class ShipmentSubject:
    def __init__(self, code: str):
        self._code = code; self._status="PENDING"; self._obs: List[Observer]=[]
    def attach(self, o: Observer) -> None:
        self._obs.append(o)
    def set_status(self, status: str) -> None:
        self._status=status
        for o in self._obs:
            o.update(self._code, self._status)

class ConsoleObserver(Observer):
    def update(self, code: str, status: str) -> None:
        print(f"[OBS] {code} => {status}")
