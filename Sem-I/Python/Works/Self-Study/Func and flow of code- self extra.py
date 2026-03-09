a=1
def f():
    print("f():", a)

def g():
    a=2
    print("g():", a)
def h():
    global a
    a=3
    print("h():", a)
print("global():", a)
b=f()
print(b)
g()
h()
print("afterh():", a)