x = "global"

def foo():
    x = x * 2
    print(x)
# foo()
"""The output shows an error because Python treats x as a 
local variable and x is also not defined inside foo()."""

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
print()
x = 5

def foo1():
    x = 10
    print("local x:", x)


foo1()
print("global x:", x)

print()
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
print()
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)