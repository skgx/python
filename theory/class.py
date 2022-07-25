class Dog:

    def __init__(self,name,age):
        #way of making attributes of the class
        self.name=name
        self.age=age
        print(name) 
    def add_1(self,x):
        return x+1

    def bark(self):
        print("bark")
    
    def get_age(self):
        return self.age

d=Dog("tim",34) #this line will call the init method and pass the parameter to it
d.bark()
print(d.get_age())
print(type(d))
print(d.add_1(5))
