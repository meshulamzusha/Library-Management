class Book:
    def __init__(self, title: str, author: str, isbn: str, is_available: bool=True) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available


    def get_details(self) -> str:
        return f'title: {self.title}, author: {self.author}, isbn: {self.isbn}, is_available: {self.is_available}'
