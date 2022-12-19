import time
import progressbar as p
from cakesolution import *
from vehicles import *
from converters import *
from ducks import *
from weather import *
from StarBuzz import *

class App:
    def __init__(self, converter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

if __name__ == '__main__':
    # for i in p.progressbar(range(5)):
    #     time.sleep(0.2)
    #
    # print(solution(''))

    # person = Person('John Doe')
    # storage = PersonXML()
    # storage.save(person)

    # car = Car()
    # car.go()

    # converter = FXConverter()
    # app = App(converter)
    # app.start()

    # fly1 = Fly1()
    # duck = MallardDuck(fly1)
    # duck.display()
    # duck.fly()

    # screen = Display()
    # stats = StatsDisplay()
    #
    # datas = WeatherData()
    # datas.append(screen)
    # datas.append(stats)
    # datas.measurementChanged()

    cafe = Sugar(Milk(Expresso()))
    cafe.cost()