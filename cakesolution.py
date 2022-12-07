from abc import ABC, abstractmethod

def solution(cake):
    return max([cake.count(cake[:index]) if cake.count(cake[:index]) > 1 and len(cake.replace(cake[:index], '')) == 0 else 1 for index in range(len(cake))], default=1)

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Person(name=" + self.name + ")"

class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

class PersonXML(PersonStorage):
    @classmethod
    def save(self, person):
        print(f'Save the {person} to a XML file')

class PersonJSON(PersonStorage):
    @classmethod
    def save(self, person):
        print(f'Save the {person} to a JSON file')

class PersonDatabase(PersonStorage):
    @classmethod
    def save(self, person):
        print(f'Save the {person} to a Database')
