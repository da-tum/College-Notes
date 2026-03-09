 
class var:
    x=5

o1=var()
print(o1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hello, my name is {self.name}"
    def welcome(self):
        message=self.greet()
        print("Welcome",message)
p1=person("John",36) #to create an object of class person to call it
print(p1.name)
print(p1.age)
p1.greet()
p1.welcome()