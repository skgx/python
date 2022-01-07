#In Python, value of an integer is not restricted 
# by the number of bits and can expand to the limit of the available memory 

print(100**100)

print("Python" , end = '@') 
print("GeeksforGeeks")

#example below shows implicit conversion
x = 10
print("x is of type:",type(x))
y = 10.6
print("y is of type:",type(y))
x = x + y
print(x)
print("x is of type:",type(x))

#explicit type casting
s = "10010"
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

'''ord() : This function is used to convert a character to integer.
   hex() : This function is to convert integer to hexadecimal string.
   oct() : This function is to convert integer to octal string.
'''