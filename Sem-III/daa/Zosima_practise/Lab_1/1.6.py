'''
1.6 Runtime Comparison Chart Data and Scalability Report
You are building a runtime comparison and scalability reporting tool.
Given different input sizes, prepare chart-ready runtime count data for searching and sorting algorithms.
Instead of generating actual charts, the program must generate structured data that can be used to draw comparison charts.
Use deterministic operation-count estimates so that the output can be checked through auto-evaluation.
Calculate operation counts for the following algorithms:
Linear Search
Binary Search
Bubble Sort
Insertion Sort
Operation count rules:
Linear Search count is n.
Binary Search count is floor(log2(n)) + 1.
Bubble Sort count is n * (n - 1) / 2.
Insertion Sort count is n * (n - 1) / 2.
After generating chart data, prepare a scalability summary showing complexity and scalability level.
Use the following scalability levels:
Binary Search: Excellent
Linear Search: Moderate
Bubble Sort: Poor
Insertion Sort: Poor

Input Format
First line: An integer k representing the number of input sizes.
Second line: k space-separated integers representing input sizes.

Output Format
First print:
Runtime Comparison Chart Data
Then print the heading:
InputSize LinearSearch BinarySearch BubbleSort InsertionSort
After that, print one row for each input size.
Then print:
Scalability Summary
Then print the heading:
Algorithm Complexity Scalability
After that, print algorithm complexity and scalability level.
Finally, print key observations and conclusion.

Constraints
1 <= k <= 20
1 <= n <= 100000
All input sizes are positive integers.

Note :
The input-reading and output-handling functionality is already implemented in the hidden Wrapper Code. 
Students should not write input(), main(), or additional input-handling statements in their submissions.
'''

# Solution

