from abc import ABC, abstractmethod

class RouteStrategy(ABC):
    @abstractmethod
    def compute(self, origin: str, dest: str) -> str: ...

class FastestRouteStrategy(RouteStrategy):
    def compute(self, origin: str, dest: str) -> str:
        return f"Fastest route {origin}->{dest} (highway)"

class CheapestRouteStrategy(RouteStrategy):
    def compute(self, origin: str, dest: str) -> str:
        return f"Cheapest route {origin}->{dest} (avoid tolls)"

class RoutePlanner:
    def __init__(self, strategy: RouteStrategy):
        self._s = strategy
    def set_strategy(self, strategy: RouteStrategy) -> None:
        self._s = strategy
    def plan(self, origin: str, dest: str) -> str:
        return self._s.compute(origin, dest)
