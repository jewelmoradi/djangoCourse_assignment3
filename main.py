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
        if not self.available:
            self.available = True  # book is returned
            print(f'{self.title} is returned now!')
        else:
            print(f'the book {self.title} was not borrowed to be returned!')


class Member:

    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f'Member name: {self.name} has member ID: {self.member_id}'

    def borrow_book(self, book):
        if book in self.borrowed_books:  # the member had borrowed the book before
            print(f'the book {book.title} is already borrowed by {self.name}!')
        elif book.available:
            self.borrowed_books.append(book)
        book.borrow()  # handles the case of an unavailable book too

    def return_book(self, book):
        if not book.available:  # the book is borrowed
            if book in self.borrowed_books:  # the book is borrowed by this member
                self.borrowed_books.remove(book)
                book.return_book()
            else:  # the book is not borrowed by this member
                print(f'{self.name} has not borrowed {book.title}!')
        else:  # the book is not borrowed
            print(f'{book.title} was never borrowed!')


