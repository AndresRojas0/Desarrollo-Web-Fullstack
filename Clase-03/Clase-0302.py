# 2. Escribe un programa Python que acepte 5 números decimales del usuario.

n=[]
for i in range(5):
    num=float(input('Ingrese un número decimal: '))
    n.insert(i, num)
print(n)