import os


class Library(object):
    def __init__(self):
        self.books = []
        print("LIBRARY HAS BEEN CREATED.")

    def __str__(self):
        """Returns a string representation of the library."""
        return "There are {} books in the library.".format(len(self.books))

    def add_book(self, book):
        """Adds a book to the library"""
        self.books.append(book)

    def print_books(self):
        """Prints books"""
        for book in self.books:
            print("Title: {}\
                \nAuthor: {}\
                \nYear: {}\
                \nGenre: {}\
                \nRating: {}\
                \nISBN: {}\
                \n\n".format(book.title,
                             book.author,
                             book.year,
                             book.genre,
                             book.rating,
                             book.isbn))

    def save_books(self):
        file = open('lib.txt', "a+")

        if len(self.books) == 0:
            print("There's nothing to write to file.")
        else:
            i = 1
            for book in self.books:
                file.write("{}: Title: {} Author: {} Year: {} Genre: {} Rating: {} ISBN: {}\n".format(i,
                                                                                                      book.title,
                                                                                                      book.author,
                                                                                                      book.year,
                                                                                                      book.genre,
                                                                                                      book.rating,
                                                                                                      book.isbn))

                i += 1


class Book(object):
    def __init__(self):

        # ASK FOR TITLE
        self.title = input("Please enter a title: ")
        if len(self.title) == 0:
            i = 0
            while True:
                if i == 3:
                    raise SystemExit("No information was entered repeatedly, now exiting.")
                if len(self.title) == 0:
                    print("No data was entered.")
                    self.title = input("Please enter a title: ")
                    i += 1
        else:
            print("Thanks for entering \"{}\" as a title.\n".format(self.title))

        # ASK FOR AUTHOR
        self.author = input("Who wrote {}: ".format(self.title))
        # if the length of self.author is 0 it is assigned a N/A value.
        if len(self.author) == 0:
            self.author = "N/A"

        self.year = input("What year was {} by {} written: ".format(self.title,
                                                                    self.author))
        try:
            self.year = int(self.year)
        except TypeError:
            self.year = "N/A"

        if self.author == "N/A":
            self.genre = input("Please enter a genre for {}: ".format(self.title))
        else:
            self.genre = input("Please enter a genre for {} by {}: ".format(self.title,
                                                                            self.author))

        self.isbn = input("What's the ISBN: ")
        if len(self.isbn) == 0:
            self.isbn = "N/A"

        self.rating = input("What have you rated {} by {} (out of 10): ".format(self.title,
                                                                                self.author))
        try:
            self.rating = float(self.rating)
            if self.rating > 10:
                self.rating = 0
                print("Your rating was greater than 10 we've assigned a null value to it. ")
        except:
            self.rating = 0

    def __str__(self):
        """Returns a string object representation of the book object"""
        return "{} ({}) by {} belongs to the {} genre and was rated {}/10. It's ISBN is: {}.".format(self.title,
                                                                                                     self.year,
                                                                                                     self.author,                                                                                             self.genre,
                                                                                                     self.rating,
                                                                                                     self.isbn)
