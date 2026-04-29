from patterns.chain import WeightHandler, InsuranceHandler, ComplianceHandler, ShipmentRequest
from patterns.state import ShipmentContext
from patterns.mediator import DispatchMediator, DriverColleague, VehicleColleague, WarehouseColleague
from patterns.template_method import DailyReport, MonthlyReport
from patterns.visitor import Shipment, CsvExportVisitor, XmlExportVisitor

def main():
    print("=== Chain ===")
    chain = WeightHandler()
    chain.set_next(InsuranceHandler()).set_next(ComplianceHandler())
    print(chain.handle(ShipmentRequest(9000, 3000, "Chișinău")))

    print("\n=== State ===")
    ctx = ShipmentContext("S-1")
    ctx.dispatch(); ctx.deliver()
    print("Final:", ctx.status())

    print("\n=== Mediator ===")
    med = DispatchMediator()
    med.register(DriverColleague(med,"Ion"), VehicleColleague(med,"TR-101"), WarehouseColleague(med,"WH-1"))
    med.dispatch("S-10")

    print("\n=== Template Method ===")
    DailyReport().generate()
    MonthlyReport().generate()

    print("\n=== Visitor ===")
    shipments = [Shipment("S1","Chișinău",1000), Shipment("S2","Bălți",500)]
    print(CsvExportVisitor().export(shipments))
    print(XmlExportVisitor().export(shipments))

if __name__ == "__main__":
    main()
