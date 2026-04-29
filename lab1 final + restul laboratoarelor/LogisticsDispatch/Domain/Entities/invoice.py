
from dataclasses import dataclass
from LogisticsDispatch.Domain.Entities.base_entity import BaseEntity
from LogisticsDispatch.Domain.Entities.enums import PaymentStatus

@dataclass
class Invoice(BaseEntity):
    shipment_id: int = 0
    amount: float = 0.0
    status: PaymentStatus = PaymentStatus.UNPAID

    def validate(self) -> None:
        if self.shipment_id <= 0:
            raise ValueError("shipment_id must be > 0.")
        if self.amount < 0:
            raise ValueError("amount must be >= 0.")
