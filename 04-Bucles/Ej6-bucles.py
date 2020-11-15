'''
Introducide un número por el usurio, guardar su tabla de multiplicar del 1 al 10 en una lista
Y mostrarla por pantalla.
'''
lista = []
num = int(input("Introduce el número del que quieras saber su tabla de multiplicar: "))

for i in range(1, 11):
    lista.append(num * i)
    print(f"{i} x {num} = {lista[i - 1]}")
