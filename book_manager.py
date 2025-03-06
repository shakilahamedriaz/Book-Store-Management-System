import json
from book import Book
from file_handler import load_books, save_books

class BookManager:
    def __init__(self):
        self.books = load_books()

    def add_book(self, title, author, isbn, genre, price, quantity):
        if isbn in self.books:
            print("Error: A book with this ISBN already exists.")
            return
        
        if not isinstance(price, (int, float)) or price < 0:
            print("Error: Price must be a positive number.")
            return
        
        if not isinstance(quantity, int) or quantity < 0:
            print("Error: Quantity must be a non-negative integer.")
            return
        
        new_book = Book(title, author, isbn, genre, price, quantity)
        self.books[isbn] = new_book.to_dict()
        save_books(self.books)
        print("Book added successfully!")



    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(f"{book['title']} by {book['author']} - {book['genre']}, ${book['price']} (Stock: {book['quantity']})")

    def search_book(self, keyword):
        found = [book for book in self.books.values() if keyword.lower() in book['title'].lower()]
        if found:
            for book in found:
                print(f"{book['title']} by {book['author']} - {book['genre']}, ${book['price']} (Stock: {book['quantity']})")
        else:
            print("No books found.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            save_books(self.books)
            print("Book removed successfully!")
        else:
            print("Error: No book found with this ISBN.")
