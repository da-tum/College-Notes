# DAA Study Notes: Asymptotic Analysis, Recurrences & Divide and Conquer

## 1. Asymptotic Analysis & Growth of Functions

Analyzing algorithm performance involves classifying functions according to their rate of growth.

### Formal Definitions

1. **Big-O Notation (Upper Bound):**
   $$O(g(n)) = \{ f(n) : \exists \, c > 0, n_0 > 0 \text{ s.t. } 0 \le f(n) \le c \cdot g(n) \, \forall n \ge n_0 \}$$
   Represents the worst-case scenario.

2. **Big-Omega Notation (Lower Bound):**
   $$\Omega(g(n)) = \{ f(n) : \exists \, c > 0, n_0 > 0 \text{ s.t. } 0 \le c \cdot g(n) \le f(n) \, \forall n \ge n_0 \}$$
   Represents the best-case scenario.

3. **Theta Notation (Tight Bound):**
   $$\Theta(g(n)) = \{ f(n) : \exists \, c_1, c_2 > 0, n_0 > 0 \text{ s.t. } 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \, \forall n \ge n_0 \}$$
   $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$.

---

## 2. Solving Recurrence Relations

### Master Theorem for Divide-and-Conquer

For recurrences of the form:
$$T(n) = a T(n/b) + f(n) \quad (a \ge 1, b > 1)$$

Compare $f(n)$ with $n^{\log_b a}$:

1. **Case 1:** If $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$.
2. **Case 2:** If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$, then $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. **Case 3:** If $f(n) = \Omega(n^{\log_b a + \epsilon})$ and regularity condition holds ($a f(n/b) \le c f(n)$ for $c < 1$), then $T(n) = \Theta(f(n))$.

---

## 3. Divide and Conquer Sorting Algorithms

### Merge Sort
- **Recurrence:** $T(n) = 2T(n/2) + \Theta(n)$
- **Time Complexity:** $\Theta(n \log n)$ in all cases (Best, Average, Worst).
- **Space Complexity:** $O(n)$ auxiliary space for merging.
- **Stability:** Stable sort.

### Quick Sort
- **Partition Scheme:** Lomuto or Hoare partition.
- **Recurrence (Worst-Case):** $T(n) = T(n-1) + \Theta(n) \implies O(n^2)$ (when array is already sorted and first/last element chosen as pivot).
- **Recurrence (Average-Case):** $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$.
- **Space Complexity:** $O(\log n)$ auxiliary stack space (in-place sorting).
- **Stability:** Unstable sort.
