'''
Pide numeros y metelos en una lista, cuando el usuario meta un 0 dejaremos de insertar.
Por último muestra los números ordenados de menor a mayor.
'''
num = -1
lista = []

while(num != 0):
    print("Introduce cero para finalizar")
    num = int(input("Introduce un numero: "))
    if num == 0:
        break
    else:

        lista.append(num);

lista.sort();
print("La lista ordenada sería:")
for i in lista:
    print(i, end=" ")