# Program to convert Infix expression to Postfix expression

# Function to define precedence of operators
def precedence(operator):
    # Higher value means higher precedence
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0  # For non-operators


# Function to convert infix to postfix
def infix_to_postfix(expression):
    
    stack = []      # Stack to store operators
    postfix = ""    # Output string for postfix expression

    # Loop through each character in input expression
    for char in expression:

        # If operand (letter or digit), add directly to postfix
        if char.isalnum():
            postfix += char

        # If opening bracket, push to stack
        elif char == '(':
            stack.append(char)

        # If closing bracket, pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '(' from stack

        # If operator
        else:
            # Pop operators from stack while they have higher or equal precedence
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    # Pop all remaining operators from stack
    while stack:
        postfix += stack.pop()

    return postfix


# Taking user input
expr = input("Enter infix expression: ")

# Remove spaces (optional)
expr = expr.replace(" ", "")

# Convert and print result
result = infix_to_postfix(expr)
print("Postfix Expression:", result)