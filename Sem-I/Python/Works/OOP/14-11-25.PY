#ACCESS MODIFIERS 
'''
class tryi:
    def __init__ (self,trymessage):
        self.trymessage=trymessage
    def _message():
        print("the message is", end=" ", self.trymessage)
    

class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name         
        self.__roll = roll          
        self.__branch = branch     

    def __displayDetails(self):     
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()    


obj = Geek("R2J", 1706256, "CSE")

obj.accessPrivateFunction()


class student(Geek):
    pass

obj2=student("R2J", 1706256, "CSE")
obj2.accessPrivateFunction()  
obj2.__displayDetails()  #AttributeError: 'student' object has no attribute '__displayDetails'  
'''

class Student:
    def __init__(self, name, roll, branch):
        self._name = name            
        self._roll = roll           
        self._branch = branch       

    def _displayRollAndBranch(self): 
        print("Roll:", self._roll)
        print("Branch:", self._branch)


class Geek(Student):
    def displayDetails(self):
        print("Name:", self._name)  
        self._displayRollAndBranch() 




class user(Geek):
    pass
obj2=user("R2J", 1706256, "CSE")
obj2.displayDetails()
print(end="\n")
obj2._displayRollAndBranch()
