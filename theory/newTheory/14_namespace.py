"""Everything in Python is an object. Name is a way to access the underlying object."""
#We can get the address (in RAM) of some object through the built-in function id().
# Note: You may get different values for the id
#Here, both refer to the same object 2, so they have the same id()

a = 2
print('id(2) =', id(2))
print('id(a) =', id(a))

# Note: You may get different values for the id
print()
a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))
print()
# Functions are objects too, so a name can refer to them as well.\
def printHello():
    print("Hello")
a = printHello

a()

#a namespace is a collection of names.
def outer_function():
    b = 20
    def inner_func():
        c = 30
a = 10
print()
def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)

print()
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)