from book import Book
from typing import Optional

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
        except ValueError as e:
            return e

    def returning_book(self, book: Book) -> str:
        if len(self.borrowed_books) == 0:
            return "You have not borroed any book yet."
        else:
            try:
                idx = self.borrowed_books.index(book)
                book.recive_book()
                self.borrowed_books.pop(idx)
                return f"Book '{book.title}' returned sucessfully."
            except ValueError as e:
                return e

class Student(User):
    def __init__(self, name, ID, degree_program):
        super().__init__(name, ID)
        self.degree_program = degree_program
        self.limit_books = 3

    def borrow_book(self, book: Book) -> str:
        try:
            if len(self.borrowed_books) < self.limit_books:
                book.loan()
                self.borrowed_books.append(book)
                return f"Autorized book '{book.title}' loan."
            else:
                return f"Sorry! You have already had reached the limit of borrowed books. \nLimit: {self.limit_books}"
        except ValueError as e:
            return e

class Professor(User):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.limit_books = None

    def borrow_book(self, book):
        return super().borrow_book(book)


if __name__ == "__main__":
    pass