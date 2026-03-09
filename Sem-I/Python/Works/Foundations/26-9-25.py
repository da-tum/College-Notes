
def my_name():
    '''Returns Your name.'''
    return "Your Name"
print(my_name())
# Replace "Your Name" with your actual name.
print(my_name.__doc__)


# *Args

def my_fun(*args):
    return sum(args)
print(my_fun(1,2,3,4,5))  # Output: 15
print(my_fun(10,20))      # Output: 30
print(my_fun())           # Output: 0
print(my_fun(5,10,15,20,25,30))  # Output: 105

# *Kwargs
def my_fun2(**kwargs):
    return kwargs
print(my_fun2(name="Alice", age=30))  # Output: {'name': 'Alice', 'age': 30}
print(my_fun2(city="New York"))        # Output: {'city': 'New York
print(my_fun2())                       # Output: {}
print(my_fun2(country="USA", profession="Engineer", hobby="Reading"))  # Output: {'country': 'USA', 'profession': 'Engineer', 'hobby': 'Reading'}
# Replace "Your Name" with your actual name.
