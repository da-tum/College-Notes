"""
Experiment 10: Singly Linked List (Core Operations)

Aim: Implement dynamic insertion and deletion without shifting.

What is Singly Linked List?
- A linear data structure where elements are stored in nodes
- Each node has: data + pointer to next node
- Unlike arrays, no need to shift elements for insert/delete

Visual representation:
┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│  10  │ -> │  20  │ -> │  30  │ -> │  40  │ -> None
└──────┘    └──────┘    └──────┘    └──────┘
   HEAD                                      TAIL

Key Advantage: Insertion/Deletion doesn't require shifting elements!
"""

# ==================== NODE CLASS ====================
# Node is the building block of linked list
# Each node stores: 1) data (the value)  2) next (pointer to next node)
class Node:
    def __init__(self, data):
        self.data = data    # Store the value
        self.next = None    # Pointer to next node (initially None)


# ==================== LINKED LIST CLASS ====================
class SinglyLinkedList:
    """
    Linked List with head and tail pointers.
    - head: points to first node
    - tail: points to last node (for O(1) end insertion)
    """
    
    def __init__(self):
        self.head = None    # First node (None when empty)
        self.tail = None    # Last node (None when empty)
    
    
    # ==================== OPERATION 1: INSERT AT BEGINNING ====================
    # Add new node at the START of list
    # Time: O(1) - constant time, no traversal needed
    #
    # Before: HEAD -> [10] -> [20] -> None
    # After:  HEAD -> [5] -> [10] -> [20] -> None
    def insert_at_beginning(self, data):
        new_node = Node(data)    # Create new node with data
        
        if self.head is None:    # If list is empty
            self.head = new_node # New node becomes head
            self.tail = new_node # New node also becomes tail
        else:
            new_node.next = self.head    # Point new node to current head
            self.head = new_node         # Update head to new node
    
    
    # ==================== OPERATION 2: INSERT AT END ====================
    # Add new node at the END of list
    # Time: O(1) - using tail pointer, no traversal needed
    #
    # Before: HEAD -> [10] -> [20] -> TAIL
    # After:  HEAD -> [10] -> [20] -> [30] -> TAIL
    def insert_at_end(self, data):
        new_node = Node(data)    # Create new node
        
        if self.head is None:    # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node    # Point current tail to new node
            self.tail = new_node         # Update tail to new node
    
    
    # ==================== OPERATION 3: DELETE BY VALUE ====================
    # Delete first occurrence of value
    # Time: O(n) - may need to traverse
    #
    # Three cases:
    # 1. DELETE HEAD: Value is at first node
    # 2. DELETE MIDDLE: Value is in between
    # 3. DELETE TAIL: Value is at last node
    def delete_by_value(self, value):
        # Case 0: Empty list
        if self.head is None:
            return "List is empty"
        
        # Case 1: Delete HEAD node
        if self.head.data == value:
            if self.head == self.tail:  # Only one node in list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next  # Move head to next
            return f"Deleted {value} from head"
        
        # Case 2 & 3: Delete MIDDLE or TAIL node
        # Start from head and search for the node before target
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                # Found the node to delete (current.next)
                
                # Check if deleting TAIL
                if current.next == self.tail:
                    self.tail = current    # Update tail to previous node
                    current.next = None    # Remove link to deleted node
                else:
                    # Delete MIDDLE: skip the node
                    current.next = current.next.next
                return f"Deleted {value}"
            
            current = current.next  # Move to next node
        
        # Value not found in list
        return f"Value {value} not found"
    
    
    # ==================== OPERATION 4: TRAVERSE ====================
    # Display all elements from head to tail
    # Time: O(n) - must visit every node
    #
    # Output format: 10 -> 20 -> 30 -> None
    def traverse(self):
        if self.head is None:
            return "List is empty"
        
        elements = []    # Store all data values
        current = self.head
        
        # Loop until end of list (current becomes None)
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements)


# ==================== MAIN PROGRAM ====================
# Test all operations
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    # ----- Test Insert at Beginning -----
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(30)
    print("After insert at beginning:", sll.traverse())
    # Output: 30 -> 20 -> 10
    
    # ----- Test Insert at End -----
    sll.insert_at_end(40)
    sll.insert_at_end(50)
    print("After insert at end:", sll.traverse())
    # Output: 30 -> 20 -> 10 -> 40 -> 50
    
    # ----- Test Delete by Value -----
    # Delete from HEAD
    print(sll.delete_by_value(30))
    print("After deleting 30:", sll.traverse())
    # Output: 20 -> 10 -> 40 -> 50
    
    # Delete from MIDDLE
    print(sll.delete_by_value(40))
    print("After deleting 40:", sll.traverse())
    # Output: 20 -> 10 -> 50
    
    # Delete from TAIL
    print(sll.delete_by_value(50))
    print("After deleting 50:", sll.traverse())
    # Output: 20 -> 10
    
    # Try to delete value that doesn't exist
    print(sll.delete_by_value(100))
    print("After deleting 100:", sll.traverse())
    # Output: 20 -> 10


# ==================== TIME COMPLEXITY SUMMARY ====================
"""
Operation              | Time Complexity | Space Complexity
-----------------------|-----------------|------------------
insert_at_beginning()  | O(1)            | O(1)
insert_at_end()       | O(1)            | O(1)
delete_by_value()      | O(n)            | O(1)
traverse()             | O(n)            | O(1)

Why O(1) for insert?
- At beginning: Just update head pointer
- At end: Just update tail pointer (no traversal!)

Why O(n) for delete and traverse?
- Must search through the list to find the value or print all elements
"""
