'''
Llenar una lista con los números del 1 al 10 luego modificar los elementos de la lista
multiplicandolos por un valor que el usuario digite.
'''

lista = list(range(1,11))

print("La lista original es: ")

for i in lista:
    print(i, end=" ")

numero = int(input("\nIntroduce un numero para modificar una lista: "))


for i in range(len(lista)):
    lista[i] *= numero

'''
Otra forma de hacer el for anterior sería:
for indice, i in enumerate(lista):
    lista[indice] *= numero
'''

print(f"\nLista con los elementos multiplicados por {numero}")

for i in lista:
    print(i, end=" ")