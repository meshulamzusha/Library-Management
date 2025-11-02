from classes.book import Book
from classes.library import Library
from classes.system_admin import SystemAdmin
from classes.user import User

if __name__ == '__main__':
    book1 = Book('1984', 'George Orwell', '978-0451524935')
    book2 = Book('To Kill a Mockingbird', 'Harper Lee', '978-0061120084')
    book3 = Book('Dune', 'Frank Herbert', '978-0441172719')

    user1 = User('001', 'Ben')
    user2 = User('002', 'Jon')

    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.register_user(user1)
    library.register_user(user2)

    library.perform_borrow('001', '978-0441172719')

    SystemAdmin.report_stats()

    print([book.get_details() for book in user1.books])