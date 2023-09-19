# import functions
from utility import add, calculate  # similar to static import in java

add = add(10, 20)
print(add)

calc = calculate(10, 20, "*")
print(calc)

import utility

utility.add(5, 10)
utility.calculate(10, 2, "/")
utility.square(5)

print("================================================")
# we can give an alias to import to make it more readable
# defining alias name for module
import utility as util

util.add(12, 21)
util.calculate(12, 12, "+")
util.square(3)

print("================================================")
# defining alias name for functions
from utility import square as sq, add as a

sq(3)
a(10,10)

