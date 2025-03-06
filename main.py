from book_manager import BookManager

def main():
    manager = BookManager()

    while True:
        print("--------------------------")
        print("| Book Store Management  |")
        print("--------------------------")
        print("\n1. Add Book")
        print("2. View Book")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit now")

        choice = input("\nEnter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter Author name: ")
            isbn = input("Enter ISBN no: ")
            genre = input("Enter genre: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            #add this information to book_manager/add_books()
            manager.add_book(title, author, isbn, genre, price, quantity)
        
        elif choice == "2":
            manager.view_books()
        
        elif choice == "3":
            keyword = input("Enter book title keyword: ")
            manager.search_book(keyword)
        
        elif choice == "4":
            isbn = input("Enter ISBN to remove book: ")
            manager.remove_book(isbn)
        
        elif choice == "5":
            print("Exiting ....")
            break

        else:
            print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()
            