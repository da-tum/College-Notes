# Single Linked List - Explanation

This document provides a comprehensive explanation of the `single-linked-list.py` file, which implements a complete Single Linked List data structure in Python along with a detailed analysis of time complexity for all operations.

## Overview

A **Single Linked List** is a fundamental linear data structure in computer science. It consists of a sequence of nodes, where each node contains:
- **Data**: The value or information stored in the node
- **Next**: A reference (pointer) to the next node in the sequence

Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead, each element points to the next element, creating a dynamic chain of nodes.

## What is a Single Linked List?

### Basic Structure

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
│  Data   │     │  Data   │     │  Data   │     │  Data   │
│   10    │ --> │   20    │ --> │   30    │ --> │   40    │
└─────────┘     └─────────┘     └─────────┘     └─────────┘
      │                                       │
    HEAD                                  Null (None)
```

### Key Components

1. **Node**: The building block of a linked list. Contains data and a pointer to the next node.
2. **Head**: The first node in the linked list. If the list is empty, head is NULL (None in Python).
3. **Tail**: The last node in the linked list. Its next pointer always points to NULL (None).
4. **Next Pointer**: Links each node to the next node in the sequence.

## Code Structure

The code is organized into two main classes. Let's break down each component.

### 1. Node Class

```
python
class Node:
    """
    Node class represents a single node in the linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Purpose**: Represents a single node in the linked list.

**Attributes**:
- `data`: Stores the actual value/data for the node
- `next`: Reference to the next node (initialized as None)

**Design Note**: The `next` is initially set to `None` because when we create a node, it doesn't point to anything yet. The link is established later when inserting the node into the list.

### 2. LinkedList Class

The `LinkedList` class contains all the operations that can be performed on a singly linked list.

#### Constructor

```
python
def __init__(self):
    self.head = None
```

- Initializes an empty linked list with `head` set to `None`
- An empty list has no nodes, so head being None indicates an empty list

#### Core Operations

##### a) is_empty()

```
python
def is_empty(self):
    """Check if the linked list is empty."""
    return self.head is None
```

- **Time Complexity**: O(1) - Constant Time
- **Explanation**: We only check if head is None, which is a single operation regardless of list size.

##### b) insert_at_beginning(data)

```
python
def insert_at_beginning(self, data):
    """
    Insert a new node at the beginning of the list.
    Time Complexity: O(1) - Constant time
    """
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

- **Time Complexity**: O(1) - Constant Time
- **Steps**:
  1. Create a new node with the given data
  2. Point new_node's next to the current head
  3. Update head to point to the new node
- **Why O(1)?**: We perform a fixed number of operations regardless of list size.

##### c) insert_at_end(data)

```
python
def insert_at_end(self, data):
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
        return
    
    current = self.head
    while current.next is not None:
        current = current.next
    
    current.next = new_node
```

- **Time Complexity**: O(n) - Linear Time
- **Steps**:
  1. Handle empty list case (special case)
  2. Traverse the entire list to reach the last node
  3. Point the last node's next to the new node
- **Why O(n)?**: We must visit each node to find the end. In worst case (list of n nodes), we traverse all n nodes.

##### d) insert_at_position(data, position)

```
python
def insert_at_position(self, data, position):
    if position < 0:
        print("Invalid position!")
        return
    
    if position == 0:
        self.insert_at_beginning(data)
        return
    
    new_node = Node(data)
    current = self.head
    count = 0
    
    while current is not None and count < position - 1:
        current = current.next
        count += 1
    
    if current is None:
        print(f"Position {position} out of bounds!")
        return
    
    new_node.next = current.next
    current.next = new_node
```

- **Time Complexity**: O(n) - Linear Time
- **Steps**:
  1. Handle edge cases (negative position, position 0)
  2. Traverse to the node just before the target position
  3. Insert the new node by adjusting pointers
- **Why O(n)?**: In worst case (inserting at end), we traverse all n nodes.

##### e) delete_from_beginning()

```
python
def delete_from_beginning(self):
    if self.head is None:
        print("List is empty, nothing to delete!")
        return
    
    self.head = self.head.next
```

- **Time Complexity**: O(1) - Constant Time
- **Steps**:
  1. Check if list is empty
  2. Move head to the next node
- **Why O(1)?**: Single operation regardless of list size.

##### f) delete_from_end()

```
python
def delete_from_end(self):
    if self.head is None:
        print("List is empty, nothing to delete!")
        return
    
    if self.head.next is None:
        self.head = None
        return
    
    current = self.head
    while current.next.next is not None:
        current = current.next
    
    current.next = None
```

- **Time Complexity**: O(n) - Linear Time
- **Steps**:
  1. Handle empty list and single node cases
  2. Traverse to find the second-to-last node
  3. Set second-to-last node's next to None
- **Why O(n)?**: Must traverse to find the node before the last.

##### g) delete_at_position(position)

```
python
def delete_at_position(self, position):
    if self.head is None:
        print("List is empty, nothing to delete!")
        return
    
    if position == 0:
        self.delete_from_beginning()
        return
    
    current = self.head
    count = 0
    
    while current.next is not None and count < position - 1:
        current = current.next
        count += 1
    
    if current.next is None:
        print(f"Position {position} out of bounds!")
        return
    
    current.next = current.next.next
```

- **Time Complexity**: O(n) - Linear Time
- **Why O(n)?**: Must traverse to position-1 to delete the node at given position.

##### h) search(target)

```
python
def search(self, target):
    current = self.head
    position = 0
    
    while current is not None:
        if current.data == target:
            return position
        current = current.next
        position += 1
    
    return -1
```

- **Time Complexity**: O(n) - Linear Time
- **Steps**:
  1. Start from head
  2. Compare each node's data with target
  3. Return position if found, -1 if not found
- **Why O(n)?**: In worst case, target is at the last position or not present, requiring full traversal.

##### i) get_length()

```
python
def get_length(self):
    count = 0
    current = self.head
    
    while current is not None:
        count += 1
        current = current.next
    
    return count
```

- **Time Complexity**: O(n) - Linear Time
- **Why O(n)?**: Must visit every node to count them.

##### j) display()

```
python
def display(self):
    if self.head is None:
        print("List is empty!")
        return
    
    elements = []
    current = self.head
    
    while current is not None:
        elements.append(str(current.data))
        current = current.next
    
    print("Linked List: " + " -> ".join(elements) + " -> None")
```

- **Time Complexity**: O(n) - Linear Time
- **Why O(n)?**: Must visit every node to print all elements.

## Time Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|-------------------|
| is_empty() | O(1) | O(1) |
| insert_at_beginning() | O(1) | O(1) |
| insert_at_end() | O(n) | O(1) |
| insert_at_position() | O(n) | O(1) |
| delete_from_beginning() | O(1) | O(1) |
| delete_from_end() | O(n) | O(1) |
| delete_at_position() | O(n) | O(1) |
| search() | O(n) | O(1) |
| get_length() | O(n) | O(1) |
| display() | O(n) | O(1) |

### Understanding Big O Notation

- **O(1) - Constant Time**: The operation takes the same amount of time regardless of the list size.
- **O(n) - Linear Time**: The operation takes time proportional to the number of elements in the list.

### Why These Complexities?

1. **O(1) Operations**: These only modify or access the head pointer, requiring no traversal.

2. **O(n) Operations**: These require traversing the list to:
   - Find the end (insert_at_end)
   - Find a specific position (insert_at_position, delete_at_position)
   - Check every element (search, get_length, display)

## Advantages of Linked Lists

1. **Dynamic Size**: Can grow or shrink dynamically during runtime
2. **Efficient Insertions/Deletions**: O(1) for insertions/deletions at the beginning
3. **No Memory Wastage**: No pre-allocation of memory (unlike arrays)
4. **Simple Implementation**: Easier to implement compared to other data structures

## Disadvantages of Linked Lists

1. **No Random Access**: Cannot access elements directly by index
2. **Extra Memory**: Requires extra memory for storing pointers
3. **Not Cache-Friendly**: Nodes are scattered in memory, causing cache misses
4. **Traversal Required**: Must traverse sequentially to find elements

## When to Use Linked Lists?

- When the size of data is unknown or changes frequently
- When frequent insertions/deletions at the beginning are required
- When implementing other data structures (stacks, queues)
- When memory allocation needs to be flexible

## Comparison with Arrays

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory Layout | Contiguous | Scattered |
| Size | Fixed (usually) | Dynamic |
| Access Time | O(1) - Random Access | O(n) - Sequential |
| Insertion at Beginning | O(n) | O(1) |
| Insertion at End | O(1) | O(n) or O(1)* |
| Deletion at Beginning | O(n) | O(1) |
| Deletion at End | O(1) | O(n) |
| Extra Memory | None | Pointer per element |

*With tail pointer

## Conclusion

This implementation demonstrates a complete Single Linked List with all fundamental operations. The time complexity analysis shows that while linked lists excel at insertions and deletions at the beginning (O(1)), they require linear time for operations that need to traverse the list (O(n)).

Understanding these trade-offs is crucial for choosing the right data structure for specific applications. Linked lists are particularly useful when:
- The number of elements is unpredictable
- Frequent modifications at the beginning are needed
- Sequential access is acceptable

The code provides a clear, educational example of how linked lists work internally and serves as a foundation for understanding more complex data structures like doubly linked lists, circular linked lists, and more.
