'''
1.4 Algorithm Execution Observation Table
You are building an algorithm performance analysis toolkit.
Given different input sizes, prepare an observation table for the algorithms implemented in this lab.
Instead of using actual execution time, use deterministic operation-count estimates so that the result can be checked by auto-evaluation.
For each input size n, calculate operation counts for:
Recursive Factorial
Iterative Factorial
Recursive Fibonacci
Iterative Fibonacci
Linear Search
Binary Search
Bubble Sort
Insertion Sort
Operation count rules:
Recursive Factorial count is n + 1.
Iterative Factorial count is n.
Recursive Fibonacci count is the number of recursive function calls required to compute Fibonacci.
Iterative Fibonacci count is n.
Linear Search count is n for worst-case search.
Binary Search count is floor(log2(n)) + 1.
Bubble Sort count is n * (n - 1) / 2.
Insertion Sort count is n * (n - 1) / 2.
The output must show a comparative observation table for all given input sizes.

Input Format
First line: An integer k representing the number of input sizes.
Second line: k space-separated integers representing input sizes.

Output Format
First print:
Algorithm Execution Observation Table
Then print the heading:
InputSize RecursiveFactorial IterativeFactorialRecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort
After that, print one row for each input size.

Constraints
1 <= k <= 20
1 <= n <= 30
All input sizes are positive integers.

Examples
Input
4
1 2 4 8

Output
Algorithm Execution Observation Table
InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort
1 2 1 1 1 1 1 0 0
2 3 2 3 2 2 2 1 1
4 5 4 9 4 4 3 6 6
8 9 8 67 8 8 4 28 28
'''

# Solution

import math
def generate_execution_observation_table(sizes):
    # Dictionary to speed up the Recursive Fibonacci count calculation
    memo = {0: 1, 1: 1}
    
    def get_fib_calls(n):
        if n not in memo:
            # The number of calls is the calls for (n-1) + calls for (n-2) + 1 (the current call)
            memo[n] = get_fib_calls(n - 1) + get_fib_calls(n - 2) + 1
        return memo[n]

    # Initialize the return list with the headers
    result = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]
    
    # Loop through every size in the dataset
    for n in sizes:
        # Calculate counts based exactly on the provided rules
        rec_fact = n + 1
        iter_fact = n
        rec_fib = get_fib_calls(n)
        iter_fib = n
        lin_search = n
        bin_search = math.floor(math.log2(n)) + 1
        
        # Use integer division (//) to avoid printing decimal points
        bub_sort = (n * (n - 1)) // 2 
        ins_sort = (n * (n - 1)) // 2
        
        # Format the row exactly as requested
        row = f"{n} {rec_fact} {iter_fact} {rec_fib} {iter_fib} {lin_search} {bin_search} {bub_sort} {ins_sort}"
        result.append(row)
        
    return result