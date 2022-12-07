import time
import progressbar as p
from cakesolution import *

if __name__ == '__main__':
    # for i in p.progressbar(range(5)):
    #     time.sleep(0.2)
    #
    # print(solution(''))

    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)