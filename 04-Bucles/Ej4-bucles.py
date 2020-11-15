'''
hacer un programa para sumar números pares dentro de un rango.
'''
suma = 0
rangoInferior = int(input("Introduce el rango inferior: "))
rangoSuperior = int(input("Introduce el rango superior: "))

for i in range(rangoInferior, rangoSuperior +1):
    if i % 2 == 0:
        suma += i


print(f"La suma de los numeros pares del {rangoInferior} al {rangoSuperior} es {suma}")

