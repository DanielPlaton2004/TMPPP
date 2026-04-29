from abc import ABC, abstractmethod
import json

class ReportRenderer(ABC):
    @abstractmethod
    def render(self, data: dict) -> None: ...

class ConsoleRenderer(ReportRenderer):
    def render(self, data: dict) -> None:
        print("Report:", data)

class JsonRenderer(ReportRenderer):
    def render(self, data: dict) -> None:
        print(json.dumps(data, ensure_ascii=False))

class DispatchReport:
    def __init__(self, renderer: ReportRenderer):
        self._r = renderer
    def render(self, data: dict) -> None:
        self._r.render(data)
