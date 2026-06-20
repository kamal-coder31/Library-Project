class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self,book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def show_user_books(self):
      if len(self.borrowed_books)==0:
          print("no books borrowed")
      else:
          for book in self.borrowed_books:
              print(book.title, "-", book.author)
