'''
Llenar una lista con los números de 1 al 50, luego mostrar la lista con un bucle for,
los elementos deben mostrarse de la siguiente forma:
1-2-3-4-...-50
'''
# i = 1;
# lista = []
#
# while(i <= 50):
#     lista.append(i)
#     i += 1

# Otra forma más sencilla de hacerlo:
lista = list(range(1, 51))

for i in lista:
    if i <= 49:
        print(i, end="-")
    else:
        print(i)