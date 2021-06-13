# 2. Crea una clase Minibus que herede de la clase Vehiculo.
# Debes poder tener un método capacidad() que defina por defecto la capacidad de 6 asientos.
# Luego crea una clase Pasajero que puedas ir agregando a una instancia de Minibus.
# Esa instancia no deberá permitir mas de 50 pasajeros únicos (no se permiten pasajeros repetidos).

class Vehiculo:
    def __init__(self, asientos, pasajeros):
        self.asientos = asientos
        self.pasajeros = []

    def capacidad(self, asientos):
        self.asientos = asientos
        return f"Capacidad: {self.asientos} asientos."

    def agregar_pasajero(self, nombre):
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(nombre)
        return True
    
    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

class Minibus(Vehiculo):
    def capacidad(self, asientos = 6):
        self.asientos = 6

