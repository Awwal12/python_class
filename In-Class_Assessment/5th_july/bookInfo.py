# QUESTION:

# Create a program that reads a text file containing information about a group of books. Each line of the file should contain the book's title, author, and ISBN, separated by commas. Your program should create a Book class with attributes for title, author, and ISBN, and a method for displaying the book's information. The program should then read the file, create a Book object for each book, and store the objects in a list. Finally, the program should print the list of books to the console.

# Example input file (books.txt):

# The Great Gatsby, F. Scott Fitzgerald, 9780521599879
# To Kill a Mockingbird, Harper Lee, 9780446310789
# 1984, George Orwell, 9780451524935
# Animal Farm, George Orwell, 9780451526342


# Example output:

# The Great Gatsby by F. Scott Fitzgerald (ISBN: 9780521599879)
# To Kill a Mockingbird by Harper Lee (ISBN: 9780446310789)
# 1984 by George Orwell (ISBN: 9780451524935)
# Animal Farm by George Orwell (ISBN: 9780451526342)
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.isbn = ISBN

    def displayBook(self):
        books = []
        with open("books.txt", "r+") as f:
            booklets = f.readlines()
        for book in booklets:
            books.append(Book(book.split(',')[0], book.split(',')[1].strip(
                ' '), int(book.split(',')[2].strip(' ').strip('\n'))))
        return books
