#Vamos a crear una calculadora básica que imite las cuatro operaciones elementales:
'''
S o s para suma
R o r para Resta
P o p o M o M para multiplicación
D o d para division
'''

print("Este programa suma, resta, multiplica o divide dos numeros.")

num1 = float(input("Introduce el numero 1: "))
num2 = float(input("Introduce el numero 2: "))

print("Introduce S o s para suma, R o r para Resta, \nP p M o m para producto y D o d para division.")
operacion = input("Introduce tu operación: ")

if operacion == "S" or operacion == "s":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "R" or operacion == "r":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "P" or operacion == "p" or operacion == "M" or operacion == "m":
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion es es: {resultado}")
elif operacion == "D" or operacion == "d":
    resultado = num1 / num2
    print(f"El resultado de la resta es: {resultado}")
else:
    print("El carácter introducido no es una operacion valida")
