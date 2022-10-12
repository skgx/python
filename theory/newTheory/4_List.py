"""everything is an object in Python programming, 
data types are actually classes and variables are instance (object)
 of these classes."""

"""Integers can be of any length, it is only limited by the memory available.
A floating-point number is accurate up to 15 decimal places"""
#numbers
a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
#isinstance functions returns true if the passed variable is of given class
print()

#LIST
"""List is an ordered sequence of items. It is one of the most used datatype
 in Python and is very flexible.
 All the items in a list do not need to be of the same type."""
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3]) #0th index included but 3rd index not included

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#Lists are mutable, meaning, the value of elements of a list can be altered.
a = [1, 2, 3]
a[2] = 4
print(a)
print()


