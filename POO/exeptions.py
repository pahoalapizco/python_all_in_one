class LibraryError(Exception):
    pass

class BookNotAvailableError(LibraryError):
    pass

class ReturnedBookError(LibraryError):
    pass