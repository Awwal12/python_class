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
# class Book:

#     def displayBook(self):
#         books = []
#         with open("books.txt", "r+") as f:
#             booklets = f.readlines()
#         for book in booklets:
#             books.append([book.split(',')[0], book.split(',')[1].strip(
#                 ' '), int(book.split(',')[2].strip(' ').strip('\n'))])
#         return books

#     def printBook(self):
#         books = self.displayBook()

#         for book in books:
#             print(f"{book[0]} by {book[1]} (ISBN: {book[2]})")
#             # print(book)


# lib1 = Book()
# lib1.printBook()
class Book:
    """class describing a book
    """

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def print_book(self):
        """_summary_

        :return: _description_
        """
        return f'{self.title} by {self.author} (isbn: {self.isbn})'


booklets = []
with open("books.txt", 'r+', encoding=str) as f:
    result = f.readlines()
    for book in result:
        spilt_result = book.split(',')
        title = spilt_result[0]
        author = spilt_result[1].strip(' ')
        isbn = spilt_result[2].strip(' ').strip('\n')
        booklets.append(Book(title, author, isbn))

print(booklets)
