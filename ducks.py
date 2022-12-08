from abc import ABC, abstractmethod

class Flyable(ABC):
    def fly(self):
        pass

class Fly1(Flyable):
    def fly(self):
        print("bruh")

class Fly2(Flyable):
    def fly(self):
        print("zbeub")

class Duck(ABC):
    def __init__(self, flyingClass):
        self.flyingClass = flyingClass

    def fly(self):
        self.flyingClass.fly()

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        print("Quack.")

    def display(self):
        print("I'm a Mallard Duck, and I'm a duck.")

class RedheadDuck(Duck):
    def quack(self):
        print("Quack.")

    def display(self):
        print("I'm a Redhead Duck, and I'm possibly a duck.")

