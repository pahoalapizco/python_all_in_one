import json
from datetime import datetime
from library import Library
from book import Book
from users import Student, Professor


class Persistence:
    """Saves and loads library's instance."""

    def __init__(self, file="data.json"):
        self.file = file

    def save(self, library: Library) -> None:
        """Save a whole library (including books and users) into a json file.

        Args:
            library (Library): Library's instance to save into a json file.
        """
        data = {
            "name": library.name,
            "address": library.address,
            "books": [book.__dict__ for book in library.books],
            "users": [
                {user.__class__.__name__: user.__dict__} for user in library.users
            ],
            "saved_at": datetime.now().isoformat(),
        }

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
                default=lambda obj: obj.__dict__,
            )

    def load(self) -> Library:
        """Takes a JSON file with library's info that had been saved before and rebuilds it.

        Returns:
            Library: Rebuilt library from a JSON file
        """
        with open(self.file, "r", encoding="utf-8") as file:
            data = json.load(file)

            books: dict[Book] = dict()
            library = Library(data["name"], data["address"])

            for data_book in data["books"]:
                book = Book.from_dict(data_book)
                library.add_book(book)
                books[data_book["_Book__UUID"]] = book

            for data_user in data["users"]:
                user_type, user_info = list(data_user.items())[0]
                book_list = []
                user = None

                if len(user_info["_User__borrowed_books"]) > 0:
                    book_list = [
                        books[borrowed_book["_Book__UUID"]]
                        for borrowed_book in user_info["_User__borrowed_books"]
                    ]

                if user_type == Professor.__name__:
                    user = Professor.from_dict(user_info, book_list)
                elif user_type == Student.__name__:
                    user = Student.from_dict(user_info, book_list)

                if user:
                    library.register_user(user)

        return library


if __name__ == "__main__":
    p = Persistence()
    library = p.load()
    print(library)
