from patterns.builder import ShipmentDirector, StandardShipmentBuilder, ExpressShipmentBuilder
from patterns.prototype import ShipmentTemplate
from patterns.singleton import AppConfig

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
            print("Introduce un număr valid.")

def read_str(prompt: str) -> str:
    return input(prompt).strip()

def print_menu():
    print("""
==================== LAB 3 - LOGISTICS DISPATCH ====================
1) Builder - creează shipment standard
2) Builder - creează shipment express
3) Prototype - clonează un shipment template
4) Singleton - vezi / schimbă configurarea globală
5) Rulează demo complet
0) Ieșire
===================================================================
""")

def builder_standard():
    print("\n--- Builder: Shipment Standard ---")
    shipment_id = read_int("Shipment ID: ")
    destination = read_str("Destinație: ")
    weight = read_float("Greutate (kg): ")

    director = ShipmentDirector()
    builder = StandardShipmentBuilder()
    director.construct_standard(builder, shipment_id, destination, weight)
    shipment = builder.build()

    print("\n✅ Shipment standard creat:")
    print(shipment)
    print()

def builder_express():
    print("\n--- Builder: Shipment Express ---")
    shipment_id = read_int("Shipment ID: ")
    destination = read_str("Destinație: ")
    weight = read_float("Greutate (kg): ")

    director = ShipmentDirector()
    builder = ExpressShipmentBuilder()
    director.construct_express(builder, shipment_id, destination, weight)
    shipment = builder.build()

    print("\n✅ Shipment express creat:")
    print(shipment)
    print()

def prototype_demo():
    print("\n--- Prototype: clonare shipment template ---")
    destination = read_str("Destinația template: ")
    insurance = read_float("Valoare asigurare: ")
    template = ShipmentTemplate(destination=destination, fragile=True, insurance_value=insurance)

    shallow_id = read_int("ID pentru shallow clone: ")
    deep_id = read_int("ID pentru deep clone: ")

    shallow = template.clone_shallow(shallow_id)
    deep = template.clone_deep(deep_id)

    shallow.metadata["tags"].append("SHALLOW")
    deep.metadata["tags"].append("DEEP")

    print("\nTemplate original:")
    print(template)
    print("\nShallow clone:")
    print(shallow)
    print("\nDeep clone:")
    print(deep)
    print("\nObservație:")
    print("- shallow copy partajează metadata cu template-ul")
    print("- deep copy creează o copie separată a metadata")
    print()

def singleton_demo():
    print("\n--- Singleton: configurare globală ---")
    cfg = AppConfig.instance()

    while True:
        print("\nConfig curentă:")
        print(f"1) price_per_km = {cfg.get('price_per_km')}")
        print("2) Schimbă price_per_km")
        print("0) Înapoi")
        c = read_str("Alege: ")

        if c == "1":
            print(f"Valoare curentă: {cfg.get('price_per_km')}")
        elif c == "2":
            val = read_float("Noua valoare price_per_km: ")
            cfg.set("price_per_km", val)
            print("✅ Configurare actualizată.")
        elif c == "0":
            break
        else:
            print("Opțiune invalidă.")

def full_demo():
    print("\n================ DEMO COMPLET ================")

    director = ShipmentDirector()

    standard_builder = StandardShipmentBuilder()
    director.construct_standard(standard_builder, 1, "Chișinău", 1200)
    standard = standard_builder.build()

    express_builder = ExpressShipmentBuilder()
    director.construct_express(express_builder, 2, "Bălți", 800)
    express = express_builder.build()

    template = ShipmentTemplate(destination="Orhei", fragile=True, insurance_value=5000)
    shallow = template.clone_shallow(10)
    deep = template.clone_deep(11)

    shallow.metadata["tags"].append("SHALLOW")
    deep.metadata["tags"].append("DEEP")

    cfg1 = AppConfig.instance()
    cfg2 = AppConfig.instance()
    cfg1.set("price_per_km", 3.2)

    print("\n[Builder]")
    print("Standard:", standard)
    print("Express:", express)

    print("\n[Prototype]")
    print("Template:", template)
    print("Shallow:", shallow)
    print("Deep:", deep)

    print("\n[Singleton]")
    print("Same instance:", cfg1 is cfg2)
    print("price_per_km:", cfg2.get("price_per_km"))
    print("================================================\n")

def main():
    while True:
        print_menu()
        choice = read_str("Alege opțiunea: ")

        if choice == "1":
            builder_standard()
        elif choice == "2":
            builder_express()
        elif choice == "3":
            prototype_demo()
        elif choice == "4":
            singleton_demo()
        elif choice == "5":
            full_demo()
        elif choice == "0":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.\n")

if __name__ == "__main__":
    main()
