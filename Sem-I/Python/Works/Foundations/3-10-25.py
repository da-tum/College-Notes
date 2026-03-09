'''
def factor(a):
    l=[]
    for i in range(1,a+1):
        if a%i==0:
            l.append(i)
            print(l)
        print(l)
    return l

factor(100)
'''

def armstrong(a):
    a=str(a)
    l=list(a)
    sum=0
    print(l)
    for i in l :
        print(int(i))
        sum+=(int(i))**len(l)
    print(sum)
armstrong(253)
