from patterns.factory_method import TruckFactory, VanFactory, ReeferTruckFactory
from patterns.abstract_factory import LocalCarrierFactory, InternationalCarrierFactory
from domain.shipment import Shipment
from cli.io_utils import read_int, read_float, read_str

def _print_menu():
    print("""
================== LAB 2 – LOGISTICS DISPATCH ==================
1) Factory Method: creează vehicul
2) Abstract Factory: toolkit carrier (pricing + tracking + docs)
3) Demo complet: creează shipment + calculează cost + tracking + documente
0) Ieșire
===============================================================
""")

def run_app():
    while True:
        _print_menu()
        choice = read_str("Alege opțiunea: ")

        if choice == "1":
            _menu_factory_method()
        elif choice == "2":
            _menu_abstract_factory()
        elif choice == "3":
            _menu_full_demo()
        elif choice == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.")

def _menu_factory_method():
    print("""
--- Factory Method (Vehicule) ---
1) Truck
2) Van
3) ReeferTruck (frig)
0) Înapoi
""")
    c = read_str("Alege: ")
    vid = read_int("Vehicle ID: ")
    plate = read_str("Placă: ")
    cap = read_float("Capacitate (kg): ")

    if c == "1":
        factory = TruckFactory()
    elif c == "2":
        factory = VanFactory()
    elif c == "3":
        factory = ReeferTruckFactory()
    elif c == "0":
        return
    else:
        print("Tip invalid.")
        return

    vehicle = factory.create_vehicle(vehicle_id=vid, plate=plate, capacity_kg=cap)
    print("✅ Creat:", vehicle)

def _menu_abstract_factory():
    print("""
--- Abstract Factory (Carrier Toolkit) ---
1) LocalCarrier (MD)
2) InternationalCarrier (EU/INTL)
0) Înapoi
""")
    c = read_str("Alege: ")
    if c == "1":
        factory = LocalCarrierFactory()
    elif c == "2":
        factory = InternationalCarrierFactory()
    elif c == "0":
        return
    else:
        print("Opțiune invalidă.")
        return

    pricing = factory.create_pricing_service()
    tracking = factory.create_tracking_service()
    docs = factory.create_document_service()

    print("✅ Toolkit creat:")
    print(" - pricing:", pricing.__class__.__name__)
    print(" - tracking:", tracking.__class__.__name__)
    print(" - docs:", docs.__class__.__name__)

    code = read_str("Tracking code (ex: TRK-001): ")
    print("Status:", tracking.get_status(code))

def _menu_full_demo():
    print("""
--- Demo complet (Shipment + Carrier Toolkit) ---
Alege carrier:
1) LocalCarrier
2) InternationalCarrier
""")
    c = read_str("Alege: ")
    factory = LocalCarrierFactory() if c == "1" else InternationalCarrierFactory()

    shipment_id = read_int("Shipment ID: ")
    destination = read_str("Destinație: ")
    weight = read_float("Greutate (kg): ")
    distance = read_float("Distanță (km): ")
    tracking_code = read_str("Tracking code: ")

    shipment = Shipment(id=shipment_id, destination=destination, weight_kg=weight, distance_km=distance, tracking_code=tracking_code)

    pricing = factory.create_pricing_service()
    tracking = factory.create_tracking_service()
    docs = factory.create_document_service()

    cost = pricing.calculate_cost(shipment)
    status = tracking.get_status(shipment.tracking_code)
    awb = docs.generate_awb(shipment)
    invoice = docs.generate_invoice(shipment, amount=cost)
    label = docs.generate_label(shipment)

    print("\n✅ Shipment creat:", shipment)
    print("Cost estimat:", f"{cost:.2f}")
    print("Tracking:", status)
    print("\n--- Documente ---")
    print(awb)
    print(invoice)
    print(label)
