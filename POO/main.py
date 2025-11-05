import random
from typing import Protocol, Optional

from book import Book
from library import Library
from data import books_data, users_data
from users import Student, Professor, BorrowReturningBooksProtocol
from exeptions import ReturnedBookError, BookNotAvailableError, BorrowBookError, NotFoundUserError


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

def get_user() -> Optional[Student | Professor]:
    print("Please fill the next form to register a new user.")
    name = input("Name (name, last name): ")
    print("What type of user are you registering?")
    print(" 1 - Professor \n 2 - Student")    
    user_type = input("Chose and option: ")
    
    if user_type == "1":
        program = input("Department: ")
        user_id = "P"+str(random.randint(100_000, 600_000))
    elif user_type == "2":
        program = input("Degree program: ")
        user_id = "S"+str(random.randint(100_000, 600_000))
    else:
        raise ValueError(f"Please choose between these two options: 1 - Professor, 2 - Student.")
    
    if not name or not program:
        msj = (" name" if not name else "") \
            + (" department" if not program and user_type == "1" else "") \
            + (" degree program" if not program and user_type == "2" else "")
        
        raise ValueError(f"the folowing data are missed: {msj}")

    user = Professor(name, user_id, program) if user_type == "1" else Student(name, user_id, program)
    return user

def get_book() -> Book:
    pass

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
        print()
        
        if opt == 1:
            try:
                user = get_user()
                library.register_user(user)
                print(f"\nUser {user.name} has succesfully registered with and id: {user.user_id}")
            except ValueError as e:
                print (e)
        elif opt == 2:
            book = get_book()
            library.add_book(book)
            print(f"Book '{book.title}' has succesfully added into the library.")
        elif opt == 3:
            user_id = input("User ID: ")
            try:
                user = library.search_user(user_id)
                print(user)
            except NotFoundUserError as e:
                print(e)
        elif opt == 4:            
            print("\nPlease tell us what book you are looking for.\n")
            title = input("Book's title: ")
            isbn = input("Book's isbn: ")
            try:
                book = library.search_book(title, isbn)
                print(book)
            except BookNotAvailableError as e:
                print(e)
            except ValueError as e:
                print("Pleae write the book's title or isbn.")
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
