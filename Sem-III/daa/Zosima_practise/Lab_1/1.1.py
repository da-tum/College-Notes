'''
1.1 Recursive and Iterative Computation Analyzer
You are building an algorithm performance analysis toolkit.
For a given integer n, calculate factorial and Fibonacci using both 
recursive and iterative approaches.
The program must display four results:
Recursive factorial
Iterative factorial
Recursive Fibonacci
Iterative Fibonacci
For auto-evaluation, instead of actual execution time, the program must also 
display deterministic operation counts.
Operation count rules:
Recursive factorial count is n + 1.
Iterative factorial count is n.
Recursive Fibonacci count is the number of recursive function calls made while 
computing Fibonacci.
Iterative Fibonacci count is n.

Use the standard Fibonacci definition:
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)

Input Format
The platform wrapper reads one integer n and passes it as an argument to:
analyze_recursive_iterative(n)

Output Format
Return a list of strings in the following exact order:
Computation Analysis Report
Recursive Factorial: <value>
Iterative Factorial: <value>
Recursive Fibonacci: <value>
Iterative Fibonacci: <value>
Operation Count Comparison
Recursive Factorial Count: <count>
Iterative Factorial Count: <count>
Recursive Fibonacci Count: <count>
Iterative Fibonacci Count: <count>
Do not print these lines inside the function.

Constraints
0 <= n <= 20

Important Submission Instruction:
The platform wrapper will read the input value n and pass it to the function
analyze_recursive_iterative(n).
Do not use input() and do not print the output directly.
Complete only the given function and return the output as a list of strings.
The wrapper will print each returned line.

Examples
Input
5
Output
Computation Analysis Report
Recursive Factorial: 120
Iterative Factorial: 120
Recursive Fibonacci: 5
Iterative Fibonacci: 5
Operation Count Comparison
Recursive Factorial Count: 6
Iterative Factorial Count: 5
Recursive Fibonacci Count: 15
Iterative Fibonacci Count: 5
'''

# Solution

def analyze_recursive_iterative(n):
    # your code goes here
    global fib_count
    fib_count=0
    return [
            "Computation Analysis Report",
            f"Recursive Factorial: {recursive_factorial(n)}",
            f"Iterative Factorial: {iterative_factorial(n)}",
            f"Recursive Fibonacci: {recursive_fibonacci(n)}",
            f"Iterative Fibonacci: {iterative_fibonacci(n)}",
            "Operation Count Comparison",
            f"Recursive Factorial Count: {n+1}",
            f"Iterative Factorial Count: {n}",
            f"Recursive Fibonacci Count: {fib_count}", 
            f"Iterative Fibonacci Count: {n}"
        ]
  
def recursive_factorial(n):
    if n == 0:
      return 1
    elif n == 1:
      return 1
    else:
        return (n * recursive_factorial(n-1))

def iterative_factorial(n):
  prod=1
  for i in range (1, n+1):
    prod *= i
  return prod

fib_count=0
def recursive_fibonacci(n):
  global fib_count
  fib_count+=1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
  
def iterative_fibonacci(n):
  if n == 0:
    return 0
  else:
    a,b=0,1
    for i in range(1,n):
      a,b=b,a+b
    return b