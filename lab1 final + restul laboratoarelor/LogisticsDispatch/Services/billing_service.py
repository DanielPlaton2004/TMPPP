
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.invoice import Invoice
from LogisticsDispatch.Domain.Entities.payment import Payment
from LogisticsDispatch.Domain.Entities.enums import PaymentStatus
from LogisticsDispatch.Services.notifier import Notifier

class BillingService:
    """SRP: facturi + plăți."""

    def __init__(self, invoice_repo: RepositoryBase[Invoice], payment_repo: RepositoryBase[Payment], notifier: Notifier):
        self._invoices = invoice_repo
        self._payments = payment_repo
        self._notifier = notifier

    def create_invoice(self, shipment_id: int, amount: float) -> Invoice:
        invoice = Invoice(id=self._next_invoice_id(), shipment_id=shipment_id, amount=amount, status=PaymentStatus.UNPAID)
        invoice.validate()
        self._invoices.add(invoice)
        return invoice

    def pay_invoice(self, invoice_id: int, method: str = "Cash") -> bool:
        inv = self._invoices.get_by_id(invoice_id)
        if not inv:
            return False
        if inv.status == PaymentStatus.PAID:
            return True

        payment = Payment(id=self._next_payment_id(), invoice_id=invoice_id, amount=inv.amount, status=PaymentStatus.PAID, method=method or "Cash")
        payment.validate()
        self._payments.add(payment)

        inv.status = PaymentStatus.PAID
        inv.touch()
        self._invoices.update(inv)

        self._notifier.notify(f"Invoice #{inv.id} paid ({payment.method}) for shipment #{inv.shipment_id}.")
        return True

    def list_invoices(self):
        return self._invoices.get_all()

    def list_payments(self):
        return self._payments.get_all()

    def _next_invoice_id(self) -> int:
        ids = [i.id for i in self._invoices.get_all()]
        return (max(ids) + 1) if ids else 1

    def _next_payment_id(self) -> int:
        ids = [p.id for p in self._payments.get_all()]
        return (max(ids) + 1) if ids else 1
