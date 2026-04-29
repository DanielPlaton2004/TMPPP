
from LogisticsDispatch.Domain.Entities.client import Client
from LogisticsDispatch.Domain.Entities.truck import Truck
from LogisticsDispatch.Domain.Entities.van import Van
from LogisticsDispatch.Domain.Entities.driver import Driver
from LogisticsDispatch.Domain.Entities.shipment import Shipment

from LogisticsDispatch.Infrastructure.Repositories.in_memory_repositories import (
    ClientRepository, VehicleRepository, DriverRepository,
    ShipmentRepository, InvoiceRepository, PaymentRepository
)

from LogisticsDispatch.Services.notifier import EmailNotifier
from LogisticsDispatch.Services.client_service import ClientService
from LogisticsDispatch.Services.driver_service import DriverService
from LogisticsDispatch.Services.fleet_service import FleetService
from LogisticsDispatch.Services.shipment_service import ShipmentService
from LogisticsDispatch.Services.billing_service import BillingService
from LogisticsDispatch.Services.dispatch_service import DispatchService


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Introduce un număr întreg.")

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Introduce un număr (float).")

def read_str(prompt: str) -> str:
    return input(prompt).strip()


class Program:
    @staticmethod
    def main():
        # Repository concrete (InMemory) – ca în exemplul colegului
        client_repo = ClientRepository()
        vehicle_repo = VehicleRepository()
        driver_repo = DriverRepository()
        shipment_repo = ShipmentRepository()
        invoice_repo = InvoiceRepository()
        payment_repo = PaymentRepository()

        # Servicii concrete cu injectare (DIP)
        notifier = EmailNotifier()
        client_service = ClientService(client_repo)
        fleet_service = FleetService(vehicle_repo)
        driver_service = DriverService(driver_repo, vehicle_repo)
        shipment_service = ShipmentService(shipment_repo, client_repo)
        billing_service = BillingService(invoice_repo, payment_repo, notifier)
        dispatch_service = DispatchService(shipment_repo, driver_repo, fleet_service, notifier, billing_service)

        # Seed demo (ca să ai date)
        Program._seed(client_service, fleet_service, driver_service, shipment_service)

        # Meniu
        while True:
            Program._menu()
            c = read_str("Alege: ")

            if c == "1":
                Program._clients(client_service)
            elif c == "2":
                Program._vehicles(fleet_service)
            elif c == "3":
                Program._drivers(driver_service)
            elif c == "4":
                Program._shipments(shipment_service)
            elif c == "5":
                Program._dispatch(dispatch_service)
            elif c == "6":
                Program._billing(billing_service)
            elif c == "0":
                print("La revedere!")
                break
            else:
                print("Opțiune invalidă.")

    @staticmethod
    def _seed(client_service, fleet_service, driver_service, shipment_service):
        # clienți
        client_service.create(Client(id=1, name="SRL Alfa", phone="+37360000001"))
        client_service.create(Client(id=2, name="SRL Beta", phone="+37360000002"))

        # vehicule
        fleet_service.add_vehicle(Truck(id=1, plate="TR-101", capacity_kg=12000))
        fleet_service.add_vehicle(Van(id=2, plate="VN-202", capacity_kg=3500))

        # șoferi
        driver_service.create(Driver(id=1, name="Ion Popescu", license_no="MD-DR-1001", vehicle_id=1))
        driver_service.create(Driver(id=2, name="Maria Rusu", license_no="MD-DR-2001", vehicle_id=2))

        # shipments
        shipment_service.create(Shipment(id=1, client_id=1, destination="Chișinău", weight_kg=2500))
        shipment_service.create(Shipment(id=2, client_id=2, destination="Bălți", weight_kg=8000))

    @staticmethod
    def _menu():
        print("""
==================== LOGISTICS DISPATCH ====================
1) Clienți
2) Vehicule
3) Șoferi
4) Shipments (comenzi transport)
5) Dispatch
6) Billing (facturi/plăți)
0) Ieșire
============================================================
""")

    @staticmethod
    def _clients(svc):
        print("""
--- Clienți ---
1) Afișează
2) Adaugă
3) Șterge
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            for x in svc.list_all():
                print(" -", x)
        elif c == "2":
            cid = read_int("Client ID: ")
            name = read_str("Nume: ")
            phone = read_str("Telefon: ")
            svc.create(Client(id=cid, name=name, phone=phone))
            print("✅ Client adăugat.")
        elif c == "3":
            cid = read_int("Client ID: ")
            print("✅ Șters." if svc.delete(cid) else "❌ Nu există.")
        elif c == "0":
            return

    @staticmethod
    def _vehicles(svc):
        print("""
--- Vehicule ---
1) Afișează
2) Adaugă Truck
3) Adaugă Van
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            for v in svc.list_all():
                print(" -", v)
        elif c in ("2","3"):
            vid = read_int("Vehicle ID: ")
            plate = read_str("Placă: ")
            cap = read_float("Capacitate (kg): ")
            v = Truck(id=vid, plate=plate, capacity_kg=cap) if c == "2" else Van(id=vid, plate=plate, capacity_kg=cap)
            svc.add_vehicle(v)
            print("✅ Vehicul adăugat.")
        elif c == "0":
            return

    @staticmethod
    def _drivers(svc):
        print("""
--- Șoferi ---
1) Afișează
2) Adaugă
3) Asignează vehicul
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            for d in svc.list_all():
                print(" -", d)
        elif c == "2":
            did = read_int("Driver ID: ")
            name = read_str("Nume: ")
            lic = read_str("Nr permis: ")
            vid = read_int("Vehicle ID (0 dacă nu are): ")
            vehicle_id = vid if vid != 0 else None
            svc.create(Driver(id=did, name=name, license_no=lic, vehicle_id=vehicle_id))
            print("✅ Șofer adăugat.")
        elif c == "3":
            did = read_int("Driver ID: ")
            vid = read_int("Vehicle ID: ")
            print("✅ Asignat." if svc.assign_vehicle(did, vid) else "❌ Nu s-a putut asigna.")
        elif c == "0":
            return

    @staticmethod
    def _shipments(svc):
        print("""
--- Shipments ---
1) Afișează
2) Adaugă
3) Detalii (by id)
4) Șterge
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            for s in svc.list_all():
                print(" -", s)
        elif c == "2":
            sid = read_int("Shipment ID: ")
            cid = read_int("Client ID: ")
            dest = read_str("Destinație: ")
            w = read_float("Greutate (kg): ")
            svc.create(Shipment(id=sid, client_id=cid, destination=dest, weight_kg=w))
            print("✅ Shipment adăugat.")
        elif c == "3":
            sid = read_int("Shipment ID: ")
            s = svc.get(sid)
            print(s if s else "❌ Not found.")
        elif c == "4":
            sid = read_int("Shipment ID: ")
            print("✅ Șters." if svc.delete(sid) else "❌ Nu există.")
        elif c == "0":
            return

    @staticmethod
    def _dispatch(svc):
        print("""
--- Dispatch ---
1) Dispatch shipment (auto-assign)
2) Cancel shipment
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            sid = read_int("Shipment ID: ")
            print("✅ Dispatch finalizat." if svc.assign_and_dispatch(sid) else "❌ Dispatch eșuat.")
        elif c == "2":
            sid = read_int("Shipment ID: ")
            print("✅ Anulat." if svc.cancel(sid) else "❌ Nu s-a putut anula.")
        elif c == "0":
            return

    @staticmethod
    def _billing(svc):
        print("""
--- Billing ---
1) Afișează facturi
2) Afișează plăți
3) Plătește factură
0) Înapoi
""")
        c = read_str("Alege: ")
        if c == "1":
            for inv in svc.list_invoices():
                print(" -", inv)
        elif c == "2":
            for p in svc.list_payments():
                print(" -", p)
        elif c == "3":
            iid = read_int("Invoice ID: ")
            method = read_str("Metodă (Cash/Card): ")
            print("✅ Plătit." if svc.pay_invoice(iid, method=method) else "❌ Invoice not found.")
        elif c == "0":
            return


if __name__ == "__main__":
    Program.main()
