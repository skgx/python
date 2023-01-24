def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("The factorial of", num, "is", factorial(num))
print(factorial.__doc__)
"""The Python interpreter limits the depths of recursion to 
help avoid infinite recursions, resulting in stack overflows.
By default, the maximum depth of recursion is 1000. If the 
limit is crossed, it results in RecursionError."""