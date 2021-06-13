# 1. Escribe una clase de Python llamada Rectangulo que se define por una longitud y un ancho
# y un método que calculará el área de un rectángulo.

class Rectangulo:

    tipoGeometrico = "Cuadrilátero"

    def __init__(self, long, ancho):
        self.long = float(long)
        self.ancho = float(ancho)
    
    def area(self):
        return f"Rectángulo tiene área de: {self.long * self.ancho} unidades"

r1 = Rectangulo(10,20)
print(r1.area())