''''
Hacer un programa que pida una cadena por teclado. Luego meta los caracteres en una lista sin repetir
caracteres.
'''

frase = input("Introduce una frase: ")
lista = []

for i in frase:
    if i not in lista:
        lista.append(i)


print(lista)