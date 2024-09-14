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

    def borrow_book(self, book: Book):
        if book in self.borrowed_books:  # the member had borrowed the book before
            print(f'the book {book.title} is already borrowed by {self.name}!')
        elif book.available:
            self.borrowed_books.append(book)
        book.borrow()  # handles the case of an unavailable book too

    def return_book(self, book: Book):
        if not book.available:  # the book is borrowed
            if book in self.borrowed_books:  # the book is borrowed by this member
                self.borrowed_books.remove(book)
                book.return_book()
            else:  # the book is not borrowed by this member
                print(f'{self.name} has not borrowed {book.title}!')
        else:  # the book is not borrowed
            print(f'{book.title} was never borrowed!')


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        if book in self.books:  # book is previously added to the library
            print(f'{book.title} is already registered in the library!')
        else:
            self.books.append(book)

    def register_member(self, member: Member):
        if member in self.members:  # member is previously registered in the library
            print(f'{member.name} is already registered in the library!')
        else:
            self.members.append(member)

    def issue_book(self, member_id, isbn):
        for member in self.members:  # searching for member in members list
            if member.member_id == member_id:
                for book in self.books:  # searching for book in books list
                    if book.isbn == isbn:
                        member.borrow_book(book)
                        break
                else:
                    print(f'there were no books with ISBN {isbn} found!')
        else:
            print(f'there were no members with ID {member_id} found!')

    def return_book(self, member_id, isbn):
        for member in self.members:  # searching for member in members list
            if member.member_id == member_id:
                for book in self.books:  # searching for book in books list
                    if book.isbn == isbn:
                        member.return_book(book)
                        break
                else:
                    print(f'there were no books with ISBN {isbn} found!')
        else:
            print(f'there were no members with ID {member_id} found!')
