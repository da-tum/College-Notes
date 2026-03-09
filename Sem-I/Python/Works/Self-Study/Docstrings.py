'''Hello this is a Docstring example
comments are ignored , docstrings are not 
by changing docstring the output of the help program can be changed
it is used to document the dode 
by using __doc__ attribute we can access it .'''

#docstring written just below / above the function definition for it to be valid.

def square(n):
    '''This function returns the square of a number'''
    return n*n
print(square(5))
print(square.__doc__)
help(square)
print(help(square))
print(square.__doc__.split())
print(square.__doc__.split()[3])
print(len(square.__doc__.split()))
print(len(square.__doc__))
print(len(square.__doc__.split()[3]))
print(type(square.__doc__))

