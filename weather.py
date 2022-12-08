from abc import ABC, abstractmethod

class AbstractDisplay(ABC):
    @abstractmethod
    def update(self, temp, hum, press):
        pass

class Display(AbstractDisplay):
    def update(self, temp, hum, press):
        print("Affichage des infos : " + str(temp) + '°C ' + str(hum) + '% ' + str(press) + 'bars')

class StatsDisplay(AbstractDisplay):
    def update(self, temp, hum, press):
        print("Affichage des stats : " + str(temp+276) + '°K ' + str(hum) + '% ' + str(press*10000) + 'Pa')

class WeatherData:
    def __init__(self):
        self.displays = []

    def getTemperature(self):
        return 20

    def getHumidity(self):
        return 10

    def getPressure(self):
        return 1

    def measurementChanged(self):
        for display in self.displays:
            display.update(self.getTemperature(), self.getHumidity(), self.getPressure())

    def append(self, display: AbstractDisplay):
        self.displays.append(display)

    def pop(self, index: int):
        self.displays.pop(index)
