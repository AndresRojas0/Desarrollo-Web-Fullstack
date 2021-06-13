# 3. Escribe un programa Python que reciba 5 números enteros del usuario y los guarde en una lista.

n=[]
for i in range(5):
    num=int(input('Ingrese un número entero: '))
    n.insert(i, num)
print(n)