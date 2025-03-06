#Bismillahhir Rahmanir Rahim
class Book:
    def __init__(self, title, author, isbn, genre, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn  # # unique value, we cannot assign multiple book as same isbn/book_id
        self.genre = genre
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        #Convert book object to dictionary format for saving in JSON
        return self.__dict__

    @staticmethod
    def from_dict(data):
        #Create a Book instance from dictionary data
        return Book(**data)
