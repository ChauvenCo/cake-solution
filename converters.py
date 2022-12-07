from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, from_currency, to_currency, amount):
        pass

class FXConverter(Converter):
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2
