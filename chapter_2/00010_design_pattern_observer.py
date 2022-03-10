from typing import List


class EventBus:
    def __init__(self):
        self.subscribers: dict = {}

    def subscribe(self, event_type: str, fn):
        if not event_type in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(fn)

    def post_event(self, event_type: str, data):
        if not event_type in self.subscribers:
            return

        list_of_subscribers: List = self.subscribers[event_type]
        for fn in list_of_subscribers:
            fn(data)


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"name = {self.name}, value = {self.value}"


class ShoppingCart:
    def __init__(self, event_bus: EventBus):
        self.items: List[Item] = []
        self.event_bus = event_bus

    def add_item(self, item: Item):
        self.items.append(item)
        self.event_bus.post_event("shopping_cart_item_added", item)

    def remove_item(self, item: Item):
        self.items.remove(item)
        self.event_bus.post_event("shopping_cart_item_removed", item)


class Summary:
    def __init__(self, event_bus: EventBus):
        self.summary: dict = {"items": [], "total": 0}
        self.event_bus = event_bus
        self.event_bus.subscribe(
            "shopping_cart_item_added", self.update_summary_add_item
        )
        self.event_bus.subscribe(
            "shopping_cart_item_removed", self.update_summary_remove_item
        )
        self.event_bus.subscribe("shopping_cart_item_added", self.update_summary_total)
        self.event_bus.subscribe(
            "shopping_cart_item_removed", self.update_summary_total
        )

    def update_summary_add_item(self, item: Item):
        self.summary["items"].append(item)

    def update_summary_remove_item(self, item: Item):
        self.summary["items"].remove(item)

    def update_summary_total(self, item: Item):
        self.summary["total"] = 0
        for item in self.summary["items"]:
            self.summary["total"] += item.value

        self.event_bus.post_event("price_updated", self.summary)


class CashierVisor:
    def __init__(self, event_bus: EventBus):
        self.msg = "Summary: "
        self.event_bus = event_bus
        self.event_bus.subscribe("price_updated", self.print)

    def print(self, total: int):
        print(self.msg + str(total))


event_bus: EventBus = EventBus()
shopping_cart: ShoppingCart = ShoppingCart(event_bus)
summary: Summary = Summary(event_bus)
cashier: CashierVisor = CashierVisor(event_bus)

item1: Item = Item("mickey", 10)
item2: Item = Item("hulk", 100)
item3: Item = Item("developer", 1)

shopping_cart.add_item(item1)
shopping_cart.add_item(item2)
shopping_cart.add_item(item3)
