from book import Book
from typing import Protocol

from exeptions import BookNotAvailableError, ReturnedBookError
class BorrowReturningBooksProtocol(Protocol):
    def borrow_book(self, book: Book) -> str: ...
    
    def returning_book(self, book: Book) -> str: ...

class User():
    def __init__(self, name: str, ID: str) -> None:
        self.name = name
        self.ID = ID
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> str:
        try:
            book.loan()
            self.borrowed_books.append(book)
            return f"Autorized loan of book '{book.title}'."
        except BookNotAvailableError as e:
            return e

    def returning_book(self, book: Book) -> str:
        if self.borrowed_books.count(book) == 0:
            raise ReturnedBookError(f"{book.title} is not in the borrowed list")
        
        if len(self.borrowed_books) == 0:
            return "You have not borroed any book yet."
        else:
            idx = self.borrowed_books.index(book)
            book.recive_book()
            self.borrowed_books.pop(idx)
            return f"Book '{book.title}' returned sucessfully."

class Student(User):
    def __init__(self, name, ID, degree_program):
        super().__init__(name, ID)
        self.degree_program = degree_program
        self.limit_books = 3

    def borrow_book(self, book: Book) -> str:
        if len(self.borrowed_books) < self.limit_books:
            book.loan()
            self.borrowed_books.append(book)
            return f"Autorized book '{book.title}' loan."
        else:
            return f"Sorry! You have already had reached the limit of borrowed books. \nLimit: {self.limit_books}"

class Professor(User):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.limit_books = None

    def borrow_book(self, book):
        return super().borrow_book(book)


if __name__ == "__main__":
    pass