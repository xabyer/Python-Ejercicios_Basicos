# Esto es un comentio de 1 sola línea

'''
Esto es un comentario
multilínea.
'''

# Tipos de datos primitivos en Python

# Enteros:
numero = 10
print(numero)
print(type(numero))

# Float:
numero2 = 10.01
print(numero2)
print(type(numero2))

suma = numero + numero2# Suma
print(suma)
print(type(suma))

# String:
cadena = "Me llamo Javi"
print(cadena)
print(type(cadena))
cadena2 = ' y me gusta programar'

print(cadena + cadena2) # concatenacion
# Nota: Python como JavaScript sabe diferenciara cuando sumas números y cuando concatenas strings

print(cadena + cadena2 + ". El resultado de sumar numero y numero2 es: ", suma)


#Como JavaScritp Python permite el tipado dinámico. Ejemplo:

valor = 25; # Ahora es entera
print(valor)
print (type(valor))
valor = "Juan" # Ahora es de tipo string
print(valor)
print (type(valor))


# Boolean

# Como en cualquier otro lenguaje tienen el valor de True o False
cierto = True
falso = False
print(cierto)
print (type(cierto))
print(falso)
print (type(falso))