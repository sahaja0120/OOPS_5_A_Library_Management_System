# member.py
"""
Member class representing a library member.

Attributes:
- member_id (str)
- name (str)
- borrowed_books (list of Book objects)

Methods:
- borrow_book(book)
- return_book(book_id)
- __str__() for printing member info

💡 Hint:
- Use append() to add to borrowed_books
- Use a loop to find a book to return
"""

# from book import Book

class Member:
    def __init__(self, member_id, name):
        # self.member_id = member_id
        # self.name = name
        # self.borrowed_books = []
        pass

    def borrow_book(self, book):
        # Hint: Add book to borrowed_books
        pass

    def return_book(self, book_id):
        # Hint: Remove book with matching ID from borrowed_books
        pass

    def __str__(self):
        # Hint: return f"Member[{self.member_id}] - {self.name}"
        pass
