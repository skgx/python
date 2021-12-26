from math import *   #this lines imports all the functions of math class

name='saurabh'
age=19
print("hello I am 7",100)
print(name+' is nice and'+' his age is ',age) #conactenating string with int gives error so we use , 

print('hi\nhow are you')

print('welcome \"Saurabh\"') #to print special charcters it has to be followed by a \ backslash

print(name.upper()) #converts to uppercase

print(len(name)) #gives length of string

print(name.isupper()) #checks if whole string is uppercase

print(name.index('u')) #prints the index of passed character

print(name.replace('a','z')) #replaces all occurences with given character

num=35
num2=str(num)
#print('hi'+num) this gives error becuse we can't catenate string with int
print('hi '+num2)

print(max(2,12,1,34)) #max of all numbers
print(round(3.5))

print(bin(3)) #print binary string of the number