pal=int(input("enter a number"))
def palindrome(a):
    b=str(a)
    if b==b[::-1]:
        print(a,"is a palindrome")
    else:
        print(a,"is not a palindrome")

palindrome(pal)

def palindrome1(a):
    b=str(a)
    c=list(b)
    for i in range (0,len(c)//2):
        if c[i]!=c[len(c)-1-i]:
            print(a,"is not a palindrome")
            break   
    else:
        print(a,"is a palindrome")
palindrome1(pal)

'''
pre=int(input("enter a number"))
def nonprime(a):
    if a>1:
        for i in range(2,int(a**0.5)):
            if (a%i)==0:
                print(a,"is not a prime number")
                break
        else:
            print(a,"is a prime number")
    else:
        print(a,"is not a prime number")

for i in range (pre):
    pre=pre-1
    nonprime(pre)
'''

'''fact=int(input("enter a number for factorial"))

def factorial(a):
    if a== 0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(fact))


if fact==1 or fact==0:
    print("factorial is 1")
else:
    factorial=1
    for i in range (1,(fact)+1):
        factorial=(factorial)*(i)
    print("factorial is",factorial)

'''
    
    