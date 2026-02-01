import unittest
import sys
import os

# Add the parent directory (LIB-INV-MANAGER) to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Library_manager.book import book
from Library_manager.inventory import LibraryInventory

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        b = book("Python 101", "Harsh Dev Jha", "12345")
        self.assertEqual(b.title, "Python 101")
        self.assertEqual(b.status, "available")

    def test_issue_return(self):
        b = book("Test Book", "Author", "999")
        # Test Issue
        b.issued()
        self.assertEqual(b.status, "issued")
        # Test Return
        b.return_book()
        self.assertEqual(b.status, "available")
        
if __name__ == '__main__':
    unittest.main()
