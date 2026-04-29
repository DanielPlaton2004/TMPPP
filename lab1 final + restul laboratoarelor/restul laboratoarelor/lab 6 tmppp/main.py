from patterns.strategy import RoutePlanner, FastestRouteStrategy, CheapestRouteStrategy
from patterns.observer import ShipmentSubject, ConsoleObserver
from patterns.command import DispatchCommand, CancelCommand, CommandInvoker
from patterns.memento import ShipmentCaretaker
from patterns.iterator import ShipmentCollection

def main():
    print("=== Strategy ===")
    p = RoutePlanner(FastestRouteStrategy()); print(p.plan("A","B"))
    p.set_strategy(CheapestRouteStrategy()); print(p.plan("A","B"))

    print("\n=== Observer ===")
    s = ShipmentSubject("S-1"); s.attach(ConsoleObserver())
    s.set_status("IN_TRANSIT"); s.set_status("DELIVERED")

    print("\n=== Command + Memento + Iterator ===")
    col = ShipmentCollection(["S-1","S-2"])
    caretaker = ShipmentCaretaker(col)
    inv = CommandInvoker()
    inv.execute(DispatchCommand(col, "S-3"))
    inv.execute(CancelCommand(col, "S-1"))
    print("Now:", list(col.iterator()))
    inv.undo()
    print("After undo:", list(col.iterator()))
    caretaker.restore_initial()
    print("After restore:", list(col.iterator()))

if __name__ == "__main__":
    main()
