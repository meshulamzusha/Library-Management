from classes.logger import Logger
from classes.system_admin import SystemAdmin


class Library:
    """Manages book inventory and users."""
    nax_borrow = 14
    def __init__(self):
        """initialize a library with empty lists for users and books"""
        self.books = {}
        self.users = {}


    def register_user(self, user) -> None:
        """register a new user to the library"""
        if user.user_id in self.users.keys():
            print('User already registered')
        else:
            self.users[user.user_id] = user


    def add_book(self, book) -> None:
        """add a new book to the library's books list"""
        if book.isbn in self.books.keys():
            print('The book is already in the library.')
        else:
            self.books[book.isbn] = book


    def perform_borrow(self, user_id: str, isbn: str) -> None:
        if not user_id in self.users.keys():
            print('Unregistered user')
        if not isbn in self.books.keys():
            print('Book does not exist in the library.')

        if self.books[isbn].is_available:
            book = self.books[isbn]
            book.is_available = False
            self.users[user_id].borrow_book(book)
            Logger.log_action('BORROW', user_id=user_id, isbn=isbn)
            SystemAdmin.update_transactions_count()
        else:
            print('book not available')


    def perform_return(self, user_id: str, isbn: str) -> None:
        if not user_id in self.users.keys():
            print('Unregistered user')
        if not isbn in self.books.keys():
            print('Book does not exist in the library.')

        book = self.books[isbn]
        user = self.users[user_id]

        if self.books[isbn].is_available:
            print('The book is not borrowed')
        elif book not in user.books:
            print('user do not borrowed this book')
        else:
            user.return_book(book)
            Logger.log_action('RETURN', user_id=user_id, isbn=isbn)
            SystemAdmin.update_transactions_count()
