# Solicitud de datos
from math import pi

radio = float(input("Introduce el radio del circulo: "))

area = pi *radio ** 2
longitud = 2 * pi * radio

print(f"El área del circulo es {area: .2f} y su longituda es {longitud: .2f}")
