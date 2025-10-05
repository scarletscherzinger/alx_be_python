# programming_paradigm/library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # was not checked out

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # not found or unavailable

    def return_book(self, title):
        """Return a checked-out book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # not found or already available

    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


