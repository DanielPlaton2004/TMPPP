from abc import ABC, abstractmethod
from patterns.iterator import ShipmentCollection

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class DispatchCommand(Command):
    def __init__(self, c: ShipmentCollection, code: str): self._c=c; self._code=code
    def execute(self) -> None: self._c.add(self._code)
    def undo(self) -> None: self._c.remove(self._code)

class CancelCommand(Command):
    def __init__(self, c: ShipmentCollection, code: str): self._c=c; self._code=code; self._existed=False
    def execute(self) -> None:
        self._existed = self._code in self._c.snapshot()
        self._c.remove(self._code)
    def undo(self) -> None:
        if self._existed: self._c.add(self._code)

class CommandInvoker:
    def __init__(self): self._h: list[Command]=[]
    def execute(self, cmd: Command) -> None:
        cmd.execute(); self._h.append(cmd)
    def undo(self) -> None:
        if self._h: self._h.pop().undo()
