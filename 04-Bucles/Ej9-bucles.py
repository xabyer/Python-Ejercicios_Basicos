'''
Mostrar una frase introducida por el usuario sin espacios
'''

frase = input("Introduce una frase: ")
frase2 = ""

for i in frase:
    if i != " ":
        frase2 += i

print(frase2)
print((f"El numero de caracteres de la frase es: {len(frase2)}"))