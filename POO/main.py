from typing import Protocol

from book import Book
from library import Library
from data import books_data, users_data
from users import Student, Professor, BorrowReturningBooksProtocol
from exeptions import ReturnedBookError, BookNotAvailableError, BorrowBookError


def fill_library(library: Library, users: list[Student | Professor], books: list[Book]):
    """
    Function to register users and add books into a library instance.
    
    Args:
        library (Library): Library instance to fill with users and books
        users (list[Student  |  Professor]): List of users intances of students or profesors which are used to register into the librare instance.
        books (list[Book]): List of book instances which are used to fill the library.

    Returns:
        None
    """
    # Register users:
    for user in users:
        library.register_user(user)
    
    # Add books:
    for book in books:
        library.add_book(book)    

## ===========  TESTING BOOK FUNCTIONALITY =========== 
# loan a book direct from the Book's instance
def loan_book_similator(book: Book, borrow_times: int) -> None:
    try:
        for _ in range(borrow_times):
            if not book.is_available:
                book.recive_book()        
            book.loan()
    except ReturnedBookError as e:
        print(e)
    except BookNotAvailableError as e:
        print(e)

# loan a book from a user's instance
def borrow_books_simulator(user: BorrowReturningBooksProtocol, books: list[Book]) -> None:
    try:
        for book in books:
            print(user.borrow_book(book))
    except BorrowBookError as e:
        print(e)

# return a book from a user's intance
def returning_simulator(user: BorrowReturningBooksProtocol, book: Book) -> None:
    try:
        print(user.returning_book(book))
    except ReturnedBookError as e:
        print(e)

def menu():    
    try:
        menu_list = [
            "Register an user into the library system.",
            "Add a book to the library.",
            "Find a user.",
            "Find a book.",
            "Return a book.",
            "Available books.",
            "Get the most popular books.",
            "Exit.",
        ]
        
        print(" Library menu ".center(20, "="))
        for idx, opt_desc in enumerate(menu_list):
            print(f"  {idx+1} -> {opt_desc}")
        
        opt = int(input("Chose an option: "))
        
    except ValueError:
        raise TypeError(f"int value expected, got str")
    
    
    if opt < 1 or opt > len(menu_list):
        raise ValueError(f"int between 1 and {len(menu_list)} expected, got {opt}")
    
    return opt

def main():
    # Create and fill the library
    library = Library("The Fantastic Book Store", "123 Best Av.")
    fill_library(library, users_data, books_data)
    print(f"Welcome to {library.name}\n")
    print("Available Books:")
    for book in library.get_available_books():
        print(f"  - {book.title} (isbn: {book.isbn})")
    
    ## TODO: Code options' functionality
    while True:
        print("\n")
        opt = menu()
        
        if opt == 1:
            pass
        elif opt == 2:
            pass
        elif opt == 3:
            pass
        elif opt == 4:
            pass
        elif opt == 5:
            pass
        elif opt == 6:
            pass
        elif opt == 7:
            pass
        
        elif opt == 8:
            print("Thans for visiting us, we hope to see you soon...")
            break

if __name__ == "__main__":
    main()
