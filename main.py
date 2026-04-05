import sqlite3

# Connect DB
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    available INTEGER
)
""")
conn.commit()

# FUNCTIONS (must be ABOVE menu)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    cursor.execute(
        "INSERT INTO books (title, author, available) VALUES (?, ?, 1)",
        (title, author)
    )
    conn.commit()
    print("Book added!")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        status = "Available" if book[3] == 1 else "Issued"
        print(f"{book[0]} | {book[1]} | {book[2]} | {status}")

def issue_book():
    book_id = int(input("Enter book ID to issue: "))
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    conn.commit()
    print("Book issued!")

def return_book():
    book_id = int(input("Enter book ID to return: "))
    cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
    conn.commit()
    print("Book returned!")

import sqlite3

# Connect DB
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    available INTEGER
)
""")
conn.commit()

# FUNCTIONS (must be ABOVE menu)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    cursor.execute(
        "INSERT INTO books (title, author, available) VALUES (?, ?, 1)",
        (title, author)
    )
    conn.commit()
    print("Book added!")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        status = "Available" if book[3] == 1 else "Issued"
        print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")

def issue_book():
    book_id = int(input("Enter book ID to issue: "))
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    conn.commit()
    print("Book issued!")

def return_book():
    book_id = int(input("Enter book ID to return: "))
    cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
    conn.commit()
    print("Book returned!")

# MAIN MENU (must be LAST)

while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

def search_book():
    keyword = input("Enter book title to search: ")

    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()

    for book in results:
        status = "Available" if book[3] == 1 else "Issued"
        print(f"{book[0]} | {book[1]} | {book[2]} | {status}")

def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

    print("Book deleted!")

# MAIN MENU (must be LAST)

while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        break
    else:
        print("Invalid choice")