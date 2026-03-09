#code 1 , using for loop
'''n1=int(input("num1:\n"))
n2=int(input("num2:\n"))

for i in range(n1,n2+1):
    if i%2==0:
        print("even no: ", i)
    else:1
        print("odd no: ", i)'''

#code 2 , using while loop
n1=int(input("num1:\n"))
n2=int(input("num2:\n"))

while n1<=n2 :
    if n1%2==0:
        print("even no: ", n1)
    else:
        print("odd no: ", n1)
    n1+=1

#for right triangular code
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print('*', end=" ")
    print('\n')
