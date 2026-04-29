from abc import ABC, abstractmethod

class TrackingProvider(ABC):
    @abstractmethod
    def get_status(self, tracking_code: str) -> str: ...


class OldCarrierApi:
    def track(self, code: str) -> dict:
        return {"code": code, "state": "IN_TRANSIT"}


class OldCarrierAdapter(TrackingProvider):
    def __init__(self, old_api: OldCarrierApi):
        self._old = old_api

    def get_status(self, tracking_code: str) -> str:
        data = self._old.track(tracking_code)
        return f"Tracking {data['code']}: {data['state']}"
