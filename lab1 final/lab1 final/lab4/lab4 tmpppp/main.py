from patterns.adapter import OldCarrierApi, OldCarrierAdapter, TrackingProvider
from patterns.composite import ShipmentLeaf, ShipmentGroup
from patterns.facade import DispatchFacade

SESSION_HISTORY = []


def log_action(text: str) -> None:
    SESSION_HISTORY.append(text)


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("⚠️ Introdu un număr întreg.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("⚠️ Introdu un număr valid.")


def read_str(prompt: str) -> str:
    return input(prompt).strip()


def pause():
    input("\nApasă Enter pentru a continua...")


def title():
    print("\n" + "=" * 72)
    print("        LAB 4 - LOGISTICS DISPATCH (Adapter / Composite / Facade)")
    print("=" * 72)


def menu():
    print("""
1) Adapter - verifică tracking prin API adaptat
2) Composite - calculează costul total al unui grup de shipments
3) Facade - rezervare + dispatch simplificat
4) Demo complet
5) Exemple presetate
6) Istoric sesiune
0) Ieșire
""")


def adapter_demo():
    print("\n--- Adapter ---")
    print("Adapter transformă un API vechi într-o interfață modernă și ușor de folosit.")
    code = read_str("Tracking code: ")
    provider: TrackingProvider = OldCarrierAdapter(OldCarrierApi())
    status = provider.get_status(code)
    print("\n✅ Rezultat tracking:")
    print(status)
    log_action(f"Adapter -> tracking {code}")
    pause()


def composite_demo():
    print("\n--- Composite ---")
    print("Composite tratează un shipment simplu și un grup de shipments în același mod.")
    group_name = read_str("Numele grupului: ")
    group = ShipmentGroup(group_name)

    count = read_int("Câte shipment-uri vrei să adaugi? ")
    for i in range(1, count + 1):
        print(f"\nShipment {i}:")
        code = read_str("  Cod: ")
        weight = read_float("  Greutate (kg): ")
        price_per_kg = read_float("  Preț per kg: ")
        group.add(ShipmentLeaf(code, weight_kg=weight, price_per_kg=price_per_kg))

    print(f"\n✅ Grup creat: {group.name()}")
    print(f"Cost total: {group.total_cost():.2f}")
    log_action(f"Composite -> group {group_name} total={group.total_cost():.2f}")
    pause()


def facade_demo():
    print("\n--- Facade ---")
    print("Facade oferă o singură metodă simplă pentru mai multe subsisteme.")
    client = read_str("Client: ")
    destination = read_str("Destinație: ")
    weight = read_float("Greutate (kg): ")
    tracking_code = read_str("Tracking code: ")

    facade = DispatchFacade()
    result = facade.book_and_dispatch(client=client, destination=destination, weight_kg=weight, tracking_code=tracking_code)

    print("\n✅ Rezultat complet:")
    print(f"Shipment code: {result.shipment_code}")
    print(f"Status: {result.status}")
    print(f"Cost estimat: {result.estimated_cost:.2f}")
    log_action(f"Facade -> book_and_dispatch {tracking_code}")
    pause()


def preset_examples():
    print("\n--- Exemple presetate ---")

    print("\n[Adapter]")
    provider: TrackingProvider = OldCarrierAdapter(OldCarrierApi())
    print(provider.get_status("TRK-001"))

    print("\n[Composite]")
    group = ShipmentGroup("Preset-Group")
    group.add(ShipmentLeaf("S1", 500, 2.5))
    group.add(ShipmentLeaf("S2", 1200, 2.5))
    print("Nume grup:", group.name())
    print("Cost total:", group.total_cost())

    print("\n[Facade]")
    facade = DispatchFacade()
    result = facade.book_and_dispatch("SRL Alfa", "Chișinău", 900, "TRK-009")
    print(result)

    log_action("Exemple presetate afișate")
    pause()


def full_demo():
    print("\n================ DEMO COMPLET ================")

    print("\n[Adapter]")
    provider: TrackingProvider = OldCarrierAdapter(OldCarrierApi())
    print(provider.get_status("TRK-123"))

    print("\n[Composite]")
    group = ShipmentGroup("Demo-Group")
    group.add(ShipmentLeaf("S-100", 300, 2.5))
    group.add(ShipmentLeaf("S-200", 700, 2.5))
    print("Total group cost:", group.total_cost())

    print("\n[Facade]")
    facade = DispatchFacade()
    result = facade.book_and_dispatch("SRL Beta", "Bălți", 1000, "TRK-999")
    print(result)

    print("==============================================")
    log_action("Demo complet executat")
    pause()


def history():
    print("\n--- Istoric sesiune ---")
    if not SESSION_HISTORY:
        print("Nu există acțiuni încă.")
    else:
        for idx, item in enumerate(SESSION_HISTORY, start=1):
            print(f"{idx}. {item}")
    pause()


def main():
    while True:
        title()
        menu()
        choice = read_str("Alege opțiunea: ")

        if choice == "1":
            adapter_demo()
        elif choice == "2":
            composite_demo()
        elif choice == "3":
            facade_demo()
        elif choice == "4":
            full_demo()
        elif choice == "5":
            preset_examples()
        elif choice == "6":
            history()
        elif choice == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.")


if __name__ == "__main__":
    main()
