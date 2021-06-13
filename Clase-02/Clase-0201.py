# 1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área.

from math import pi 

r = float(input('Radio del círculo: '))
area  = pi * r ** 2
print('El área del círculo de radio: ',r,'es: ',area)