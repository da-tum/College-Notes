#list comprehension 
lst = [(i, j, i * j) for i in range(1, 11) for j in range(1, 11)]
for i, j, product in lst:
    print(f'{i} * {j} = {product}')
print(lst)