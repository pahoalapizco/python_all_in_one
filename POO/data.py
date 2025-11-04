from book import Book
from users import Student, Professor


books_data: list[Book] = [
    # Fantasy, Fictions
    Book("Harry Potter y la Piedra Filosofal", "JK Rowling", "123456789"),
    Book("22/11/63", "Stephen King", "789456123"),
    Book("El Problema de los Tres Cuerpos", "Cixin Liu", "456123789"),
    # Science
    Book("Deep Learning", "Jhon D. Keller", "15478932"),
    Book("Why Machines Learn", "Anil Ananthaswamy", "7854123694"),
    Book("Naked Statistics", "Charles Wheelan", "1597536548", False)
]

users_data: list[Student | Professor] = [
    Professor("Luis Martínez", "P123456", "Sitemas"),
    Professor("Ana Camacho", "P183456", "Industrial"),
    Professor("Helena Romance", "P623456", "Humanidades"),
    Student("Paola Alapizco", "S951753", "Ing. Sistemas Computacionales"),
    Student("Jr Peréz", "S951753", "Ing. Industrial"),
    Student("María Soto", "S951524", "Antropología e Historia"),
    Student("Tomás Esquibel", "S964153", "Ing. Sistemas Computacionales"),
]

if __name__ == "__main__":
    pass