# book.py
"""
Book class representing a library book.

Attributes:
- book_id (str)
- title (str)
- author (str)
- available (bool) → default True

Methods:
- mark_borrowed()
- mark_returned()
- __str__() for printing book info

💡 Hint:
- When book is borrowed → available = False
- When returned → available = True
"""

class Book:
    def __init__(self, book_id, title, author):
        # self.book_id = book_id
        # self.title = title
        # self.author = author
        # self.available = True
        pass

    def mark_borrowed(self):
        # Hint: Set available to False
        pass

    def mark_returned(self):
        # Hint: Set available to True
        pass

    def __str__(self):
        # Hint: return f"{self.title} by {self.author} (Available: {self.available})"
        pass
