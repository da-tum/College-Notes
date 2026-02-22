"""
Q=3 Tower of Hanoi Implementation (Recursive)

This script implements the Tower of Hanoi algorithm and provides a systematic trace for N=3.
"""

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Recursive function to solve Tower of Hanoi puzzle.
    n: number of disks
    source: source rod
    destination: destination rod
    auxiliary: auxiliary rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Move the n-th disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# --- Systematic Trace for N=3 ---
"""
TRACE FOR N=3 (Source: A, Destination: C, Auxiliary: B):

hanoi(3, 'A', 'C', 'B'):
├── hanoi(2, 'A', 'B', 'C'):
│   ├── hanoi(1, 'A', 'C', 'B'):
│   │   └── Step 1: Move disk 1 from A to C
│   ├── Step 2: Move disk 2 from A to B
│   └── hanoi(1, 'C', 'B', 'A'):
│       └── Step 3: Move disk 1 from C to B
├── Step 4: Move disk 3 from A to C
└── hanoi(2, 'B', 'C', 'A'):
    ├── hanoi(1, 'B', 'A', 'C'):
    │   └── Step 5: Move disk 1 from B to A
    ├── Step 6: Move disk 2 from B to C
    └── hanoi(1, 'A', 'C', 'B'):
        └── Step 7: Move disk 1 from A to C

TOTAL STEPS: 7 (2^3 - 1)
"""

# --- Time Complexity Analysis ---
"""
TIME COMPLEXITY JUSTIFICATION:

1. Let T(n) be the number of moves for n disks.
2. The recurrence relation is: T(n) = 2*T(n - 1) + 1
3. Base case: T(1) = 1
4. Expanding the relation:
   T(n) = 2 [2*T(n-2) + 1] + 1 = 4*T(n-2) + 2 + 1
   T(n) = 8*T(n-3) + 4 + 2 + 1
   ...
   T(n) = 2^(n-1) * T(1) + 2^(n-2) + ... + 2^1 + 2^0
   T(n) = 2^(n-1) + 2^(n-2) + ... + 1
   This is a Geometric Progression with sum = 2^n - 1

Therefore, Time Complexity is O(2^n).
Space Complexity is O(n) due to the recursive call stack depth.
"""

def main():
    n = 3
    print(f"--- Q=3 Tower of Hanoi (n={n}) ---")
    tower_of_hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
