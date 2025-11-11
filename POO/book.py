import uuid
from typing import Optional
from datetime import datetime

from exeptions import BookNotAvailableError, ReturnedBookError

class Book:
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True, ID: Optional[str] = None) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.is_available: bool = is_available
        self.__loan_times: int = 0
        self.__limit_loan_days: int = 7
        self.__loan_date: Optional[datetime]= None
        self.__UUID = str(uuid.uuid1()) if not ID else ID
    
    def __str__(self) -> str:
        msj = "This title is" + ("" if self.is_available else " not") + " available"
        return f"{self.title} by {self.author}. \nLoan times: {self.loan_times} \n{msj}."

    @classmethod
    def from_dict(cls, book_dict: dict):
        book = cls(
            title = book_dict["title"],
            author = book_dict["author"],
            isbn = book_dict["isbn"],
            is_available = book_dict["is_available"],
            ID = book_dict["_Book__UUID"]
        )
        book.loan_times = book_dict["_Book__loan_times"]
        book.__loan_date = book_dict["_Book__loan_date"]
        
        return book
    ## ======== PROPERTIES ========
    @property
    def loan_times(self) -> int:        
        """Number of times a book has been loaned"""
        return self.__loan_times
    
    @loan_times.setter
    def loan_times(self, times: int) -> None:
        self.__loan_times = times
    
    @property
    def limit_loan_days(self) -> int:
        """Limit days a user can borrow a book"""
        return self.__limit_loan_days
    
    @property
    def loan_date(self) -> Optional[datetime]:
        """Date the book has loaned"""
        return self.__loan_date
    
    ## ======== METHODS ========    
    def loan(self) -> None:
        """
        Loan a book, it's marked as unavailable (is_availble = False), 
        set the date when it was loaned, 
        and increase the loan_times counter.

        Raises:
            BookNotAvailableError: Raised an error when the book is not available to loan.
        """
        if self.is_available:
            self.is_available = False
            self.loan_times += 1
            self.__loan_date = datetime.now().isoformat()
        else:
            raise BookNotAvailableError(f"'{self.title}' is not available.")

    def recive_book(self) -> None:
        """
        Return the book to the library.
        It marks the book available and reset to None the loan date.

        Raises:
            ReturnedBookError: Raised an error when the book is not available to returned. 
        """
        if not self.is_available:
            self.is_available = True
            self.__loan_date = None
        else:
            raise ReturnedBookError(f"'{self.title}' has been already returned")

    def is_popular(self) -> bool:
        """_summary_
        Returns True if the book has been loaned more than 5 times.
        
        Returns:
            bool: True if loan_times is more than 5, otherwise returns False.
        """
        return self.loan_times > 5
    
    def duration_time(self) -> int:
        """
        Calculate the remaining days that the book must be returned by the user.

        Returns:
            int: Number of days the user has to return the book.
        """
        diff = datetime.now() - datetime.fromisoformat(self.loan_date)
        return self.limit_loan_days - diff.days


if __name__ == "__main__":
    book = Book.from_dict({
            "title": "El Problema de los Tres Cuerpos",
            "author": "Cixin Liu",
            "isbn": "456123789",
            "is_available": False,
            "_Book__loan_times": 1,
            "_Book__limit_loan_days": 7,
            "_Book__loan_date": "2025-11-07T10:40:52.655156",
            "_Book__UUID": "600cf962-bc24-11f0-9c5e-7e6a8f7333de"
        })
    print(book)
    print(book.loan_date)
    print(book.duration_time())