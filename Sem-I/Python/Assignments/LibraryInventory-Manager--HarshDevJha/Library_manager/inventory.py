import json
import logging
from pathlib import Path
from .book import book

#--------- Task 5: Logging Configuration --------#

logging.basicConfig(
    filename='library_inventory.log',
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


#-------- Task 2: Create LibraryInventory Class --------#
class LibraryInventory:
    def __init__(self,filename='book_data.json'):
        self.books = []
        self.filename=filename
        self.load_book()
    
    def add_book(self, title, author, isbn):
        # Check for duplicate using isbn
        if self.search_by_isbn(isbn):
            logging.warning(f"Attempted to add duplicate ISBN: {isbn}")
            print("Error: A book with this ISBN already exists.")
            return
        new_book = book(title, author, isbn, "available")
        self.books.append(new_book)
        self.save_book()
        logging.info(f"Book added: {title} ({isbn})")
        print("Book added successfully.")
        
    def search_by_title(self, title):
        '''Searches for a book by its title.'''
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def search_by_isbn(self, isbn):
        '''Searches for a book by its ISBN.'''
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def display_all(self):
        '''Displays all books in the inventory.'''
        if not self.books:
            print("No books in inventory.")
        for book in self.books:
            print(book)

    def issue_book(self, isbn):
        '''Issues a book by ISBN.'''
        book = self.search_by_isbn(isbn)
        if book and book.is_available():
            book.issued()
            self.save_book()
            logging.info(f"Book issued: {book.title} ({isbn})")
            print("Book issued successfully.")
        elif book:
            print("Book is already issued.")
        else:
            print("Book not found.")

    def return_book(self, isbn):
        '''Returns a book by ISBN.'''
        book = self.search_by_isbn(isbn)
        if book and not book.is_available():
            book.return_book()
            self.save_book()
            logging.info(f"Book returned: {book.title} ({isbn})")
            print("Book returned successfully.")
        elif book:
            print("Book is already available.")
        else:
            print("Book not found.")
            
#-------- Task 3: Data Persistence with JSON --------#
            
    def save_book(self):
        """Saves the list of books to a JSON file."""
        try:
            # Convert list of Book objects to list of dicts
            data = [book.to_dict() for book in self.books]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logging.error(f"Failed to save data: {e}")
              
    def load_book(self):
        """Loads books from JSON file."""
        file_path = Path(self.filename)
        if not file_path.exists():
            logging.warning("JSON file not found. Starting with empty inventory.")
            return
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                # Convert list of dicts back to list of Book objects
                self.books = [book.from_dict(item) for item in data]
            logging.info(f"Loaded {len(self.books)} books from storage.")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            self.books = []
