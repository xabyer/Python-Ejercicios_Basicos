# Determinar si los dos numeros solicitados al usuario son pares o impares.

print("Este programa determina si los 2 numeros que introduzcas son pares o impares")

num1 = int(input("Introduce el numero 1: "))
num2 = int(input("Introduce el numero 2: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos numeros son pares")
elif num1 % 2 != 0 and num2 % 2 == 0:
    print(f"Solo el numero {num2} es par")
elif num1 % 2 == 0 and num2 % 2 != 0:
    print(f"Solo el numero {num1} es par")
else:
    print("Ambos numeros son impares")
