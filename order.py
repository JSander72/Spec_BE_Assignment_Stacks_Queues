class Order:
    def __init__(self, meals, table_number):
        self.meals = meals
        self.table_number = table_number
        self.next = None