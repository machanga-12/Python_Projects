
# Library Management System

A simple Python-based Library Management System that allows users to browse a collection of books, add new books, borrow (remove) books, return books, search for books, view available books, and sort the library catalog by various fields.

## Features

- **Browse Library Catalog**: View a list of all books in the library.
- **Add a Book**: Add a new book to the library with details like title, author, year, genre, and availability status.
- **Remove (Borrow) a Book**: Mark a book as borrowed, changing its availability status to "not available."
- **Return a Book**: Mark a borrowed book as returned, making it available for others to borrow.
- **Search for a Book by Title**: Search for a specific book in the library by its title.
- **View Available Books**: View a list of books that are currently available to borrow.
- **Sort Library Catalog**: Sort the library collection by title, author, year, or genre.

## Installation

1. **Clone the repository** or **download the project files**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the project directory**:
   ```bash
   cd library-management-system
   ```
3. **Open the project in PyCharm or your preferred IDE**.

## Usage

1. **Run the `library_system.py` file** to start the library management system:
   ```bash
   python library_system.py
   ```
2. **Choose from the menu** to perform different operations:
   - **Option 1**: Browse the library catalog.
   - **Option 2**: Add a new book to the library.
   - **Option 3**: Borrow (remove) a book from the library.
   - **Option 4**: Return a borrowed book.
   - **Option 5**: Search for a book by title.
   - **Option 6**: View all available books.
   - **Option 7**: Sort the library catalog by title, author, year, or genre.
   - **Type `exit`** to exit the program.

## Example Commands

- **Browse Library**: View all books in the library.
- **Add a Book**: Provide book details like title, author, year, and genre.
- **Borrow a Book**: Provide the title of the book you want to borrow.
- **Return a Book**: Provide the title of the book you are returning.
- **Search for a Book**: Provide the title of the book to search for.
- **Sort Library**: Choose from sorting options (title, author, year, or genre).

## Code Overview

The main functionalities are encapsulated in the following functions:

- `library_menu()`: Displays the menu options and handles user input.
- `library()`: Displays a full list of books in the library.
- `add_book()`: Allows users to add a new book to the library.
- `remove_book()`: Allows users to borrow a book from the library, marking it as not available.
- `return_book()`: Allows users to return a previously borrowed book.
- `search_book()`: Searches for a book by its title.
- `view_available_books()`: Lists only the books that are available to borrow.
- `sort_library()`: Allows sorting of the library by title, author, year, or genre.
- `management_system()`: Initiates the library menu and runs the system.

## Requirements

- Python 3.x

## Contributing

Feel free to submit issues or create pull requests if you have suggestions or improvements. This project is designed to be beginner-friendly, so contributions are welcome!

## License

This project is open-source and available under the MIT License.

## Acknowledgements

This project is a simple implementation designed to help beginners understand the basic concepts of Python, including working with lists, dictionaries, loops, and functions. It also introduces basic object-oriented design principles.
