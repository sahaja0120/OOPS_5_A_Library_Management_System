# library.py
"""
Library class to manage books and members.

Responsibilities:
- Store books in dict {book_id: Book}
- Store members in dict {member_id: Member}
- Add book, add member
- Borrow book
- Return book

💡 Hints:
- Use book.mark_borrowed() when lending
- Raise BookNotAvailableError if book not available
- Check if member exists before borrowing
"""

# from book import Book
# from member import Member
# from exceptions import BookNotFoundError, BookNotAvailableError, MemberNotFoundError

class Library:
    def __init__(self):
        # self.books = {}
        # self.members = {}
        pass

    def add_book(self, book):
        # Hint: Add book to self.books using book.book_id
        pass

    def add_member(self, member):
        # Hint: Add member to self.members using member.member_id
        pass

    def borrow_book(self, member_id, book_id):
        # Hint: Get member + book, check availability, update both
        pass

    def return_book(self, member_id, book_id):
        # Hint: Mark book as returned + remove from member
        pass
