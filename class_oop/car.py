

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
my_used_car = Car('lambo', 'caddy', 2000)
print(my_used_car.get_descriptive_name())

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(44)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)

my_used_car.update_odometer(45003)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()