from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def dispatch(self, ctx): ...
    @abstractmethod
    def deliver(self, ctx): ...
    @abstractmethod
    def cancel(self, ctx): ...
    @abstractmethod
    def name(self) -> str: ...

class Pending(State):
    def dispatch(self, ctx): ctx._state = InTransit()
    def deliver(self, ctx): pass
    def cancel(self, ctx): ctx._state = Cancelled()
    def name(self): return "PENDING"

class InTransit(State):
    def dispatch(self, ctx): pass
    def deliver(self, ctx): ctx._state = Delivered()
    def cancel(self, ctx): ctx._state = Cancelled()
    def name(self): return "IN_TRANSIT"

class Delivered(State):
    def dispatch(self, ctx): pass
    def deliver(self, ctx): pass
    def cancel(self, ctx): pass
    def name(self): return "DELIVERED"

class Cancelled(State):
    def dispatch(self, ctx): pass
    def deliver(self, ctx): pass
    def cancel(self, ctx): pass
    def name(self): return "CANCELLED"

class ShipmentContext:
    def __init__(self, code: str):
        self._code = code
        self._state: State = Pending()
    def dispatch(self):
        self._state.dispatch(self); print(f"{self._code}: {self._state.name()}")
    def deliver(self):
        self._state.deliver(self); print(f"{self._code}: {self._state.name()}")
    def cancel(self):
        self._state.cancel(self); print(f"{self._code}: {self._state.name()}")
    def status(self) -> str:
        return self._state.name()
