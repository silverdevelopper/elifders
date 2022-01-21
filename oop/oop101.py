# Abstraction : Soyut özellik taşıma
# Inheritence: Kalıtım. Objeler arasında miras
# Polymorphism: Çok biçimlilik
# Pythonda bütün classalr Object class'ından miras alırlar.

class Library:
    book_count = 0
    # init constructor
    def __init__(self, name, adress):
        # attribute
        self.name = name
        self.address = adress
        self.__books: list = [] # gizli özellik
    
    def add_book(self,b):
        self.__books.append(b)
        Library.book_count += 1
        
    def isbn_is_exist(self,isbn:int):
        for x in self.__books:
            if int(x.isbn) == int(isbn):
                print("isbn is same: {}".format(isbn))
                return True
        return False
        
    def remove_book(self,isbn:int):
        for ind,val in enumerate(self.__books):
            if val.isbn == isbn:
                self.__books.pop(ind)
                
    #self olan her şey object ile ilgili
    def get_books(self):
        return self.__books
    
    def get_lib_size(self):
        return len(self.__books)
   
    @classmethod  # Bu method class'a aittir, objelere ait değildir.
    def get_book_count(cls):
        return Library.book_count
         
    # polymorphism       
    def __str__(self) -> str:
        s = 'Library Books\n'
        for b in self.__books:
            s += str(b) + "\n"
        return s
    
    def __add__(self,l2):
        l3 = Library(self.name+" - "+l2.name,self.address)
        
        for x in self.__books:
            l3.add_book(x)
            
        for x in l2.get_books():
            if not l3.isbn_is_exist(x.isbn):
                l3.add_book(x)
                
        return l3

    @staticmethod
    def show_open_time():
        print("Kütüphane her gün 10'da açılır")

    
class Book:
    def __init__(self, name, isbn:int, author, year):
        self.name: str = name
        self.isbn: int = isbn
        self.author: str = author
        self.year: int = year
        
    # magic functions +, - .. operators are magic functions
    #override: Bir üst classdan gelen metodu üzerine yazmaktır.
    def __str__(self):
        return "{} by {}, {}, {}".format(self.name, self.author, self.year,self.isbn)

class ScienceBook(Book):
    def __init__(self,name, isbn, author, year,field) -> None:
        super().__init__(name,isbn,author,year)
        self.field = field
    
    def __str__(self):
        return super().__str__() +", " +self.field
    
        

x = Library("Atatürk", "test adress")
y = Library("Merkez", "test adress2")

# x.name = "Merkez kütüphane"
# print(x.name)

'''
x.books.append(Book("körlük", "121313", "Yazar 1", 2012))
b: Book = Book("körlük2", "121313", "Yazar 2", 2012)
x.books.append(b)
'''

x.add_book(Book("körlük", 121313, "Yazar 1", 2012))
y.add_book(Book("körlük", 121313, "Yazar 1", 2012))
for i in range(100):
    x.add_book(
        ScienceBook("İzafiyet Teorisi",3131*(i+1),"Albert Einstein",1940+i%10,"Fizik")
    )
    y.add_book(
        ScienceBook("İzafiyet Teorisi",2131*(i+1),"Albert Einstein",1940+i%10,"Fizik")
    )
    
#print(x)

print(Library.get_book_count())
Library.show_open_time()
z =x+y
print(z.get_lib_size())
print(z)