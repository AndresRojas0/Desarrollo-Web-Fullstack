try:
    f = open("Clase-04\miarchivo.txt", "w")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
except FileNotFoundError:
    print("Algo malo pasó al intentar abrir el archivo.")
    f = open("Clase-04\milog.txt", "w")
    f.write("Linea de prueba que estoy escribiendo en el curso.")
finally:
    print("El try y except finalizó.")