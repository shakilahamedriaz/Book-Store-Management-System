import json
from book import Book


class BookManager:
    def __init__(self):
        self.books = load.books()
    
    def add_books(self, title, author, isbn, genre, price, quantity):
        if isbn in self.books:
            print("Error: A book with this ISBN/BOOKID already exist.Please enter a new book data!")
            return

        new_book = Book(title, author, isbn, genre, price, quantity)
        self.books[isbn] = new_book.to_dict()
        save_books(self.books)
        print("Book added successfully!\nThank you..")


    def view_books(self):
        if not self.books:
            print("No books available right now here!")

            for book in self.books.values():
                print(f"Book Name: {book['title']} Auther: {book['author']} - {book['genre']}, ${book['price']} (Stock: {book['quantity']})")
        
        else:
            print("No books fund in the book list.")
    


    def search_book(self, keyword):
        found = [book for book in self.books.values() if keyword.lower() in book['title'].lower()]
        if found:
            print(f"Book Name: {book['title']} Auther: {book['author']} - {book['genre']}, ${book['price']} (Stock: {book['quantity']})")
        else:
            print("No books found with this keyword")
    


    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            save_books(self.books)
            print("Book removed successfully!")
        else:
            print("No book found here with is ISBN/BOOKID.")
        