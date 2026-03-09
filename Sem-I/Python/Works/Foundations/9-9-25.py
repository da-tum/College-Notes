'''write a program to calculate the marks of subjects given below and assign grade 
accordingly 
a. python , maths , design thinking , compter fundamentas 
b. percentage >=90 - grade A '''

a=int(input('enter your marks in Python\n'))
b=int(input('enter your marks in Desgin thinking\n'))
c=int(input('enter your marks in Computer fundamentals\n'))
d=int(input('enter your marks in Maths\n'))

avg = (a+b+c+d)/4

if avg>=90:
    print('Grade A')
elif avg<=89 and avg>=81:
    print('Grade B')
elif avg<81 and avg>=71:
    print('Grade C')
elif avg>71 and avg>61:
    print('Grade D')
else:
    print('Out of Competition')

