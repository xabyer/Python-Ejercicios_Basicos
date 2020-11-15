'''
Juego de adivinar el número dando pistas de mayor o menor. Del 0 al 100 aleatorio.
'''

import random

aleatorio = random.randint(0, 100)
cuenta = 0
numero = -1

while (aleatorio != numero):
    numero = int(input("Trata de adivinar el número elegido. Introduce un número: "))

    if numero < aleatorio:
        print("\tEl numero introducido < buscado.")
        cuenta += 1
    elif numero > aleatorio:
        print("\tEl numero introducido > buscado")
        cuenta += 1
    else:
        print(f"\tEnhorabuena, has acertado. Has tardado {cuenta} intentos")