class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name

    def welcome_customers(self):
        print(f"Welcome to {self.shop_name} phone shop!")
class Store(Shop):
    def __init__(self, shop_name, store_name):
        super().__init__(shop_name)
        self.store_name = store_name

    def display_store_info(self):
        print(f"This is {self.store_name} at {self.shop_name} phone shop.")
class Employee(Store):
    def __init__(self, shop_name, store_name, employee_name):
        super().__init__(shop_name, store_name)
        self.employee_name = employee_name

    def greet_customer(self):
        print(f"Hello, I am {self.employee_name}. How can I assist you today?")
phone_shop = Shop("TechGadgets")
store = Store("TechGadgets", "Main Store")
employee = Employee("TechGadgets", "Main Store", "Mohan")
phone_shop.welcome_customers()
store.display_store_info()
employee.greet_customer()

