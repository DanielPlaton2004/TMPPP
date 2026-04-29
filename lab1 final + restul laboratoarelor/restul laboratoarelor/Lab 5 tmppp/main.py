from patterns.flyweight import AddressFlyweightFactory
from patterns.decorator import EmailNotifier, SmsDecorator, PushDecorator
from patterns.bridge import DispatchReport, ConsoleRenderer, JsonRenderer
from patterns.proxy import DispatchService, DispatchServiceProxy

def main():
    print("=== Flyweight ===")
    f = AddressFlyweightFactory()
    a1 = f.get("MD","Chișinău","Stefan cel Mare 1")
    a2 = f.get("MD","Chișinău","Stefan cel Mare 1")
    print("same:", a1 is a2, "pool:", f.pool_size())

    print("\n=== Decorator ===")
    n = PushDecorator(SmsDecorator(EmailNotifier()))
    n.send("Shipment delivered!")

    print("\n=== Bridge ===")
    DispatchReport(ConsoleRenderer()).render({"shipments":2,"delivered":2})
    DispatchReport(JsonRenderer()).render({"shipments":3,"delivered":1})

    print("\n=== Proxy ===")
    real = DispatchService()
    print(DispatchServiceProxy(real, "dispatcher").dispatch("S-1"))
    print(DispatchServiceProxy(real, "guest").dispatch("S-2"))

if __name__ == "__main__":
    main()
