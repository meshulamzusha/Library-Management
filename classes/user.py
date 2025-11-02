class User:
    """
    represent a user with:
        attributes:
            * user_id
            * name
            * list of books now by the user
        methods:
            * borrow_book: add book to 'books'
            * return_book: remove book from 'books'
    """
    def __init__(self, user_id: str, name: str) -> None:
        """initialize a user object with user_id, name and empty list 'books' """
        self.user_id = user_id
        self.name = name
        self.books = []


    def borrow_book(self, book) -> None:
        """add the provided book to objname.books"""
        self.books.append(book)


    def return_book(self, book) -> None:
        """remove the provided book from objname.books"""
        for i in range(len(self.books)):
            if self.books[i].isbn == book.isbn:
                self.books.remove(i)
            else:
                print(f'book with isbn {book.isbn} is not use by by {self.name}.')