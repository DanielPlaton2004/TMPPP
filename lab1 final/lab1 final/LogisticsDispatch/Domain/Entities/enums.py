
from enum import Enum

class VehicleType(str, Enum):
    TRUCK = "Truck"
    VAN = "Van"

class ShipmentStatus(str, Enum):
    PENDING = "Pending"
    ASSIGNED = "Assigned"
    IN_TRANSIT = "In transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class PaymentStatus(str, Enum):
    UNPAID = "Unpaid"
    PAID = "Paid"
    FAILED = "Failed"
