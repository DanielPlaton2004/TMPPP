from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass(frozen=True)
class Address:
    country: str; city: str; street: str

class AddressFlyweightFactory:
    def __init__(self):
        self._pool: Dict[Tuple[str,str,str], Address] = {}
    def get(self, country: str, city: str, street: str) -> Address:
        k = (country, city, street)
        if k not in self._pool:
            self._pool[k] = Address(country, city, street)
        return self._pool[k]
    def pool_size(self) -> int:
        return len(self._pool)
