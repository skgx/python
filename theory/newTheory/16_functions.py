def greet(name):
    """
    This function greets toṇ
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

greet('Paul') #this statement can only be written after function definition

def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")#if any 1 parameter passed is missing it will give error

print()
def greet1(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet1("Kate")
greet1("Bruce", "How do you do?")