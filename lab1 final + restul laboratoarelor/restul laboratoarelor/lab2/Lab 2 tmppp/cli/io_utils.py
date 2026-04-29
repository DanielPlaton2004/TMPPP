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
