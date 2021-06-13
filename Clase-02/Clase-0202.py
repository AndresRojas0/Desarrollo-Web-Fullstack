# 2. Escribe un programa Python que acepte un número entero (n) y calcule el valor de n + nn + nnn.

n = int(input('Ingrese un número entero: '))
suma = n + n*n + n*n*n 
print('La suma de su potencia primera, su potencia segunda y su tercera es: ',suma)