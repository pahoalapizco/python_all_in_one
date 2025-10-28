from typing import Optional
from book import Book
from student import Student
from professor import Professor

def borrow_books_simulator(user: Optional[Professor | Student], books: list[Book]) -> None:
    for book in books:
        print(user.borrow_book(book))

def returning_simulator(user: Optional[Professor | Student], book: Book) -> None:
    print(user.returning_book(book))

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
    
    prof = Professor("Luis Martínez", "P-123456", "Sitemas")
    student = Student("Paola Alapizco", "S-951753", "Sistemas")
    
    book_list = [book for _, book in books.items()]
    
    # print(book_list[:4])
    borrow_books_simulator(prof, book_list)
    
    # Simulador de retorno de libros
    returning_simulator(prof, books["book1"])
    borrow_books_simulator(student, [book_list[0]])