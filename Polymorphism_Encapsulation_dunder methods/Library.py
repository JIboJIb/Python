# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books
# list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
class Author:

    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"Autors data:\n" \
               f"Name {self.name}, country: {self.country}, birthday: {self.birthday} \n" \
               f"books: {self.books}"

    def __repr__(self):
        return self.__str__()


class Book(Author):
    amount_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.amount_books += 1

    def __str__(self):
        return f"Name of the book: {self.name}, year: {self.year}" \
               f"Author: {self.author.name} / {self.author.country} / {self.author.birthday}."

    def __repr__(self):
        return self.__str__()


class Library(Book):

    def __init__(self):
        self.all_books = []

    def new_book(self, book):
        self.all_books.append({"name": book.name, "year": book.year, "author": book.author.name})

    def group_by_author(self, author):
        count = 0
        for book in self.all_books:
            if author.name == book["author"]:
                print(f"{book['name']} ({book['year']})")
                print()
                count += 1
        if count == 0:
            print("Nothing found")

    def group_by_year(self, year):
        count = 0
        for book in self.all_books:
            if year == book["year"]:
                print(f"{book['name']} ({book['year']})")
                print()
                count += 1
        if count == 0:
            print(f"Nothing found in this year {year}")

    def __str__(self):
        return f"We have {Book.amount_books} books"

    def __repr__(self):
        return self.__str__()

our_library = Library()


author_1 = Author('Isaac Asimov', 'USA', '02.01.1920', [])
author_2 = Author('Terry Pratchett', 'Great Britain', '28.04.1948', [])
author_3 = Author('J. R. R. Tolkien', 'Great Britain', '03.01.1892', [])


book_1 = Book('The Bicentennial Man', '1976', author_1)
book_2 = Book('The End of Eternity', '1955', author_1)
book_3 = Book('I, robot', '1950', author_1)
book_4 = Book('Good Omens', '1990', author_2)
book_5 = Book('The Light Fantastic', '1986', author_2)
book_6 = Book('Mort', '1987', author_2)
book_7 = Book('The Fellowship of the Ring', '1954', author_3)
book_8 = Book('The Two Towers', '1954', author_3)
book_9 = Book('The Return of the King', '1955', author_3)


our_library.new_book(book_1)
our_library.new_book(book_2)
our_library.new_book(book_3)
our_library.new_book(book_4)
our_library.new_book(book_5)
our_library.new_book(book_6)
our_library.new_book(book_7)
our_library.new_book(book_8)
our_library.new_book(book_9)


our_library.group_by_author(author_1)
our_library.group_by_author(author_2)
our_library.group_by_author(author_3)


our_library.group_by_year('1954')
our_library.group_by_year('1955')


print(our_library.__str__())
