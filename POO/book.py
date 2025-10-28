class Book:
    def __init__(self, title: str, author: str, isbn: str, is_available: bool = True) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.is_available: bool = is_available
        self.__loan_times: int = 0
    
    def __str__(self) -> str:
        msj = "This title is" + ("" if self.is_available else " not") + " available"
        return f"Book: {self.title} \nAuthor: {self.author}. \n{msj}."

    @property
    def loan_times(self) -> int:
        return self.__loan_times
    
    @loan_times.setter
    def loan_times(self, times: int) -> None:
        self.__loan_times = times
    
    def loan(self) -> None:
        if self.is_available:
            self.is_available = False
            self.loan_times += 1
        else:
            raise ValueError("Sorry this book is not available.")
    
    def recive_book(self) -> None:
        if not self.is_available:
            self.is_available = True
        else:
            raise ValueError("Sorry this book has already returned.")

    def is_popular(self) -> bool:
        return self.loan_times > 5

def loan_book_similator(book: Book, borrow_times: int) -> None:
    for _ in range(borrow_times):
        if not book.is_available:
            book.recive_book()        
        book.loan()

if __name__ == "__main__":
    try:
        books = {
            "book1": Book("Harry Potter y la Piedra Filosofal", "JK Rowling", "123456789"),
            "book2": Book("22/11/63", "Stephen King", "789456123"),
            "book3": Book("El Problema de los Tres Cuerpos", "Cixin Liu", "456123789", False),
        }

        for (name, book) in books.items():
            print(book, "\n")
        
        # Simular prestamo de libros:
        loan_book_similator(books["book1"], 6)
        loan_book_similator(books["book3"], 3)
        
        print(f"{books["book1"].title} is", ("" if books["book1"].is_popular() else "not") ,"popular.")
        print(f"{books["book3"].title} is", ("" if books["book3"].is_popular() else "not") ,"popular.")
    except ValueError as e:
        print(e)