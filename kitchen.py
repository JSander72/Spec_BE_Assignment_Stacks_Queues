from order import Order 

class Kitchen:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, order):
        if self.tail is None:
            self.head = self.tail = order
            return
        self.tail.next = order
        self.tail = order

    def cook_order(self):
        if self.head is None:
            return None
        order = self.head
        self.head = order.next
        if self.head is None:
            self.tail = None
        return order

    def view_orders(self):
        if self.head is None:
            print("No orders in the kitchen!")
            return
        current_order = self.head
        while current_order:
            print(f"Table {current_order.table_number}: {', '.join(current_order.meals)}")
            current_order = current_order.next
