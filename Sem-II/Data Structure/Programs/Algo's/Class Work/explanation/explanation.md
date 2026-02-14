## Explanation of Fibonacci (fibs.py) and Factorial (fact.py) Codes

### Fibonacci Code (fibs.py)

**What the code does:**  
This function generates the first `n` numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones (starting from 0 and 1). It returns a list of these numbers. For example, `fibonacci(10)` outputs `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`.

**DSA Terminologies and Approach:**  
- **Iterative Algorithm:** The code uses a loop to build the sequence incrementally, avoiding recursion. This is a form of **dynamic programming** (specifically, bottom-up DP), where we compute and store intermediate results in a list to reuse them.  
- **Base Cases:** Handles edge cases for `n <= 0` (empty list), `n == 1` ([0]), and `n == 2` ([0, 1]) directly.  
- **Why this approach?** Iteration is chosen over recursion to prevent stack overflow for large `n`, as recursive Fibonacci (e.g., `fib(n) = fib(n-1) + fib(n-2)`) has exponential time complexity due to redundant calculations. This iterative version computes each number once, making it efficient and practical for larger inputs.

**Time Complexity:**  
- **O(n)**: The loop runs `n-2` times (for `n > 2`), performing constant-time operations (append and arithmetic). Each element is computed in linear time relative to `n`.

**Space Complexity:**  
- **O(n)**: The list `fib` stores up to `n` elements, growing linearly with input size. No additional data structures are used beyond this.

### Factorial Code (fact.py)

**What the code does:**  
This class computes the factorial of a non-negative integer `n` (n! = n × (n-1) × ... × 1). For example, `factorial(5)` returns 120 (5 × 4 × 3 × 2 × 1). It's implemented as a method in a class for modularity.

**DSA Terminologies and Approach:**  
- **Recursive Algorithm:** The function calls itself with `n-1` until reaching the base case (`n == 0` or `n == 1`, where factorial is 1). This is a classic example of **recursion**, breaking down the problem into smaller subproblems.  
- **Base Cases:** Explicitly handles `n == 0` and `n == 1` to terminate recursion and avoid infinite loops.  
- **Why this approach?** Recursion mirrors the mathematical definition of factorial and is intuitive for problems with self-similar substructures. However, it's not always optimal due to potential stack depth limits in languages like Python (recursion limit ~1000). An iterative version (using a loop to multiply from 1 to n) would be more efficient for large `n` but is not used here, possibly for educational purposes to demonstrate recursion.

**Time Complexity:**  
- **O(n)**: The function makes `n` recursive calls (one for each decrement), each performing constant-time work (multiplication and comparison).

**Space Complexity:**  
- **O(n)**: Due to the recursion stack, which holds up to `n` frames in memory. Each call adds a layer to the stack until the base case is reached.
