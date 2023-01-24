"""In Python, an anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword in Python
anonymous functions are defined using the lambda keyword."""

"""Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned.
 Lambda functions can be used wherever function objects are required."""

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))
print()
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
print()
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

