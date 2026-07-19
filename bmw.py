from abc import ABC, abstractmethod

# Abstract Class
class Car(ABC):

    @abstractmethod
    def brand(self):
        pass

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def features(self):
        pass


# BMW Class
class BMW(Car):

    def brand(self):
        print("Car Brand : BMW")

    def speed(self):
        print("Top Speed : 250 km/h")

    def fuel_type(self):
        print("Fuel Type : Petrol")

    def features(self):
        print("Features : Sunroof, ABS, Airbags, Navigation System")


# Ferrari Class
class Ferrari(Car):

    def brand(self):
        print("Car Brand : Ferrari")

    def speed(self):
        print("Top Speed : 340 km/h")

    def fuel_type(self):
        print("Fuel Type : Petrol")

    def features(self):
        print("Features : Sports Mode, Carbon Fiber Body, Launch Control")


# Function to demonstrate Polymorphism
def car_details(car):
    car.brand()
    car.speed()
    car.fuel_type()
    car.features()
    print("-" * 40)


# Create Objects
bmw = BMW()
ferrari = Ferrari()

# Store objects in a list
cars = [bmw, ferrari]

# Polymorphism
for car in cars:
    car_details(car)