"""
Q=2 Fibonacci Implementation (Recursive)

This script demonstrates two recursive approaches to find the N-th Fibonacci number:
1. Naive Recursion (Highly inefficient)
2. Memoized Recursion (Highly efficient)
"""

# --- 1. Naive Recursive Fibonacci ---
def fibonacci_naive(n):
    """
    Finds n-th Fibonacci number using standard recursion.
    Time Complexity: O(2^n) - Exponential growth.
    Space Complexity: O(n) for recursion stack.
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# --- 2. Memoized Recursive Fibonacci ---
fib_cache = {0: 0, 1: 1}

def fibonacci_memoized(n):
    """
    Finds n-th Fibonacci number using recursion with memoization.
    Time Complexity: O(n)
    Space Complexity: O(n) for cache and recursion stack.
    """
    if n in fib_cache:
        return fib_cache[n]
    
    fib_cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return fib_cache[n]


# --- Complexity Analysis & Justification ---
"""
WHY NAIVE FIBONACCI IS INEFFICIENT:

1. Redundant Computations:
   In the naive approach, the same subproblems are solved repeatedly. For example, to find fib(5),
   fib(3) is calculated twice, fib(2) is calculated three times, and so on.
   This leads to an exponential Time Complexity of O(φ^n) where φ is the golden ratio (approx 1.618),
   often simplified to O(2^n).

2. Growth of Recursive Calls:
   The number of calls grows extremely fast. For n=40, the naive method takes millions of calls,
   whereas the memoized method takes only 40 unique calls.

JUSTIFICATION FOR MEMOIZATION:

1. Time Complexity: O(n)
   - Every unique Fibonacci number from 0 to n is computed exactly once and stored.
   - Subsequent access to any stored value is O(1).

2. Space Complexity: O(n)
   - Store 'n' values in the cache dictionary.
   - Recursion stack goes 'n' levels deep.
"""

def main():
    test_val = 10
    print(f"--- Q=2 Fibonacci (n={test_val}) ---")
    print(f"Naive result: {fibonacci_naive(test_val)}")
    print(f"Memoized result: {fibonacci_memoized(test_val)}")
    print("For n=35, naive would be slow, but memoized is instant.")

if __name__ == "__main__":
    main()
