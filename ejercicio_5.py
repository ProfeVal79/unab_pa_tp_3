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
            

#prueba
autor_1 = Persona("Daniel", "Y.Liang", "1950", "China")
autor_1.agregar_obra("Introduction to Python Programming")
autor_1.agregar_obra("Introduction to C++ Programming")
print(autor_1.datos_autor())
print("_"*20)
autor_1.mostrar_bibliografia()