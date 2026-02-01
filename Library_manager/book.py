

#-------- Task 1: Create a Book Class --------#
class book:
    def __init__(self, title, author, isbn, status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }
    
    def issued(self):
        self.status = "issued"
        
    def return_book(self):
        self.status = "available"
    
    def is_available(self):
        return self.status == "available"
