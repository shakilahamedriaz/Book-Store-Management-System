## Book Store Management System (CLI based)📚

## Overview
This is a **Command Line Interface (CLI) Book Store Management System** built with Python. The project allows users to **add, view, search, and remove books** from a store while maintaining book records in a file for persistence. The system ensures that no duplicate ISBNs are allowed and provides user-friendly error handling.

## Features
- **Add Books:** Users can add books with details such as title, author, ISBN, genre, price, and quantity.
- **Prevent Duplicate Books:** Ensures each book has a unique ISBN or Book ID.
- **View Books:** Displays all books in a well-organized format.
- **Save to File:** Stores book data in a JSON file for persistence.
- **Load from File:** Loads previously saved book data when the program starts.
- **Search Books:** Allows searching for books by title, author, or ISBN.
- **Remove Books:** Users can delete books by ISBN or Book ID.
- **Error Handling:** Provides meaningful error messages for invalid inputs.
- **Interactive Menu:** A simple CLI menu for easy navigation.

## Technologies Used
- **Python (Standard Library only)**
- **File Handling (JSON format)**

## Project Structure
```
📂 Book-Store-Management-System
│
├── 📂 Design Plan/
│   ├── 📄 plan_and_design.pdf       # Detailed plan and design documentation
│   ├── 📄 use_case_diagram.png      # Visual representation of use cases
│   ├── 📄 uml_diagram.png          # UML diagram illustrating class relationships
│   └── 📄 visual_representation.png # Additional visual representations
│
├── 📄 book.py                       # Contains the definition and management of book objects
├── 📄 book_manager.py               # Handles operations related to managing books
├── 📄 books.json                   # JSON file storing the book inventory data
├── 📄 file_handler.py              # Utility functions for handling file operations
└── 📄 main.py                      # Main entry point of the application
```

## Installation and Usage
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/BookStoreManagementSystem.git
   cd BookStoreManagementSystem
   ```
2. **Run the Program**
   ```bash
   python main.py
   ```
3. **Follow the On-Screen Menu Instructions**

## How It Works
1. **Start the Program** → Loads existing book data from `books.json`.
2. **Main Menu Options:**
   - Add a new book.
   - View all books.
   - Search for a book by title, author, or ISBN.
   - Remove a book using ISBN.
   - Exit the program (saves changes before closing).
3. **Exit the Program** → Saves all data before exiting.

## Error Handling
- Validates inputs to ensure data integrity (e.g., positive price values, unique ISBNs, non-negative stock quantities).
- Displays clear error messages to guide the user.

## Future Improvements
- Implement book stock updates.
- Allow filtering books by genre or price range.
- Improve the search functionality with multiple criteria.
- Add an option to export book records to CSV.

##License
Copyright (c) 2023 Shakil Ahamed Riaz

---
Feel free to contribute or suggest improvements!
