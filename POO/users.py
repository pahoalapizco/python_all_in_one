from typing import Protocol
from abc import ABC, abstractmethod
from book import Book
from exeptions import BorrowBookError, BookNotAvailableError, ReturnedBookError

class BorrowReturningBooksProtocol(Protocol):
    def borrow_book(self, book: Book) -> str: ...
    
    def returning_book(self, book: Book) -> str: ...

class BaseUser(ABC):
    @abstractmethod
    def borrow_book(self, book: Book) -> str:
        """ Verifies and changes book's availability, then adds the book into user's borrowed books.

        Args:
            book (Book): Book to borrow

        Returns:
            str: Authorization message
        """
        pass
    
    @abstractmethod
    def returning_book(self, book: Book) -> str:
        """ Verifies and changes book's availability, then removes the book from user's borrowed books.

        Args:
            book (Book): Book to return

        Returns:
            str: Confirmation message
        """
        pass

class User(BaseUser):
    def __init__(self, name: str, user_id: str) -> None:
        self.name = name
        self.user_id = user_id
        self.__borrowed_books: list[Book] = []
    
    def __str__(self):
        return f"User: {self.name}, ID: {self.user_id}, borrowed books: {len(self.borrowed_books)}"
    
    @property
    def borrowed_books(self) -> list[Book]:
        """List with user's borrowed books."""
        return self.__borrowed_books
    
    def borrow_book(self, book: Book) -> str:
        book.loan()
        self.borrowed_books.append(book)
        return f"Autorized loan of book '{book.title}'."

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
    def __init__(self, name, user_id, degree_program):
        super().__init__(name, user_id)
        self.degree_program = degree_program
        self.limit_books = 3
    
    def __str__(self):
        return f"Student: {self.name}\nID: {self.user_id}\n" \
            + f"Deegre program: {self.degree_program}\nBorrowed books: {len(self.borrowed_books)}"
    
    @classmethod
    def from_dict(cls, user_dict: dict, borrowed_books_list: list[Book]):
        """Creates a Student's instance and updates its borrowed books list if needed.

        Args:
            user_dict (dict): Student's Info, it mush follow the structure: {
                "name": "",
                "user_id": "",
                "degree_program": ""
            }
            borrowed_books_list (list[Book]): User's borrowed books

        Returns:
            Student: Rebuilt student
        """
        student = cls(
            name = user_dict["name"],
            user_id = user_dict["user_id"],
            degree_program = user_dict["degree_program"]
        )
        if len(borrowed_books_list) > 0:
            student._User__borrowed_books = borrowed_books_list
        return student
    
    def borrow_book(self, book: Book) -> str:
        if len(self.borrowed_books) < self.limit_books:
            book.loan()
            self.borrowed_books.append(book)
            return f"Autorized book '{book.title}' loan."
        
        raise BorrowBookError(f"Sorry! You have already had reached the limit of borrowed books. \nLimit: {self.limit_books}")

class Professor(User):
    def __init__(self, name, user_id, department):
        super().__init__(name, user_id)
        self.department = department
        self.limit_books = None

    def __str__(self):
            return f"Professor: {self.name}\nID: {self.user_id}\n" \
                + f"Deparment: {self.department}\nBorrowed books: {len(self.borrowed_books)}"

    @classmethod
    def from_dict(cls, user_dict: dict, borrowed_books_list: list[Book]):
        """Creates a Professor's instance and updates its borrowed books list if needed.

        Args:
            user_dict (dict): Professor's Info, it mush follow the structure: {
                "name": "",
                "user_id": "",
                "degree_program": ""
            }
            borrowed_books_list (list[Book]): User's borrowed books

        Returns:
            Professor: Rebuilt student
        """
        professor = cls(
            name = user_dict["name"],
            user_id = user_dict["user_id"],
            department = user_dict["department"]
        )
        if len(borrowed_books_list) > 0:
            professor._User__borrowed_books = borrowed_books_list
        return professor
    
    def borrow_book(self, book):
        return super().borrow_book(book)


if __name__ == "__main__":
    pass