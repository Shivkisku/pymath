from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def accelerate(self, name):
        pass
    
    @abstractmethod
    def park(self, name):
        pass

class Bike(Vehicle):
    def accelerate(self, name):
        print(name, "is accelerating @ 60kmph")

    def park(self, name):
        print(name, "is parked at two-wheeler parking")

class Car(Vehicle):
    def accelerate(self, name):
        print(name, "is accelerating @ 90kmph")

    def park(self, name):
        print(name, "is parked at four-wheeler parking")

# Create instances and call methods
c = Car()
c.accelerate("Car")
c.park("Car")

b = Bike()
b.accelerate("Bike")
b.park("Bike")
