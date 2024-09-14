# assignment 3
# library management system

class Book:

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # available is True by default

    def __str__(self):
        return f'Book {self.title} by {self.author} with ISBN {self.isbn}. Availability: {self.available}'

    def borrow(self):
        if self.available:
            self.available = False  # book is borrowed
            print(f'{self.title} is borrowed now!')
        else:
            print(f'the book {self.title} is not available!')

    def return_book(self):
        if self.available is False:
            self.available = True  # book is returned
            print(f'{self.title} is returned now!')
        else:
            print(f'the book {self.title} was not borrowed to be returned!')
