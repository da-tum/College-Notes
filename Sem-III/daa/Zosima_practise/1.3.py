'''
1.3 Bubble Sort and Insertion Sort Performance Comparison
You are building an algorithm performance analysis toolkit.
Given three datasets, apply Bubble Sort and Insertion Sort on each dataset.
The three datasets represent:
Random Dataset
Sorted Dataset
Reverse Dataset
For each dataset, display the sorted output using Bubble Sort and Insertion Sort.
Also display deterministic performance counts instead of actual execution time.
For Bubble Sort, count the number of element comparisons and swaps.
Use optimized Bubble Sort, where the algorithm stops early if no swap occurs in a pass.
For Insertion Sort, count the number of element comparisons and shifts.
For Insertion Sort, count a comparison whenever an existing element is compared with the key.
After comparing both algorithms, print the better algorithm based on fewer comparisons.
If both algorithms use the same number of comparisons, print Both Equal.

Input Format
First line: An integer n representing the number of elements in each dataset.
Second line: n space-separated integers representing the random dataset.
Third line: n space-separated integers representing the sorted dataset.
Fourth line: n space-separated integers representing the reverse dataset.

Output Format
First print:
Sorting Performance Report
For each dataset, print the dataset type.
Then print Bubble Sort result, comparison count and swap count.
Then print Insertion Sort result, comparison count and shift count.
Finally, print the better algorithm for that dataset.

Constraints
1 <= n <= 100
-100000 <= arr[i] <= 100000
All three datasets contain exactly n integers.

Examples
Input
4
5 3 4 1
1 2 3 4
4 3 2 1
Output
Sorting Performance Report
Random Dataset
Bubble Sorted: 1 3 4 5
Bubble Comparisons: 6
Bubble Swaps: 5
Insertion Sorted: 1 3 4 5
Insertion Comparisons: 6
Insertion Shifts: 5
Better Algorithm: Both Equal
Sorted Dataset
Bubble Sorted: 1 2 3 4
Bubble Comparisons: 3
Bubble Swaps: 0
Insertion Sorted: 1 2 3 4
Insertion Comparisons: 3
Insertion Shifts: 0
Better Algorithm: Both Equal
Reverse Dataset
Bubble Sorted: 1 2 3 4
Bubble Comparisons: 6
Bubble Swaps: 6
Insertion Sorted: 1 2 3 4
Insertion Comparisons: 6
Insertion Shifts: 6
Better Algorithm: Both Equal
'''

#Solution 

def compare_bubble_insertion(random_data, sorted_data, reverse_data):
    # your code goes here
  result = ["Sorting Performance Report"]
  datasets = [("Random Dataset",random_data),
             ("Sorted Dataset",sorted_data),
             ("Reverse Dataset",reverse_data)]
  for name , array in datasets :
    b_arr, b_swap, b_comp = bubble_sort(array)
    i_arr, i_shift, i_comp = insertion_sort(array)
    b_str = " ".join(map(str,b_arr))
    i_str = " ".join(map(str,i_arr))

    if b_comp < i_comp:
      btr_algo = "Bubble Sort"
    elif b_comp > i_comp:
      btr_algo = "Insertion Sort"
    else: 
      btr_algo = "Both Equal"

    result.extend([
              name,
              f"Bubble Sorted: {b_str}",
              f"Bubble Comparisons: {b_comp}",
              f"Bubble Swaps: {b_swap}",
              f"Insertion Sorted: {i_str}",
              f"Insertion Comparisons: {i_comp}",
              f"Insertion Shifts: {i_shift}",
              f"Better Algorithm: {btr_algo}"
          ])
  return result
    
def bubble_sort (arr):
  comparison = 0
  swaps = 0 
  arr_copy = arr[:]
  n = len (arr_copy)

  for i in range (n):
    swapped = False
    for j in range (n-1-i):
      comparison += 1
      if arr_copy[j] > arr_copy[j+1]:
        arr_copy[j] , arr_copy[j+1] = arr_copy[j+1] , arr_copy[j]
        swaps += 1
        swapped = True 

    if not swapped:
      break
  return arr_copy , swaps , comparison

def insertion_sort (arr):
  comparison = 0
  shifts = 0 
  arr_copy = arr[:]
  n = len (arr_copy)

  for i in range (1,n):
    key = arr_copy[i]
    j = i -1 
    while j >= 0 : 
      comparison += 1
      if arr_copy [j] > key :
        arr_copy[j+1] = arr_copy[j]
        shifts += 1
        j -= 1
      else:
        break
    arr_copy[j+1] = key
  return arr_copy , shifts , comparison