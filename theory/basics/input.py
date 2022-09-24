#every input is by default treated as a string
#we need to mention before the input if we want some specific data type

# name=input("enter your name\n")
# age=int(input("enter your age\n"))
# print(name,age)

hobbies=['music','coding','cricket','blogging']
print(hobbies)
print(hobbies[1:])
print(hobbies[1:3])
print(type(hobbies))

print(hobbies[-2]) #to access from back side
print(len(hobbies))
print(type(hobbies[1]))

tech=list(('saurabh','12',True))
print(tech)
print(type(tech[1]))

list1=[1,2,3]
list2=["hello",'hi','how are you']
list1.extend(list2)
list1.append(5)
list1.insert(2,'saurabh kumar')
list1.remove(3)
print(list2)
list2.clear();
print(list2)
print(list1)
print(list1.index('saurabh'))

list3=[1,45,33,21,6]
list3.sort()
print(list3)
list3.reverse()
print(list3)
list4=list3.copy()
list4.pop()
del list4[1]
print(list4)