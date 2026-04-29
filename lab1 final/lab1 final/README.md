
# LogisticsDispatch (Lab 1) – Structură ca la exemplul colegului (Domain / Infrastructure / Services) – Python

Tema: sisteme de gestionare a unei companii de logistică / dispatch.

## Structură (inspirată din exemplul colegului)
- `LogisticsDispatch/Domain/Entities` – entități (OOP)
- `LogisticsDispatch/Infrastructure/Repositories` – repository in-memory (DIP)
- `LogisticsDispatch/Services` – servicii business (SRP)
- `Program.py` – punct de intrare (ca Program.cs)

## Rulare
```bash
python main.py
```

## Funcționalități
- CRUD: clienți, vehicule, șoferi, shipments (comenzi transport)
- Dispatch: alocare automată vehicul + șofer + livrare (polimorfism)
- Billing: generare factură + plată (opțional)
- Notificări (Email) – ușor extensibil (OCP)
