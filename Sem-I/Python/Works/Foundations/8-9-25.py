''' make a program to take 2 variables from user and then perform an
arithmetic operation on it based on user choice'''

a=int(input('enter any number\n'))
b=int(input('enter any number\n'))

A=a+b
B=a-b
C=a*b
D=a/b

ch= (input('enter A,B,C,D to go for addition substraction multiplication and division\n'))
if ch=='A' or 'a':
    print('the addition is',A)
elif ch=='B' or 'b':
    print('the substraction is',B)
elif ch=='C' or 'c':
    print('the multiplication is',C)        
elif ch=='D' or 'd':  
    print('the division is',D)
else:
    print('invalid input')
