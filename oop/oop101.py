# Abstraction : Soyut özellik taşıma
# Inheritence: Kalıtım. Objeler arasında miras
# Polymorphism: Çok biçimlilik
# Pythonda bütün classalr Object class'ından miras alırlar.

class Library:
    # init constructor
    def __init__(self, name, adress):
        # attribute
        self.name = name
        self.address = adress
        self.__books: list = [] # gizli özellik
    
    def add_book(self,b):
        self.__books.append(b)
        
    def remove_book(self,isbn:str):
        for ind,val in enumerate(self.__books):
            if val.isbn == isbn:
                self.__books.pop(ind)


class Book:
    def __init__(self, name, isbn, author, year):
        self.name: str = name
        self.isbn: str = isbn
        self.author: str = author
        self.year: int = year
        
    # magic functions +, - .. operators are magic functions
    def __str__(self):
        return "{} by {}, {}".format(self.name, self.author, self.year)


x = Library("Atatürk Kütüphanesi", "test adress")
# x.name = "Merkez kütüphane"
# print(x.name)

'''
x.books.append(Book("körlük", "121313", "Yazar 1", 2012))
b: Book = Book("körlük2", "121313", "Yazar 2", 2012)
x.books.append(b)
'''
