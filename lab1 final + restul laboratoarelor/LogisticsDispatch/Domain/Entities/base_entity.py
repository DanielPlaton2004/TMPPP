
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class BaseEntity:
    """Clasă de bază (moștenire): id + timestamps."""
    id: int
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def touch(self) -> None:
        self.updated_at = datetime.utcnow()
