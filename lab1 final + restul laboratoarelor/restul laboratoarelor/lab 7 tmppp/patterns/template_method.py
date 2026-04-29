from abc import ABC, abstractmethod

class ReportTemplate(ABC):
    def generate(self) -> None:
        self.header(); data=self.collect(); self.format(data); self.footer()
    def header(self): print("=== REPORT START ===")
    @abstractmethod
    def collect(self) -> dict: ...
    @abstractmethod
    def format(self, data: dict) -> None: ...
    def footer(self): print("=== REPORT END ===")

class DailyReport(ReportTemplate):
    def collect(self) -> dict: return {"period":"daily","delivered":12,"failed":1}
    def format(self, data: dict) -> None: print("Daily:", data)

class MonthlyReport(ReportTemplate):
    def collect(self) -> dict: return {"period":"monthly","delivered":320,"failed":9}
    def format(self, data: dict) -> None: print("Monthly:", data)
