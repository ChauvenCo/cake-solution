from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class FlyingVehicle(Vehicle):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(FlyingVehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")