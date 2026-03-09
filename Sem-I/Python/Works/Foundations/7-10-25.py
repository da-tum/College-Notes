#pattern making 
'''
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()

for i in range (1,n+1):

    for j in range(1,i):
        print(" ",end=" ")

    for k in range (2*(n-i)+1):
        print("*",end=" ")
    
    print()

a="*" * (2*n-1)
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in a:
        print(k,end=" ")
    a = a[2:]
    print()'''
    
    
# Reverse heart with shaft and big base (does not modify previous pattern)
def reverse_heart_with_shaft(n: int = 8):
    # n controls overall size. Recommended: 6–12
    if n < 4:
        n = 4

    total_width = 2 * n + 1

    # Top tip to mid (expanding triangle)
    for i in range(1, n + 1):
        spaces = (total_width - (2 * i - 1)) // 2
        print(" " * spaces + "*" * (2 * i - 1) + " " * spaces)

    # Lower lobes (two triangles growing outward)
    lobes_rows = max(2, n // 2)
    for i in range(lobes_rows):
        left_width = n - i
        gap = (2 * i + 1)
        right_width = n - i
        line = "*" * left_width + " " * gap + "*" * right_width
        # Center the lobe line to total_width
        pad = (total_width - len(line)) // 2
        print(" " * pad + line + " " * pad)

    # Shaft (centered)
    shaft_width = max(3, n // 3 | 1)  # odd width
    shaft_rows = n
    left_pad = (total_width - shaft_width) // 2
    for _ in range(shaft_rows):
        print(" " * left_pad + "*" * shaft_width + " " * left_pad)

    # Big base (wider than shaft)
    base_width = min(total_width, shaft_width + n + (n // 2))
    base_rows = max(2, n // 3)
    base_pad = (total_width - base_width) // 2
    for _ in range(base_rows):
        print(" " * base_pad + "*" * base_width + " " * base_pad)


# Run the new pattern
try:
    rows = int(input("Enter size for reverse heart (e.g., 8-12): ") or "8")
except ValueError:
    rows = 8
reverse_heart_with_shaft(rows)
