#fibonnaci series
fib=int(input("enter a number for fibonacci series"))
def fib_series(a):

    if a<=0:
        print("invalid")
    elif a==1:
        print('1')
    else:
        lst=[0,1]
        n3=1
        count=0
        for i in range(2,a+1):
            while i>1:
                lst.append(i)
                lst[i]=lst[i-1]      
                
            print(lst) 
            count+=1
fib_series(fib)



#fibonnaci series
fib=int(input("enter a number for fibonacci series"))
def fib_series(a):
    n1,n2=0,1
    count=0
    if a<=0:
        print("enter a positive number")
    elif a==1:
        print("fibonacci series upto",a,":")
        print(n1)
    else:
        print("fibonacci series:")
        while count<a:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
fib_series(fib)