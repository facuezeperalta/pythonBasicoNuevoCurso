#Ejercicio de una biblioteca.

#defino la clase
class Book:
    #creo el constructor
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado.")
        else: 
            print(f"El libro {self.title} NO está disponible para ser prestado.")
        
    def return_book(self):
        self.available = True
        print(f"El libro {self.author} ha sido devuelto")

#clase user:
class User:
    #defino el constructor
    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = [] #está es una lista con los libros que el usario tiene prestados.
    
    def borrow_book(self,book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible para ser prestado.")
    
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no esta en la lista de libros prestados.")
        

class Library:
    def __init__(self):
        self.books =[]
        self.users =[]
    
    def add_book(self,book):
        self.books.append(book)
        print(f"El libro {book.title} se ha agregado correctamente.")
    
    def register_user(self,user):
        self.users.append(user)
        print(f"El usuarios {user.name} ha sido registrado.")
    
    def show_available_books(self):
        print(f"Los libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}" )

#Crear los libros.
libro1 = Book("El principito", "Antoine de Sain")
libro2 = Book("1984", "George Orwell")

#Crear usuarios
user1 = User("Facundo","01")
 
#Creamos la biblioteca 
biblioteca = Library()
biblioteca.add_book(libro1)
biblioteca.add_book(libro2)
biblioteca.register_user(user1)

#Mostrar los libros
biblioteca.show_available_books()

#presto un libro
user1.borrow_book(libro1)

#veo que libros tengo disponbiles
biblioteca.show_available_books()

#Devuelvo el libro.
user1.return_book(libro1)

biblioteca.show_available_books()


