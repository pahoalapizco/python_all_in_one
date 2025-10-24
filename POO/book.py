class Book:    
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = False) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available



if __name__ == "__main__":
    books = {
        "book1": Book("Harry Potter y la Piedra Filosofal", "JK Rowling", "123456789"),
        "book2": Book("22/11/63", "Stephen King", "789456123"),
        "book3": Book("El Problema de los Tres Cuerpos", "Cixin Liu", "456123789", True),
    }

    for (name, book) in books.items():
        print(f" {name} ".center(15, "="))
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        msj = "This title is" + ("" if book.is_available else " not") + " available"
        print(msj)