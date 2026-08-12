# Design and Analysis Of Algorithms

## Books -

1. Fundamentals of computer algo - sartaj sahni
2. Intorduction to algorithms - Cormen

## Characterstics Of An Algorithm

There are certain condition that a algorithm must satisfy:

1. Input : The algorithm must have well defined input, `it may or may not have input (meaning external input)`.
2. Output : The algorithm must have well defined output, it `Must` produce an output.
3. Unambiguous : The algorithm should be clear and unambiguous and each step should be clear and concise.
4. Finite : The algorithm `must terminate` after a finite number of steps.
5. Effective : The algorithm must be effective and should terminate after a finite number of steps.
    > Each instruction must be basic and feasible to execute in a finite amount of time .

These characterstics defien if a Algorithm is correct or even a Algoithm in first place.
Eg:

1. Brushing ... ~

### Algorithm , PseudoCode and Program

1. Algorithm - `Informal` way To explain what needs to be done in a code. Indepenedednt of Porgramming Language.
2. Pseudocode - `Formal` way of structuring and mathematically conveying what needs to be done. Independednt of the Programming language.
3. Program - entirely based and dependednt on programming language dependent.

Pseudocode is a bridge between Algorithm and Program.

### Analysis of Algorithm

1. Space Complexity
2. Time Complexity

>Sometimes in input conditions also the Algorithm novality depends.
>Different Algorithm work better on differnet input conditions.

### Condition for a Good Algorithm - What makes a good algo ~

1. Correctness - An algorithm must produce correct output
2. Scalability - A scalable Algorithm works well even when the amount of data increases.
3. Efficiency - Time and Space Complexity , Efficient algorithm solve problem using less Time and Fewer resources.

#### Time Complexity

1. Absolute Time - Platform , Programing Lang , Processor dependent.
2. Growth Of Time
w.r.t input size.

Absolute time is Platform Dependednt thus in Algorithms analysis we dont use it , as it creates `issues in comparing` the data.

##### Asymptotic Notation

    Time estimation of growth rate in terms of 'n' (inputsize)
    we do not use actual running time because ,
        1. its platform dependent.

    Notations:
        1. Big O (O) - Upper Bound - indicates the worst-case scenario
        2. Big Omega (Ω) - Lower Bound - indicates the best-case scenario
        3. Theta (Θ) - Tight Bound - meaning algorithms runtime grows at the same rate in both the upper and lower bounds.

### Searching Algorithms

#### Linear Search and Binary Search

##### Linear Search - Arr can be sorted or unsorted

    comparing each element to the key , we stop when we find the element.
    eg:
        arr = [1,2,3,4,5]
        key = 3
        compare 1,2 with 3 -> 
    Time complexity : worst case - 

    
##### Binary Search

    We calculate the mid position.
    comparing the key with the mid positon , and comapring if greater or not.
    as per the information shifting the global index by mid+1 or mid-1 for left or right indexes.
    Time complexity : worst case - 
