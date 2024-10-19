from kitchen import Kitchen
from order import Order

if __name__ == "__main__":
    kitchen = Kitchen()
    order1 = Order(["Burger", "Fries"], 1)
    order2 = Order(["Pizza", "Salad"], 2)
    order3 = Order(["Pasta", "Garlic Bread"], 3)

    kitchen.add_order(order1)
    kitchen.add_order(order2)
    kitchen.add_order(order3)

    kitchen.view_orders()
    kitchen.cook_order()
    kitchen.view_orders()