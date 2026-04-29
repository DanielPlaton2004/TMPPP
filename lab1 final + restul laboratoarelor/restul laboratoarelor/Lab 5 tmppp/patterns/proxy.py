class DispatchService:
    def dispatch(self, code: str) -> str:
        return f"Dispatched {code}"

class DispatchServiceProxy:
    def __init__(self, real: DispatchService, role: str):
        self._real = real; self._role = role
    def dispatch(self, code: str) -> str:
        print(f"[LOG] role={self._role} dispatch({code})")
        if self._role not in ("dispatcher","admin"):
            return "❌ Access denied"
        return self._real.dispatch(code)
