
import json

try:
    with open("library.txt", "r") as file:
        library = json.load(file)
except:
    library = []

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    print("Book added successfully!")

def remove_book():
    title = input("Enter title to remove: ")
    global library
    library = [book for book in library if book["title"] != title]
    print("Book removed!")

def search_book():
    option = input("Search by title or author? ").lower()
    query = input("Enter search term: ").lower()
    for book in library:
        if query in book[option].lower():
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_all():
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def stats():
    total = len(library)
    read_count = sum(book['read'] for book in library)
    print(f"Total books: {total}\nRead: {read_count} ({(read_count / total * 100) if total > 0 else 0:.2f}%)")

while True:
    print("""
    Welcome to Library Manager:
    1. Add book
    2. Remove book
    3. Search
    4. Display all
    5. Statistics
    6. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1": add_book()
    elif choice == "2": remove_book()
    elif choice == "3": search_book()
    elif choice == "4": display_all()
    elif choice == "5": stats()
    elif choice == "6": save_library(); print("Saved. Goodbye!"); break
    else: print("Invalid choice")



