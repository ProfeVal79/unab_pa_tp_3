#Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
#cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
#(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
#servicios: getters y setters, método para leer la información y método para mostrar la
#información.
#● Este último método mostrará la información del libro con este formato:
#Título: Introduction to Java Programming 3a. edición
#Autor: Liang, Y. Daniel
#ISBN: 0-13-031997-X
#Prentice-Hall, New Jersey (USA)
#viernes 16 de noviembre de 2001
#784 páginas

class Persona:
    def __init__(self, apellido, nombre, fecha_nac, lugar_nac, ):
        self.apellido = apellido
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.lugar_nac = lugar_nac
        self.obras = []

    def agregar_obra(self, titulo_obra):
        self.obras.append(titulo_obra)

    def datos_autor(self):
        return f"\n DATOS DEL AUTOR:\n Nombre:{self.nombre}\n Apellido:{self.apellido}\n Fecha de Nacimiento:{self.fecha_nac}\n Lugar de Nacimiento:{self.lugar_nac}"

    def mostrar_bibliografia(self):
        print(f" BIBLIOGRAFÍA de: {self.nombre}, {self.apellido}\n")
        if not self.obras:
            print(f"No hay obras registradas")
        for obra in self.obras:
            print(f"{obra}")

class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial,lugar, fecha_de_edicion):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_de_edicion = fecha_de_edicion
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_autor(self):
        return self.autor
    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def get_ISBN(self):
        return self.ISBN
    def set_ISBN(self, nuevo_ISBN):
        self.ISBN = nuevo_ISBN

    def get_paginas(self):
        return self.paginas
    def set_paginas(self, nuevo_paginas):
        self.paginas = nuevo_paginas
    
    def get_edicion(self):
        return self.edicion
    def set_edicion(self, nuevo_edicion):
        self.edicion = nuevo_edicion

    def get_editorial(self):
        return self.editorial
    def set_editorial(self, nuevo_editorial):
        self.editorial = nuevo_editorial

    def get_lugar(self):
        return self.lugar
    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar

    def get_fecha_de_edicion(self):
        return self.fecha_de_edicion
    def set_fecha_de_edicion(self, nueva_fecha_de_edicion):
        self.fecha_de_edicion = nueva_fecha_de_edicion

    def leer_informacion(self):
        print(f"CARGA DE DATOS DE LIBRO:\n")
        self.titulo = input("Ingrese el titulo: ")
        self.autor.nombre = input("Ingrese el nombre del autor: ")
        self.autor.apellido = input("Ingrese el apellido del autor: ")
        self.ISBN = input("Ingrese el ISBN: ")
        self.paginas = int(input("Ingrese la cantidad de páginas: "))
        self.edicion = input("Ingrese la edición: ")
        self.editorial = input("Ingrese la editorial: ")
        self.lugar = input("Ingrese lugar: ")
        self.fecha_de_edicion = input("Ingrese la fecha de edición: ")

    def mostrar_informacion(self):
        print(f"Información del libro: ")
        print(f"Titulo:{self.titulo} - {self.edicion} edición")
        print(f"Autor:{self.autor.apellido}, {self.autor.nombre}")
        print(f"ISBN:{self.ISBN}")
        print(f"{self.editorial} {self.lugar}")
        print(f"{self.fecha_de_edicion}")
        print(f"{self.paginas} páginas")



            

#prueba
autor_1 = Persona("Daniel", "Y.Liang", "1950", "China")
autor_1.agregar_obra("Introduction to Python Programming")
autor_1.agregar_obra("Introduction to C++ Programming")
print(autor_1.datos_autor())
print("_"*20)
autor_1.mostrar_bibliografia()
libro_1 = Libro("Introduction to Java Programming", autor_1, "0-13-031997-x", 784, "3a", "Prentice-Hall", "New Jersey (USA)", "viernes 16 de noviembre de 2001")
print("_"*20)
libro_1.mostrar_informacion()
#Creamos una Persona vacia y un libro vacio para llamar al método leer información
#autor_molde = Persona(" ", " ", " ", " ")
#libro_final = Libro(" ", autor_molde, " ", 0, " ", " ", " ", " ")
#libro_final.leer_informacion()

#libro_final.mostrar_informacion()
print("_"*20)

otro_autor = Persona("de Saint - Exupery", "Antoine", "29 de junio de 1900", "Lyon, Francia")
mi_libro = Libro("El principito", otro_autor, "978-0156012195", 96, "1a", "Salamandra", "Nueva York, EE.UU", "6 de abril de 1943")
mi_libro.mostrar_informacion()
print("_"*20)
print(otro_autor.datos_autor())

