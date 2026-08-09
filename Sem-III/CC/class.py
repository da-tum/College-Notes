# WAP to find the sum of first N natural number

n = int (input("Enter a number: "))
sum=0

for i in range (0,n+1):
    sum+=i
print(sum,'Using for')

sum1 = 0
while n!=0:
    sum1 += n 
    n -= 1
print (sum1,'Using while')