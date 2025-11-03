from typing import Protocol

from book import Book
from library import Library
from users import Student, Professor

## ===========  TESTING BOOK FUNCTIONALITY =========== 
def loan_book_similator(book: Book, borrow_times: int) -> None:
    for _ in range(borrow_times):
        if not book.is_available:
            book.recive_book()        
        book.loan()

def testing_books(books: dict[Book]):
    try:
        for (name, book) in books.items():
            print(book, "\n")
        
        # Simular prestamo de libros:
        loan_book_similator(books["book1"], 6)
        loan_book_similator(books["book3"], 3)
        
        print(f"{books["book1"].title} is", ("" if books["book1"].is_popular() else "not") ,"popular.")
        print(f"{books["book3"].title} is", ("" if books["book3"].is_popular() else "not") ,"popular.")
    except ValueError as e:
        print(e)


## =========== TESTING USER FUNCTIONALITY =========== 
# Practice of Duck Typing
class BorrowReturningBooksProtocol(Protocol):
    def borrow_book(self, book: Book) -> str: ...
    
    def returning_book(self, book: Book) -> str: ... 

def borrow_books_simulator(user: BorrowReturningBooksProtocol, books: list[Book]) -> None:
    for book in books:
        print(user.borrow_book(book))

def returning_simulator(user: BorrowReturningBooksProtocol, book: Book) -> None:
    print(user.returning_book(book))


def testing_users(books: dict[Book]):
    prof = Professor("Luis Martínez", "P-123456", "Sitemas")
    student = Student("Paola Alapizco", "S-951753", "Sistemas")
    
    book_list = [book for _, book in books.items()]
    
    # print(book_list[:4])
    borrow_books_simulator(prof, book_list)
    
    # Simulador de retorno de libros
    returning_simulator(prof, books["book1"])
    borrow_books_simulator(student, [book_list[0]])

def create_library(users: list[Student | Professor], books: list[Book]) -> Library:
    library = Library("The Fantastic Book Store", "123 Best Av.")
    
    # Register users:
    for _, user in users.items():
        library.register_user(user)
    
    # Add books:
    for _, book in books.items():
        library.add_book(book)
    
    return library


if __name__ == "__main__":
    books = {
        # Fiction
        "book1": Book("Harry Potter y la Piedra Filosofal", "JK Rowling", "123456789"),
        "book2": Book("22/11/63", "Stephen King", "789456123"),
        "book3": Book("El Problema de los Tres Cuerpos", "Cixin Liu", "456123789"),
        # Science
        "book4": Book("Deep Learning", "Jhon D. Keller", "15478932"),
        "book5": Book("Why Machines Learn", "Anil Ananthaswamy", "7854123694"),
        "book6": Book("Naked Statistics", "Charles Wheelan", "1597536548", False)
    }
    
    users = {
        "student1": Student("Paho Alapzico", "S-123456", "Ingeniería en Sistemas"),
        "student2": Student("Nachito", "S-123457", "Literatura Inglesa"),
        "prof1": Professor("Luis Martínez", "P-654321", "Sistemas"),
        "sprof2": Professor("Paho Alapzico", "P-654320", "Humanidades"),
    }

    
    # testing_users(books)
    library = create_library(users, books)
    testing_books(books)
    
    print(library)
    for book in library.get_popular_books():
        print(f"Book: {book.title}, Author: {book.author}")
        print(f"Times loan: {book.loan_times}")
        library.get_available_books