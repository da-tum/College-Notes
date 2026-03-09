
d={"hello":1 , "hi": 2 ,"Nihao": 3, "Hao":4}
print(type(d))
a=d.items()
print(a)
for i in (d):
    print(i,"is key and is value")

d["hello"]=69


#to hikno of updating the dict using loop the value.
for i in d:
    l=list(i)
    j=5
    l[0]=5
print (d)

del d['Hao']
print(d)

print(d.pop("hello"))