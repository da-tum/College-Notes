"""
Name: Harsh Dev Jha
Date: 2/12/25
Title: Library Inventory Manager
"""
import sys
import os

# Add the parent directory (LIB-INV-MANAGER) to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Library_manager.inventory import LibraryInventory
from Library_manager.book import book
from pathlib import Path
import logging

#---------Task 4: Menu-Driven CLI ---------#
# add issue return view search exit 
def menu():
    print("\nLibrary Inventory Manager")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book by Title/ISBN (Internal Choice)")
    print("6. Exit")
    
def main():
    book_inventory = LibraryInventory()
    while True:
        try:
            if not Path(book_inventory.filename).exists():
                with open(book_inventory.filename, 'w') as f:
                    f.write('[]')  # Initialize with empty list
            menu()
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                book_inventory.add_book(title, author, isbn)
                
            elif choice == '2':
                isbn = input("Enter ISBN of the book to issue: ")
                book_inventory.issue_book(isbn)
                    
            elif choice == '3':
                isbn = input("Enter ISBN of the book to return: ")
                book_inventory.return_book(isbn)
                    
            elif choice == '4':
                book_inventory.display_all()
                
            elif choice == '5':
                search_choice = input("Search by (1) Title or (2) ISBN? ")
                if search_choice == '1':
                    title = input("Enter book title: ")
                    found_book = book_inventory.search_by_title(title)
                elif search_choice == '2':
                    isbn = input("Enter book ISBN: ")
                    found_book = book_inventory.search_by_isbn(isbn)
                else:
                    print("Invalid choice.")
                    continue
                if found_book:
                    print("Book found:")
                    print(found_book)
                else:
                    print("Book not found.")
                    
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")   
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print("An error occurred. Please try again.") 
    
if __name__ == "__main__":
    main()