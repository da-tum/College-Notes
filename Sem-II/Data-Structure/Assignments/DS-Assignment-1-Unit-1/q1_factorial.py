"""
Q=1 Factorial Implementation (Recursive)

This script demonstrates two recursive approaches to calculate the factorial of a number:
1. Naive Recursion
2. Memoized Recursion (Optimized)
"""

import sys

# Increase recursion depth for larger calculations if needed
sys.setrecursionlimit(2000)

# --- 1. Naive Recursive Factorial ---
def factorial_naive(n):
    """
    Calculates factorial using standard recursion.
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial_naive(n - 1)


# --- 2. Memoized Recursive Factorial ---
factorial_cache = {0: 1, 1: 1}

def factorial_memoized(n):
    """
    Calculates factorial using recursion with memoization.
    Time Complexity: O(n) for the first call, O(1) for subsequent calls with same n.
    Space Complexity: O(n) for cache and recursion stack.
    """
    if n in factorial_cache:
        return factorial_cache[n]
    
    factorial_cache[n] = n * factorial_memoized(n - 1)
    return factorial_cache[n]


# --- Complexity Analysis & Justification ---
"""
JUSTIFICATION:

1. Time Complexity:
   - Both methods have O(n) time complexity for a single calculation because there are 'n' recursive calls.
   - However, Memoization is superior when multiple factorials are calculated in a single session, 
     as it avoids redundant computations by storing results in a cache.

2. Space Complexity:
   - Naive: O(n) due to the call stack depth. Each call remains on the stack until the base case is reached.
   - Memoized: O(n) for both the call stack and the dictionary storage.
"""

def main():
    test_val = 10
    print(f"--- Q=1 Factorial (n={test_val}) ---")
    print(f"Naive result: {factorial_naive(test_val)}")
    print(f"Memoized result: {factorial_memoized(test_val)}")
    print("Cache state after memoized call:", len(factorial_cache), "entries")

if __name__ == "__main__":
    main()
