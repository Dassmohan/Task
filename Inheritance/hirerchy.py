class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, frame_material):
        super().__init__(brand, model, year)
        self.frame_material = frame_material
    def display_info(self):
        super().display_info()
        print(f"Frame Material: {self.frame_material}")
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self.engine_type = engine_type
    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")
bicycle = Bicycle("Trek", "FX 2", 2022, "Aluminum")
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, "V-Twin")
print("Bicycle Information:")
bicycle.display_info()
print("\nMotorcycle Information:")
motorcycle.display_info()
