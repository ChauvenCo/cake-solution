from abc import ABC, abstractmethod

class Beverage():
    def getPrice(self):
        return self.price

class Expresso(Beverage):
    def __init__(self):
        self.price = 2.0

class Capucino(Beverage):
    def __init__(self):
        self.price = 9.0

#-----------------------------------------------------------------------------------------

class Ingredient(Beverage):
    def __init__(self, something: Beverage):
        self.price += something.getPrice()

    def cost(self):
        print("Prix : ", self.price, " €")

class Milk(Ingredient):
    def __init__(self, something: Beverage):
        self.price = 0.5
        super().__init__(something)

class Sugar(Ingredient):
    def __init__(self, something: Beverage):
        self.price = 0.3
        super().__init__(something)