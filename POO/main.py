import random
from typing import Optional

from book import Book
from library import Library
from persistence import Persistence
from users import Student, Professor, BorrowReturningBooksProtocol
from exeptions import (
    ReturnedBookError,
    BookNotAvailableError,
    BorrowBookError,
    NotFoundUserError,
)


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
def borrow_books_simulator(
    user: BorrowReturningBooksProtocol, books: list[Book]
) -> None:
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
            "Register users.",
            "Add books to the library",
            "Find a user",
            "Find a book",
            "Loan a book",
            "Return a book",
            "Available books",
            "Most popular books",
            "Exit",
        ]

        print(" Library menu ".center(20, "="))
        for idx, opt_desc in enumerate(menu_list):
            print(f"  {idx + 1} → {opt_desc}")

        opt = int(input("Chose an option: "))

    except ValueError:
        raise TypeError("int value expected, got str")

    if opt < 1 or opt > len(menu_list):
        raise ValueError(f"int between 1 and {len(menu_list)} expected, got {opt}")

    return opt


# Functions to: Get user's info to register and search users into the library
def get_user_info() -> Optional[Student | Professor]:
    print("Please fill the next form to register a new user.")
    name = input("Name (name, last name): ")
    print("What type of user are you registering?")
    print(" 1 - Professor \n 2 - Student")
    user_type = input("Chose and option: ")

    if user_type == "1":
        program = input("Department: ")
        user_id = "P" + str(random.randint(100_000, 600_000))
    elif user_type == "2":
        program = input("Degree program: ")
        user_id = "S" + str(random.randint(100_000, 600_000))
    else:
        raise ValueError(
            "Please choose between these two options: 1 - Professor, 2 - Student."
        )

    if not name or not program:
        msj = (
            (" name" if not name else "")
            + (" department" if not program and user_type == "1" else "")
            + (" degree program" if not program and user_type == "2" else "")
        )

        raise ValueError(f"the folowing data are missed: {msj}")

    user = (
        Professor(name, user_id, program)
        if user_type == "1"
        else Student(name, user_id, program)
    )
    return user


def find_user(library: Library) -> Student | Professor:
    user_id = input("User ID: ")
    user = library.search_user(user_id)
    return user


# Functions to: Get book's info to register and search books from the library
def get_book_info() -> Book:
    print("Please fill the next form to add a new book.")
    title = input("Title: ")
    author = input("Author's name: ")
    isbn = input("ISBN: ")

    if not title or not author or not isbn:
        raise ValueError("Title, author and ISBN are required.")

    is_available = input("Is available? [y/n] (default yes): ")

    if is_available and (is_available.lower() != "y" or is_available.lower() != "n"):
        raise ValueError(f"y or n excepcted, got {is_available}")

    is_available = False if is_available.lower() == "n" else True

    book = Book(title, author, isbn, is_available)
    return book


def find_book(library: Library) -> Book:
    print("\nPlease tell us what book you are looking for.\n")
    title = input("Book's title: ")
    isbn = None
    if not title:
        isbn = input("Book's isbn: ")

    book = library.search_book(title, isbn)
    return book


def main():
    # Create and fill the library
    # library = Library("The Fantastic Book Store", "123 Best Av.")
    # fill_library(library, users_data, books_data)
    persistence = Persistence()
    library = persistence.load()  # Load data from JSON file

    print(f"Welcome to {library.name}")

    ## TODO: Code options' functionality
    while True:
        print("\n")
        opt = menu()
        print()

        if opt == 1:  # register users
            try:
                user = get_user_info()
                library.register_user(user)
                print("==" * 15)
                print(
                    f"\nUser {user.name} has successfully registered with and id: {user.user_id}"
                )
            except ValueError as e:
                print("⚠️", e)
        elif opt == 2:  # Add books
            try:
                book = get_book_info()
                library.add_book(book)
                print("==" * 15)
                print(f"Book '{book.title}' has successfully added into the library.")
            except ValueError as e:
                print("⚠️", e)
        elif opt == 3:  # Find a user
            print("Entró a la opción 3")
            try:
                user = find_user(library)
                print("==" * 15)
                print(user)
            except NotFoundUserError as e:
                print("⚠️", e)
        elif opt == 4:  # Find a book
            try:
                book = find_book(library)
                print("==" * 15)
                print(book)
            except BookNotAvailableError as e:
                print("⚠️", e)
            except ValueError:
                print("Pleae write the book's title or isbn.")
        elif opt == 5:  # loan a book
            try:
                # Encontrar al usuario
                user = find_user(library)
                # listar los libros disponibles
                print("Available Books:")
                for book in library.get_available_books():
                    print(f"  - {book.title} (isbn: {book.isbn})")
                # buscar libro (selección de libro)
                book = find_book(library)
                # prestar libro
                result = user.borrow_book(book)
                print(result)
                print(user)
                print(book)
            except NotFoundUserError as e:
                print("⚠️", e)
            except BookNotAvailableError as e:
                print("⚠️", e)
            except BorrowBookError as e:
                print(e)
            except ValueError:
                print("Pleae write the book's title or isbn.")
        elif opt == 6:
            user_id = input("User ID: ")
            try:
                user = library.search_user(user_id)
                if len(user.borrowed_books) > 0:
                    print(f"{user.name} has the following borrowed books:")
                    for idx, book in enumerate(user.borrowed_books):
                        print(f"    {idx + 1} → {book.title} (isbn: {book.isbn})")

                    idx = int(input("Select the book's number you want to return: "))
                else:
                    print(f"{user.name} does not have any borrowed book yet.")
            except NotFoundUserError as e:
                print("⚠️", e)
            except BorrowBookError as e:
                print(e)
            except ValueError:
                print(f"Accepted options: 1 - {len(user.borrowed_books)}, got {idx}")
        elif opt == 7:
            if len(library.get_available_books()) > 0:
                print("Available books:")
                for book in library.get_available_books():
                    print(f"  - {book.title} (isbn: {book.isbn})")
            else:
                print("Sorry!, There are not available books.")
        elif opt == 8:
            if len(library.get_popular_books()) > 0:
                print("Most popular books:")
                for book in library.get_popular_books():
                    print(f"  - {book.title} (isbn: {book.isbn})")
            else:
                print("Sorry!, There are not popular books yet.")
        elif opt == 9:
            persistence = Persistence()
            persistence.save(library)
            print("Thans for visiting us, we hope to see you soon...")
            break


if __name__ == "__main__":
    main()
