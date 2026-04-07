#Ejercicio 2:
# Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
#constructor que recibe ambos valores.
# Definir métodos tales como:
# eje_x
# eje_y
# impresion (método que devuelve en representación de string ambos valores)
# opuesto (método que devuelve el punto opuesto -es decir con los atributos
#negativos-)
 #Cualquier otro método que considere importante

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        print(f"Eje_x: {self.x}, Eje y: {self.y}")
        return self.x , self.y

    def opuesto(self):
        op_x = -1 * self.x
        op_y = -1 * self.y
        return f"{op_x, op_y}"


#prueba
mi_punto = Punto(3, -4)
print(mi_punto.impresion())
print(mi_punto.opuesto())

