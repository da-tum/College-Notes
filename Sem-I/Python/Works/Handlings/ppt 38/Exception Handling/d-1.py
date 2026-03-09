
#Exception Handling in Python
'''
try:
    # risky code
except Exception as e:
    print("Error:", e)


'''
#Catches and handles unexpected runtime errors

'''
#Raising Custom Exceptions
try:
    #Risky Code Block
    result = 10 / 0  # This will raise a ZeroDivisionError
    print("Result:", result)
except Exception as e:
    print("Error: Division by zero is not allowed.")
    
'''
class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise NegativeAgeError("Custom Error: Age cannot be negative")
    else:
        print("Valid age:", age)


input_age = int(input("Enter your age: "))
check_age(input_age)
