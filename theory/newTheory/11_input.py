num = input('Enter a number: ')#inputted value is always a string
print(num)
print(type(num))
num=int(num)
print(type(num))
# error-->>  print(int('2+3'))
print(eval('2+3'))