"""In Python, we don't actually assign values to the variables.
 Instead, Python gives the reference of the object(value) to the variable."""

"""Python is a type-inferred language, so you don't have to explicitly
 define the variable type."""
a1=10
a1=10.1
print(a1)

print()
a, b, c = 5, 3.2, "Hello"
print (a)
print (b)
print (c)
print()


x = y = z = "same"
print (x)
print (y)
print (z)


"""A constant is a type of variable whose value cannot be changed.
 It is helpful to think of constants as containers
 that hold information which cannot be changed later."""

 #constants are conventionally written in uppercase
 #in python constant's value can be reassigned

PI=3.14
print(PI)