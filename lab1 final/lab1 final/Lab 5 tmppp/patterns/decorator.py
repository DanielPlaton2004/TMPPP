from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[EMAIL] {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrappee: Notifier):
        self._w = wrappee
    def send(self, message: str) -> None:
        self._w.send(message)

class SmsDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[SMS] {message}")

class PushDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[PUSH] {message}")
