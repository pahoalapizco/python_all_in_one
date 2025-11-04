from book import Book
from users import Student, Professor
from exeptions import NotFoundUserError


class Library:
    def __init__(self, name: str, address: str):
        self.name: str = name
        self.address: str = address
        self.__users: list[Student | Professor] = []
        self.__books: list[Book] = []
    
    def __str__(self):
        return f"Library: {self.name} \nTotal registered users: {len(self.__users)} \nTotal books: {len(self.__books)}"
    
    # ====== PROPERTIES ======
    @property
    def books(self) -> list[Book]:
        """List of all added books in the library"""
        return self.__books
    
    @property
    def users(self) -> list[Student | Professor]:
        """List of all registered users in the library"""
        return self.__users
    
    
    # ====== USERS ====== 
    def register_user(self, user: Student | Professor) -> None:
        """
        Add a new user object into __users array.        

        Args:
            user (User): Instance of a User
        """
        self.__users.append(user)
    
    def search_user(self, user_id: str) -> Student | Professor:
        for user in self.users():
            if user.ID == user_id:
                return user
        raise NotFoundUserError(f"User with ID {user_id} has not found.")
    
    # ====== BOOKS ====== 
    def add_book(self, book: Book) -> None:
        """
        Adds a new book object into __books array.
        
        Args:
            book (Book): Instance of a Book
        """
        self.__books.append(book)
    
    def get_available_books(self) -> list[Book]:
        """ 
        Get just the available books in the array __books
        
        Returns:
            list[Book]: List of available books.
        """
        available_books = [
            book for book in self.__books
            if book.is_available
        ]
        return available_books

    def get_popular_books(self) -> list[Book]:
        """
        Get the most popular books.

        Returns:
            list[Book]: List of books considered the most popular.
        """
        most_popular = [
            book for book
            in self.__books
            if book.is_popular()
        ]
        return most_popular

if __name__ == "__main__":
    pass 