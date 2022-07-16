message="hello world"
print(message.find("world")) #6

message.replace('world','universe') #this does not change the original message
print(message) #this will print the original one only
message1=message.replace('world','universe')
print(message1) #this will print the changed array

greeting='hello '
mess='how are you'

message2='{},{}.welcome!'.format(greeting,mess) #{} are the placeholders for the variable
message3=f'{greeting},{mess.upper()}.Welcome!'# faster than .format method
print(message2)
print(message3)
print("HI")

print(dir(greeting)) #this will print the various methods that can be used for that variable

#print(help(str)) #tells everything that can be done in the string type values
print(help(str.lower))