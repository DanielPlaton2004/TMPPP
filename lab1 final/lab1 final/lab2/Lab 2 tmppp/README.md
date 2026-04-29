# Laborator 2 – Factory Method & Abstract Factory (Logistics Dispatch)

Tema: sisteme de gestionare a unei companii de logistică / dispatch.

## Cerințe (conform laborator)
- Factory Method: creare obiecte fără a specifica clasa concretă direct (vehicule).
- Abstract Factory: creare *familii* de obiecte înrudite (toolkit de carrier: pricing + tracking + documente).
- Teste unitare pentru ambele paternuri.
- Demo interactiv (CLI).

## Rulare
```bash
python main.py
```

## Teste
```bash
python -m unittest -v
```

## Ce modelează proiectul
- **Factory Method**: `VehicleFactory` -> creează `Truck` / `Van` / `ReeferTruck`
- **Abstract Factory**: `CarrierToolkitFactory` -> creează:
  - `PricingService` (calcul cost)
  - `TrackingService` (status tracking)
  - `DocumentService` (AWB/Invoice/Label)
pentru 2 familii: `LocalCarrierFactory` și `InternationalCarrierFactory`.
