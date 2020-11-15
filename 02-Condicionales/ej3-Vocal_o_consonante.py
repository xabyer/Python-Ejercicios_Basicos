# Hacer un programa que indique si el carácter introducido es una vocal o una consonante:

print ("Este programa determina si el caracter que introduzcas es vocal o consonante.")

cha = input("Introduce un caracter: ")

if cha == 'a' or cha == 'e' or cha == 'i' or cha == 'o' or cha == 'u':
    print (f"El caracter introducido es la vocal {cha}")
else:
    print (f"El caracter introducido es la consonante {cha}")