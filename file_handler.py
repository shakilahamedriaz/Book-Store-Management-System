import json
import os

FILE_PATH = "books.json"

def load_books():
    #load book from json file
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, 'r') as file:
        return json.load(file)
    


def save_books(books):
    #save books to JSON file
    with open(FILE_PATH, 'w') as file:
        json.dump(books, file, indent=4)