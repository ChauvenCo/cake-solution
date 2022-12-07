import time
import progressbar as p
from cakesolution import *

for i in p.progressbar(range(5)):
    time.sleep(0.2)

print(solution('abababa'))