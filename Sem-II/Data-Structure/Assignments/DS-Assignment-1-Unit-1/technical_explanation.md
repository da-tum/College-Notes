# Technical Explanation - Unit 1 Assignment

This document provides a detailed technical breakdown of the recursive algorithms implemented in this assignment, including traces and complexity justifications.

---

## 1. Recursive Factorial (Q=1)
### Implementations:
- **Naive Recursion:** Uses the standard recurrence $F(n) = n * F(n-1)$.
- **Memoized Recursion:** Uses a dictionary to store previously calculated values, preventing redundant recursive calls.

### Complexity:
- **Time Complexity:** $O(n)$ for both (single session). Memoization is $O(1)$ for repeated calls.
- **Space Complexity:** $O(n)$ due to the recursive call stack depth.

---

## 2. Recursive Fibonacci (Q=2)
### The Inefficiency of Naive Recursion:
In the naive approach ($F(n) = F(n-1) + F(n-2)$), the same subproblems are solved multiple times. For example, calculating $F(5)$ requires calculating $F(3)$ twice and $F(2)$ three times. This leads to an exponential growth in calls.

### Complexity:
- **Naive Time:** $O(2^n)$ (Approx. $O(1.618^n)$).
- **Memoized Time:** $O(n)$ - Each value is only computed once.
- **Space Complexity:** $O(n)$ for the recursion stack and cache.

---

## 3. Tower of Hanoi (Q=3)
### Trace for N=3 (Disks):
Steps to move 3 disks from A to C using B:
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. **Move disk 3 from A to C**
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

### Complexity Justification:
The recurrence relation is $T(n) = 2T(n-1) + 1$. Solving this as a geometric progression results in $T(n) = 2^n - 1$.
- **Time Complexity:** $O(2^n)$.
- **Space Complexity:** $O(n)$ (Stack depth).

---

## 4. Recursive Binary Search (Q=4)
### Recurrence-Based Complexity:
The search space is halved in each step: $T(n) = T(n/2) + O(1)$.

### Master Theorem Calculation:
$T(n) = aT(n/b) + f(n)$ where $a=1, b=2, f(n)=1$.
$n^{\log_b a} = n^{\log_2 1} = n^0 = 1$.
Since $f(n) = \Theta(1)$, Case 2 of the Master Theorem applies.
**Time Complexity:** $O(\log n)$.

### Space Complexity:
$O(\log n)$ due to the recursive stack depth proportional to the number of splits.
