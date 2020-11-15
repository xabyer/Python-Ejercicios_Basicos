'''
Vamos a solicitar 2 variables e intercambiar su valor, para eso las mostramos por pantalla antes y despues
del la operación de intercambio.
La idea es la siguiente:
a = 7
b = 4
b = a - b
b = 7 - 4 = 3
a = a - b = 7 - 3 = 4
b = a + b = 3 + 4 = 7
'''

# Solicitamos datos
a = int(input("Introduce el numero a: "))
b = int(input("Introduce el numero b: "))

# Informamos de los valores introducidos
print(f"El valor de a es: {a}, el valor de b es: {b}")

b = a - b
a = a - b
b = a + b

# Informamos de los valores cambiados
print(f"El valor de a es: {a}, el valor de b es: {b}")

# Forma simplificada de python para intercambiar variables:

a, b = b, a

print(f"El valor de a es: {a}, el valor de b es: {b}")