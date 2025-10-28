from typing import Optional
from book import Book
from user import User

# Student
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


if __name__ == "__main__":
    pass