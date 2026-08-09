'''
1.2 Linear Search and Binary Search Comparison
You are building an algorithm performance analysis toolkit.
Given a sorted list of integers and a target value, search the target using both 
Linear Search and Binary Search.
Both algorithms must return the first index of the target if it is present.
If the target is not present, return -1.
For performance comparison, count how many array elements are checked by each algorithm.
Linear Search checks elements from left to right.
Binary Search checks the middle element repeatedly and continues searching on the 
left side when the target is found, so that the first occurrence is returned.
After performing both searches, display which algorithm used fewer comparisons.
If both algorithms use the same number of comparisons, display Both Equal.

Input Format
The platform wrapper reads:
First line: Integer n
Second line: n space-separated sorted integers
Third line: Integer target The wrapper passes arr and target to 
compare_search_algorithms(arr, target).

Output Format
First print:
Search Comparison Report
Then print the Linear Search result and comparison count.
Then print the Binary Search result and comparison count.
Finally, print the better algorithm based on fewer comparisons.

Constraints
1 <= n <= 1000
-100000 <= arr[i] <= 100000
The array is sorted in non-decreasing order.
-100000 <= target <= 100000

Important Submission Instruction:
The platform wrapper will read n, the sorted array, and the target value, 
then pass the array and target to:
compare_search_algorithms(arr, target)
Do not use input() and do not print inside the function.
Complete only the given function and return the required output as a list of strings.
The wrapper will print each returned line.

Examples
Input
7
2 4 6 8 10 12 14
10
Output
Search Comparison Report
Linear Search
Index: 4
Comparisons: 5
Binary Search
Index: 4
Comparisons: 3
Better Algorithm: Binary Search
'''

#Solution

def compare_search_algorithms(arr, target):
    # your code goes here
  linear_index = binary_index = -1
  linear_count = binary_count = 0 

  #linear
  for i in range(len(arr)):
    linear_count += 1
    if arr[i] == target:
      linear_index = i
      break 

  # binary
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left+right)//2
    binary_count += 1

    if arr[mid] == target :
      binary_index = mid
      right = mid - 1
    elif arr[mid] < target :
      left = mid + 1
    else: 
      right = mid - 1

    # better algorithm
    if binary_count > linear_count :
      btr_algo = "Linear Search" 
    elif binary_count < linear_count :
      btr_algo = "Binary Search"
    else:
      btr_algo = "Both Equal"
      
  return ["Search Comparison Report",
          "Linear Search",
          f"Index: {linear_index}",
          f"Comparisons: {linear_count}",
          "Binary Search",
          f"Index: {binary_index}",
          f"Comparisons: {binary_count}",
          f"Better Algorithm: {btr_algo}"]

