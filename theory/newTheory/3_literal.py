a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 2+3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


print()
#string literal
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
#raw strings treat backslash as a string character only

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


print()
#boolean literals
x = (1 == True)
y = (1 == False)
a = True + 4 #True=1
b = False + 10 #False=0

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


print()
#special literals
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)



print()
#literal collection
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)


