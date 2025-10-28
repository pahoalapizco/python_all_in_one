from user import User

# Professor
class Professor(User):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.limit_books = None

    def borrow_book(self, book):
        return super().borrow_book(book)


if __name__ == "__main__":
    pass