
from abc import ABC, abstractmethod

class Notifier(ABC):
    """ISP + DIP: interfață pentru notificări."""

    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"[EMAIL] {message}")
