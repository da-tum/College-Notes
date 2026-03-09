c=[]
b=[14,16,23.15]
for i in range(len(b)):
    c.append(b.pop(0))
    print(b ,'is b')
print(c)


'''b=[14,16,23.15]
b.pop()
print(b)
print(b.count(14))
l=[1,3,4,5]
b.extend(l)
c=b.sort()
print(c)'''
'''
b.insert(1,20)
print(b)'''
#list
'''
b=[14,'16',"Hello",23.15]
del b[2]
b.remove(23.15)
b[1]=46.44
for i in b:
    print(i)
b.pop(0)
print(b)

#tuple
b=(14,16,"Hello",23.15)
#need to convert into list first then perform the operations.


#Dictionary
b={"Name":"Surname","Rollno":"240KRMU012","Course":"Btech" }
for i,j in b.items():
    print(f"key {i}, value{j}")
for i in b.values():
     print(f"value{i}")'''