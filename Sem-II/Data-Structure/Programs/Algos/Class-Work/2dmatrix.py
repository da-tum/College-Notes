# Program to create and print a 2D array (matrix)

# Creating a 2D array (2 rows and 3 columns)
matrix = [
    [1, 2, 3],   # First row
    [4, 5, 6]    # Second row
]

# Printing entire matrix
print("Complete Matrix:")
print(matrix)

print("\nMatrix Elements Row by Row:")

# Loop through rows
for i in range(len(matrix)):
    
    # Loop through columns
    for j in range(len(matrix[i])):
        
        # Print each element with space
        print(matrix[i][j], end=" ")
    
    # Move to next line after each row
    print()


# Accessing specific element
print("\nAccess Specific Element:")
print("Element at row 1 column 2 is:", matrix[0][1])