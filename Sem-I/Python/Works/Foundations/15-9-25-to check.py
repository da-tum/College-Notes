n1 = int(input("num1:\n"))
n2 = int(input("num2:\n"))

'''while n1<=n2 :
    if n1%2==0:
        print("even no: ", n1)
    else:
        print("odd no: ", n1)
    n1+=1
'''
# Ensure the loop runs from the smaller number to the larger number
if n1 > n2:
    n1, n2 = n2, n1

while n1 < n2:
    if n2 % 2 == 0:
        print("even no: ", n1)
    else:
        print("odd no: ", n1)
    n2-=1
'''
if n1>n2: 1
    n3=n1
else:
    n3=n2
while n3!=0 :
    if n3%2==0:
        print("even no: ", n1)
    else:
        print("odd no: ", n1)
    n3+=1
'''