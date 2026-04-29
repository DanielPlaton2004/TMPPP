import threading
from typing import Any, Dict

class AppConfig:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self._data: Dict[str, Any] = {"price_per_km": 2.5}

    @classmethod
    def instance(cls) -> "AppConfig":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value
