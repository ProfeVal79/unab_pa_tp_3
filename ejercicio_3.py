#Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
#pasa la línea en un espacio de dos dimensiones.
#La clase dispondrá de los siguientes métodos:
#● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
#Punto, que son utilizados para inicializar los atributos.
#● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
#● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
#● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
#● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.
from ejercicio2 import Punto
class Linea:
    def __init__(self, _punto_a, _punto_b):
        self._punto_a = _punto_a
        self._punto_b = _punto_b

    def mueve_derecha(self, n):
        self._punto_a.x += n
        self._punto_b.x += n


    def mueve_izquierda(self, n):
        self._punto_a.x -= n
        self._punto_b.x -= n

    def mueve_arriba(self, n):
        self._punto_a.y += n
        self._punto_b.y += n

    def mueve_abajo(self, n):
        self._punto_a.y -= n
        self._punto_b.y -= n

    def __str__(self):
        return f"Linea(({self._punto_a.x},{self._punto_a.y}), ({self._punto_b.x},{self._punto_b.y}))"

#prueba
punto_a = Punto(3,5)
punto_b = Punto(2,6)
mi_linea = Linea(punto_a, punto_b)
print(mi_linea.__str__())
mi_linea.mueve_arriba(3)
print(mi_linea)
mi_linea.mueve_derecha(2)
print(mi_linea)
mi_linea.mueve_abajo(3)
print(mi_linea)
mi_linea.mueve_izquierda(2)
print(mi_linea)
    