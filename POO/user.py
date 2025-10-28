from book import Book

class User():
    def __init__(self, name: str, ID: str) -> None:
        self.name = name
        self.ID = ID
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> str:
        try:
            book.loan()
            self.borrowed_books.append(book)
            return f"Autorized loan of book '{book.title}'."
        except ValueError as e:
            return e

    def returning_book(self, book: Book) -> str:
        if len(self.borrowed_books) == 0:
            return "You have not borroed any book yet."
        else:
            try:
                idx = self.borrowed_books.index(book)
                book.recive_book()
                self.borrowed_books.pop(idx)
                return f"Book '{book.title}' returned sucessfully."
            except ValueError as e:
                return e


if __name__ == "__main__":
    pass