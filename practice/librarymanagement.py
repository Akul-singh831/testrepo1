class LibraryManagement:
    def __init__(self, libraryname, title, author, pages, price):
        self.libraryname = libraryname
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def get_libraryname(self):
        return self.libraryname

    def set_libraryname(self, libraryname):
        self.libraryname = libraryname

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price 
        
        
lib1 = LibraryManagement("Astin", "Behold Till Eternity", "Alexis", 269, 699)
lib2 = LibraryManagement("martin", "", "Alexis", 269, 699)

print(lib1.get_title())
print(lib1.get_title())
print(lib1.get_title())
print(lib1.get_title())

