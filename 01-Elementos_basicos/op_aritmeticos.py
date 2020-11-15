#Operadores aritméticos.

suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5 # Python decide automáticamente convertirlo en float por si tuviese decimales la división, incluso aunque no sea el caso.
division_entera = 10 // 3 # redoncea hacia abajo
modulo = 10 % 3
potencia = 2 ** 3 #Al igual que en JS tambien tiene la potencia con los dos asteriscos

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)
print(potencia)

'''
El orden de prioridad es el siguiente:
1º.-Paréntesis
2º.-Exponenciación
3º.-Multiplicación, división y módulo
4º.-Suma y resta
'''

# vamos a poner 3 elevado a 3 multiplicado por (13/5 - (2x4))
resultado = 3**3 * (13 / 5 - 2 * 4)
print(resultado)