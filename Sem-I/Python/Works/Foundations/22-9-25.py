
c=[]
b=[14,16,23.15,"hello",True,23.15,16 ,14,14,14]

for i in b:
    c.append(b.pop(0))
    print(b ,'is b')
print(c)
'''
#or

while len(b):
    c.append(b.pop())
    print(b ,'is b')
'''
print(c)

'''a=[]
b=[1,2,3,4,5,6,5]

a.append(14)
a.append(15)
print(a , 'is the list a')    

a.insert(1,20)
print(a , 'is the list a after insert')

a.remove(14)
print(a , 'is the list a after removal')
print(a.pop(), 'is the popped element')
print(a , 'is the list a after pop')

a.clear()
print(a , 'is the list a after clear')

a.extend(b)
print(a , 'is the list a after extend')

print(a.index(5), 'is the index of 5 in a')

print(a.count(5),'is the count of 5 in a')

a.sort()
print(a , 'is the list a after sort')

a.reverse()
print(a , 'is the list a after reverse')

c=a.copy()
print(c , 'is the copied list c from a')

del c[6]
print(c)

c.clear()
print(c , 'is the list c after clear')

print(a , 'is the list a after clearing c')
'''