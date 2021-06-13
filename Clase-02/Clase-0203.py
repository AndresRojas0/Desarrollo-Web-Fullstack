# 3. Escribe un programa en Python que acepte una cadena de caracteres y cuente 
# el tamaño de la cadena y cuántas veces aparece la letra A (mayúscula y minúscula).

cadena = input('Ingrese cualquier texto a tratar como una cadena de caracteres: ')
tamaño = len(cadena)
letra = "a"

contmin = 0
contmay = 0

for i, l in enumerate(cadena):
    if l == letra.lower():
       contmin = contmin + 1
    if l == letra.upper():
       contmay = contmay + 1

print('El tamaño de la cadena es: ',tamaño)
print('Cantidad de veces que aparece letra: ',letra,'minúscula: ',contmin)
print('Cantidad de veces que aparece letra: ',letra,'mayúscula: ',contmay)