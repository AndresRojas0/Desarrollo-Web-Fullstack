# 4. Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180]) 
# mostrar números divisibles por cinco, y si encuentra un número mayor que 150, salir del bucle.

lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180]
for i in range (len(lista1)):
    if lista1[i] > 150:
        break
    if lista1[i] % 5 == 0:
        print('El número: ',lista1[i],'es divisible por cinco.' )