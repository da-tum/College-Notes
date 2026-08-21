# DAA Study Notes: Greedy Strategy, Dynamic Programming & Graph Algorithms

## 1. Greedy Strategy

Greedy algorithms make the locally optimal choice at each step with the hope of finding a globally optimal solution.

### Key Properties

1. **Greedy Choice Property:** A global optimum can be arrived at by making a local optimal choice.
2. **Optimal Substructure:** An optimal solution to the problem contains optimal solutions to sub-problems.

### Classic Greedy Problems

- **Fractional Knapsack:** Sort items by value/weight ratio $v_i / w_i$ in descending order. Take maximum possible weight of highest ratio item. Time Complexity: $O(n \log n)$.
- **Huffman Coding:** Build optimal prefix tree using a min-priority queue. Time Complexity: $O(n \log n)$.
- **Minimum Spanning Tree (MST):**
  - **Prim's Algorithm:** Grows a single tree starting from a source vertex. Time: $O(E \log V)$ with Binary Heap.
  - **Kruskal's Algorithm:** Sorts edges by weight and uses Disjoint Set Union (DSU) to avoid cycles. Time: $O(E \log E)$.

---

## 2. Dynamic Programming (DP)

Dynamic Programming is used when subproblems overlap and possess optimal substructure.

### Approaches

1. **Top-Down with Memoization:** Recursive call stack + cache store.
2. **Bottom-Up with Tabulation:** Iterative table population from base cases.

### Core Problems & Recurrences

#### 1. 0/1 Knapsack Problem
- **State Definition:** $dp[i][w]$ = Max value using first $i$ items with capacity $w$.
- **Recurrence:**
  $$dp[i][w] = \begin{cases} 
  dp[i-1][w] & \text{if } w_i > w \\
  \max(dp[i-1][w], \, v_i + dp[i-1][w - w_i]) & \text{if } w_i \le w 
  \end{cases}$$
- **Time Complexity:** $O(n \cdot W)$ (Pseudo-polynomial).
- **Space Complexity:** $O(n \cdot W)$ or optimized to $O(W)$.

#### 2. Longest Common Subsequence (LCS)
- **Recurrence:**
  $$LCS(i, j) = \begin{cases} 
  0 & \text{if } i=0 \text{ or } j=0 \\
  1 + LCS(i-1, j-1) & \text{if } X[i] == Y[j] \\
  \max(LCS(i-1, j), \, LCS(i, j-1)) & \text{if } X[i] \neq Y[j]
  \end{cases}$$
- **Time Complexity:** $O(m \cdot n)$.

#### 3. Matrix Chain Multiplication (MCM)
- **Recurrence:**
  $$m[i, j] = \min_{i \le k < j} \{ m[i, k] + m[k+1, j] + p_{i-1} p_k p_j \}$$
- **Time Complexity:** $O(n^3)$.

---

## 3. Graph Traversals & Shortest Path Algorithms

| Algorithm | Strategy | Time Complexity | Use Case / Constraints |
|---|---|---|---|
| **BFS** | Queue / Level-order | $O(V + E)$ | Unweighted shortest path |
| **DFS** | Stack / Recursion | $O(V + E)$ | Topological sort, Cycle detection |
| **Dijkstra** | Greedy (Min-Heap) | $O((V + E) \log V)$ | Single-source, Non-negative weights |
| **Bellman-Ford** | DP Relaxation | $O(V \cdot E)$ | Single-source, Handles negative weights |
| **Floyd-Warshall**| All-Pairs DP | $O(V^3)$ | All-pairs shortest paths |
