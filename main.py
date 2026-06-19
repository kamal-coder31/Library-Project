from book import Book
from library import Library

lib = Library()

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book ("The A1chemist", "Pualo Coelho")

lib.add_book(book1)
lib.add_book(book2)

lib.show_books()