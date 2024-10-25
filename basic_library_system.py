#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# List of books with detailed information stored as dictionaries
library_list = [
    {"title": "Python For All", "author": "Steve March", "year": 2020, "genre": "Fiction", "available": True},
    {"title": "Introduction to Python", "author": "Antony Cranty", "year": 2019, "genre": "Science", "available": True},
    {"title": "Hello World", "author": "Kana Joy", "year": 2021, "genre": "Fantasy", "available": True}
]


def library_menu():
    print('Choose one of the options below:')
    print('1 to browse library catalog')
    print('2 to add a book')
    print('3 to remove (borrow) a book')
    print('4 to return a book')
    print('5 to search for a book by title')
    print('6 to view available books')
    print('7 to sort library catalog')
    print('exit to exit')

    while True:
        user_input = input('Enter your option: ')
        if user_input == '1':
            library()
        elif user_input == '2':
            add_book()
        elif user_input == '3':
            remove_book()
        elif user_input == '4':
            return_book()
        elif user_input == '5':
            search_book()
        elif user_input == '6':
            view_available_books()
        elif user_input == '7':
            sort_library()
        elif user_input.lower() == 'exit':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid input! Please choose a correct option.")


def library():
    print('Here is the full list of our library:')
    for book in library_list:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, "
              f"Available: {'Yes' if book['available'] else 'No'}")


def add_book():
    user_input = input('Do you want to add a book? (yes/no): ')
    if user_input.lower() == 'yes':
        title = input('What is the title of the book? ')
        author = input('Who is the author of the book? ')
        year = int(input('What is the year of publication? '))
        genre = input('What is the genre of the book? ')
        library_list.append({"title": title, "author": author, "year": year, "genre": genre, "available": True})
        print("The book has been added to the library.")
        library()


def remove_book():
    title = input('Enter the title of the book you want to borrow: ')
    for book in library_list:
        if book['title'].lower() == title.lower():
            if book['available']:
                book['available'] = False
                print(f"You have borrowed '{title}'. Enjoy reading!")
            else:
                print(f"Sorry, '{title}' is currently not available.")
            break
    else:
        print("The book you requested is not available in the library.")


def return_book():
    title = input('Enter the title of the book you want to return: ')
    for book in library_list:
        if book['title'].lower() == title.lower() and not book['available']:
            book['available'] = True
            print(f"Thank you for returning '{title}'.")
            break
    else:
        print(f"'{title}' is not currently borrowed or does not exist in the library.")


def search_book():
    title = input('Enter the title of the book you want to search for: ')
    for book in library_list:
        if book['title'].lower() == title.lower():
            print(f"Found: Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, "
                  f"Genre: {book['genre']}, Available: {'Yes' if book['available'] else 'No'}")
            break
    else:
        print(f"'{title}' is not available in the library.")


def view_available_books():
    print('Here is the list of all available books:')
    for book in library_list:
        if book['available']:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}")


def sort_library():
    print('Choose a field to sort by:')
    print('1 for Title')
    print('2 for Author')
    print('3 for Year')
    print('4 for Genre')

    user_input = input('Enter your choice: ')
    if user_input == '1':
        sorted_books = sorted(library_list, key=lambda x: x['title'].lower())
    elif user_input == '2':
        sorted_books = sorted(library_list, key=lambda x: x['author'].lower())
    elif user_input == '3':
        sorted_books = sorted(library_list, key=lambda x: x['year'])
    elif user_input == '4':
        sorted_books = sorted(library_list, key=lambda x: x['genre'].lower())
    else:
        print("Invalid input!")
        return

    print('Here is the sorted library list:')
    for book in sorted_books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, "
              f"Available: {'Yes' if book['available'] else 'No'}")


def management_system():
    library_menu()


management_system()


# In[ ]:




