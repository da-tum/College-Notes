# find the sum of all digits in a given number

n= str(input ('Enter A number'))
summ=0

# lis=n.split('')
# print(lis)

for i in range (len (str (n))):
    
    summ+= int(n)%10
    print(summ)
    n= int(n)/10

print ('Sum of digits:', summ)