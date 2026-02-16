#Initialization

class stack:
    def __init__(self,items=None):
        self.items = items if items is not None else []

    def isEmpty(self):
        return self.items == []
    
    def pop(self):
        if len(self.items)==0:
            return "UnderflowError"
        else:
            return self.items.pop()

    def peek(self):
        return ("top is :",self.items[-1])
    
    def display(self):
        return self.items

obj=stack()
obj.push(1)
value=obj.display()
print("Stack ",value)