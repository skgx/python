import math
print(math.pi)

# import statement example
# to import standard module math

import math
print("The value of pi is", math.pi)

# import module by renaming it

import math as m
print("The value of pi is", m.pi)

# import only pi from math module

from math import pi
print("The value of pi is", pi)

# import all names from the standard module math

from math import *
print("The value of pi is", pi)

#We can use the reload() function inside the imp module to reload a module
""">>> import imp
>>> import my_module
This code got executed
>>> import my_module
>>> imp.reload(my_module)
This code got executed
<module 'my_module' from '.\\my_module.py'>"""

#We can use the dir() function to find out names that are defined inside a module.
"""We can use dir in example module in the following way:

>>> dir(example)"""


"""All the names defined in our current namespace can be found out using the dir() function without any arguments.

>>> a = 1
>>> b = "hello"
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']"""