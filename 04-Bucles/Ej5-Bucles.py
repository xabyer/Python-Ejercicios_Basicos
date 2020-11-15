'''
Factorial de un numero positivo introducido por el usuario.
'''

num = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
while(num < 0):
    print("El numero debe ser positivo o cero")
    num = int(input("Introduce un número para calcular su factorial"))

for i in range(1, num + 1):
    factorial *= i

print(f"El factorial de {num} es {factorial}")