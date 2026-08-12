'''
1.5 Runtime and Complexity Comparison Table
You are building an algorithm performance comparison tool.
For a given input size n, prepare a runtime observation table for searching and sorting methods.
Instead of using actual execution time, use deterministic operation counts so that the output can be checked using auto-evaluation.
Calculate observation counts for the following methods:
Linear Search
Binary Search
Bubble Sort
Insertion Sort

Operation count rules:
Linear Search count is n.
Binary Search count is floor(log2(n)) + 1.
Bubble Sort count is n * (n - 1) / 2.
Insertion Sort count is n * (n - 1) / 2.
Also display the expected Big-O complexity and a simple observation for each method.

Input Format
First line: An integer n representing the input size.

Output Format
First print:
Runtime Complexity Comparison
Then print the heading:
Method ObservedCount ExpectedComplexity Observation
After that, print one row for each method.
Methods must be printed in this order:
Linear Search
Binary Search
Bubble Sort
Insertion Sort

Constraints
1 <= n <= 100000

Note :
The input-reading and output-handling functionality is already implemented in the hidden Wrapper Code.
Students should not write input(), main(), or additional input-handling statements in their submissions.
'''

# Solutions

