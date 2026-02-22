"""
Q=4 Recursive Binary Search Implementation

This script demonstrates recursive binary search and provides a 
recurrence-based complexity explanation.
"""

def binary_search_recursive(arr, low, high, target):
    """
    Performs recursive binary search.
    arr: sorted list
    low: starting index
    high: ending index
    target: element to find
    Returns: index of target if found, else -1
    """
    if low <= high:
        mid = (low + high) // 2

        # Case 1: Target found at middle
        if arr[mid] == target:
            return mid

        # Case 2: Target is smaller than mid, search in left half
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)

        # Case 3: Target is larger than mid, search in right half
        else:
            return binary_search_recursive(arr, mid + 1, high, target)

    # Base case: Target not present
    return -1


# --- Recurrence-Based Complexity Explanation ---
"""
COMPLEXITY EXPLANATION:

1. Recurrence Relation:
   Binary Search divides the problem size by half in each step and performs a constant amount of work O(1) for comparisons.
   Recurrence: T(n) = T(n/2) + C

2. Using Master Theorem:
   General form: T(n) = a*T(n/b) + f(n)
   Here: a = 1, b = 2, f(n) = C = O(n^0)
   
   Calculate n^(log_b(a)):
   n^(log_2(1)) = n^0 = 1
   
   Since f(n) = O(n^(log_b(a))), Case 2 of Master Theorem applies.
   T(n) = Θ(n^(log_b(a)) * log_n) = Θ(1 * log_n) = O(log n)

3. Recursion Tree Method:
   - Level 0: n
   - Level 1: n/2
   - Level 2: n/4
   ...
   - Level k: n/2^k = 1 (Base case)
   - Taking log on both sides: k = log_2(n)
   Since work at each level is constant, Total Work = C * (Number of levels) = C * log_2(n).

RESULT:
- Time Complexity: O(log n)
- Space Complexity: O(log n) due to recursive call stack.
"""

def main():
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23
    
    print(f"--- Q=4 Recursive Binary Search ---")
    print(f"Array: {sorted_array}")
    print(f"Target: {target_val}")
    
    result = binary_search_recursive(sorted_array, 0, len(sorted_array) - 1, target_val)
    
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found in array.")

if __name__ == "__main__":
    main()
