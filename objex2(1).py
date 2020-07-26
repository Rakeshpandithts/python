class Book(object):
    def __init__(self):
        self.Title = input("Title: ")
        self.Author = input("Author: ")
        self.pages = input("No. of Pages: ")
        self.yearofpub = input("year of publish: ")
        self.price = input("No. of price: ")

    def bookReadingDetails(self):
        self.pagesRead = input("No. of pages read: ")
        self.readingSpeed = input("Reading Speed: ")
    

book1 = Book()
book1.bookReadingDetails()
