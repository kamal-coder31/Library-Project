class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self , book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)
        
    def save_books(self):
       
            with open ("books.text", "w") as file:
                 for book in self.books:
                  file.write(book.title + "," + book.author + "\n")

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    title, author = line.strip().split(",")

                    self.books.append(self.books(title, author))
        except FileNotFoundError:
         self.books = []
