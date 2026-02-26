"""
Single Linked List Implementation with Time Complexity Analysis

This program demonstrates a complete implementation of a Single Linked List
and discusses the time complexity of all its operations.
"""

class Node:
    """
    Node class represents a single node in the linked list.
    Each node contains data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList class implements all operations of a Single Linked List.
    
    A Single Linked List is a linear data structure where elements are stored
    in nodes. Each node contains:
    - data: the value stored in the node
    - next: reference to the next node in the sequence
    
    The list is traversed starting from the head (first node).
    """
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        
        Time Complexity: O(1) - Constant time
        We only need to update the head pointer.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning")
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        
        Time Complexity: O(n) - Linear time
        We need to traverse the entire list to find the last node.
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end (list was empty)")
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
        print(f"Inserted {data} at the end")
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position.
        
        Time Complexity: O(n) - Linear time
        We need to traverse to the position-1 node.
        
        Args:
            data: The data to insert
            position: The position at which to insert (0-indexed)
        """
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
        print(f"Inserted {data} at position {position}")
    
    def delete_from_beginning(self):
        """
        Delete the first node from the list.
        
        Time Complexity: O(1) - Constant time
        We only need to update the head pointer.
        """
        if self.head is None:
            print("List is empty, nothing to delete!")
            return
        
        deleted_data = self.head.data
        self.head = self.head.next
        print(f"Deleted {deleted_data} from the beginning")
    
    def delete_from_end(self):
        """
        Delete the last node from the list.
        
        Time Complexity: O(n) - Linear time
        We need to traverse to find the second-to-last node.
        """
        if self.head is None:
            print("List is empty, nothing to delete!")
            return
        
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Deleted {deleted_data} from the end")
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        print(f"Deleted {deleted_data} from the end")
    
    def delete_at_position(self, position):
        """
        Delete a node at a specific position.
        
        Time Complexity: O(n) - Linear time
        We need to traverse to the position-1 node.
        
        Args:
            position: The position of the node to delete (0-indexed)
        """
        if self.head is None:
            print("List is empty, nothing to delete!")
            return
        
        if position < 0:
            print("Invalid position!")
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
        
        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted {deleted_data} from position {position}")
    
    def search(self, target):
        """
        Search for a value in the list.
        
        Time Complexity: O(n) - Linear time
        In worst case, we may need to traverse the entire list.
        
        Returns:
            The position if found, -1 otherwise
        """
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def get_length(self):
        """
        Get the length of the linked list.
        
        Time Complexity: O(n) - Linear time
        We need to traverse the entire list to count nodes.
        """
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next
        
        return count
    
    def display(self):
        """
        Display all elements in the linked list.
        
        Time Complexity: O(n) - Linear time
        We need to traverse and print all nodes.
        """
        if self.head is None:
            print("List is empty!")
            return
        
        elements = []
        current = self.head
        
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print("Linked List: " + " -> ".join(elements) + " -> None")
    
    def get_head(self):
        """Return the head of the list."""
        return self.head


# ==================== DEMONSTRATION ====================

if __name__ == "__main__":
    print("=" * 60)
    print("SINGLE LINKED LIST - IMPLEMENTATION AND OPERATIONS")
    print("=" * 60)
    
    # Create a new linked list
    ll = LinkedList()
    
    # Test is_empty
    print("\n--- Testing is_empty ---")
    print(f"Is list empty? {ll.is_empty()}")
    
    # Insert at beginning
    print("\n--- Testing insert_at_beginning ---")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.display()
    
    # Insert at end
    print("\n--- Testing insert_at_end ---")
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.display()
    
    # Insert at position
    print("\n--- Testing insert_at_position ---")
    ll.insert_at_position(25, 2)
    ll.display()
    
    # Get length
    print("\n--- Testing get_length ---")
    print(f"Length of list: {ll.get_length()}")
    
    # Search
    print("\n--- Testing search ---")
    pos = ll.search(25)
    if pos != -1:
        print(f"25 found at position {pos}")
    else:
        print("25 not found in the list")
    
    pos = ll.search(100)
    if pos != -1:
        print(f"100 found at position {pos}")
    else:
        print("100 not found in the list")
    
    # Delete from beginning
    print("\n--- Testing delete_from_beginning ---")
    ll.delete_from_beginning()
    ll.display()
    
    # Delete from end
    print("\n--- Testing delete_from_end ---")
    ll.delete_from_end()
    ll.display()
    
    # Delete at position
    print("\n--- Testing delete_at_position ---")
    ll.delete_at_position(2)
    ll.display()
    
    # Final length
    print("\n--- Final length ---")
    print(f"Length of list: {ll.get_length()}")
    
    print("\n" + "=" * 60)
    print("TIME COMPLEXITY SUMMARY")
    print("=" * 60)
    print("""
    Operation                | Time Complexity
    -------------------------|-----------------
    is_empty()               | O(1)
    insert_at_beginning()    | O(1)
    insert_at_end()          | O(n)
    insert_at_position()     | O(n)
    delete_from_beginning()  | O(1)
    delete_from_end()        | O(n)
    delete_at_position()     | O(n)
    search()                 | O(n)
    get_length()             | O(n)
    display()                | O(n)
    
    Notes:
    - O(1) = Constant Time (doesn't depend on list size)
    - O(n) = Linear Time (grows with list size)
    
    Advantages of Linked List:
    - Dynamic size allocation
    - Efficient insertions/deletions at the beginning
    - No memory wastage (unlike arrays)
    
    Disadvantages:
    - No random access (must traverse sequentially)
    - Extra memory for storing pointers
    - Not cache-friendly (non-contiguous memory)
    """)
