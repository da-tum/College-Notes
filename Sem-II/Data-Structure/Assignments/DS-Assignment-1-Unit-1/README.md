# Data Structures - Unit 1 Assignment

*Submitted for College Evaluation.*

## Student Information

**Subject:** Data Structure's  
**Assignment:** Unit 1  
**Name:** Harsh Dev Jha  
**ID:** 2501010168  
**Section:** B.Tech CSE CORE SEC-A  
**Semester:** 2nd  
---

## Project Overview

This assignment covers fundamental concepts of recursion and searching. It includes implementations of classic mathematical problems and search algorithms, along with complete complexity analysis. Each solution is provided in Python, adhering to recommended academic practices.

---

## Question 1: Recursive Factorial
**File:** `q1_factorial.py`

The factorial of a non-negative integer $n$ is the product of all positive integers less than or equal to $n$. This implementation explores two recursive strategies: a naive approach and an optimized memoized version.
- **Naive Recursion:** Directly follows the mathematical definition $n! = n \times (n-1)!$.
- **Memoization:** Enhances efficiency by caching previously computed values, reducing redundant overhead for repeated calls.
- **Complexity:** Time $O(n)$, Space $O(n)$ due to the recursion stack.

---

## Question 2: Recursive Fibonacci
**File:** `q2_fibonacci.py`

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. This script highlights the drastic performance difference between standard recursion and memoization.
- **Efficiency Analysis:** The naive method calculates $O(2^n)$ branches, which becomes unusable for larger values of $n$.
- **Optimization:** Using a dictionary cache reduces the complexity to $O(n)$, making the calculation near-instantaneous even for $n=100$.
- **Complexity:** Naive $O(2^n)$, Memoized $O(n)$ time.

---

## Question 3: Tower of Hanoi
**File:** `q3_tower_of_hanoi.py`

The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of various sizes. The goal is to move the entire stack from the source rod to the destination rod, following specific rules (e.g., no larger disk on a smaller one).
- **Implementation:** The code uses a classic divide-and-conquer recursive strategy to find the optimal sequence of moves.
- **Analysis:** Includes a systematic trace of moves for $N=3$ disks to visualize the recursive flow.
- **Complexity:** Time $O(2^n)$, Space $O(n)$.

---

## Question 4: Recursive Binary Search
**File:** `q4_binary_search.py`

Binary search is an efficient algorithm for searching a sorted list by repeatedly dividing the search interval in half. This implementation uses recursion to narrow down the potential index of the target value.
- **Logic:** The algorithm compares the target value with the middle element; if they aren't equal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half.
- **Analysis:** Uses the Master Theorem and recursion tree method to justify its efficiency on large datasets.
- **Complexity:** Time $O(\log n)$, Space $O(\log n)$.

---

## Documentation
- `explanation.md`: Detailed technical justifications, mathematical derivations, and step-by-step traces for evaluation.

## How to Run
Ensure you have Python 3 installed. Run files via terminal:
```bash
python q1_factorial.py
python q2_fibonacci.py
python q3_tower_of_hanoi.py
python q4_binary_search.py
```

---
