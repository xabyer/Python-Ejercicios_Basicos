'''
Determina el resultado del a siguiente expresión lógica:
((3+5*8) < 3 and (( (-6/3) * 4) + 2 < 2) or (a > b) )
 43 < 3 and ( -6 < 2) or (a > b )
 false and true or a>b
 Por lo que todo depende del valor de a y b
'''

# Solicitud de datos:

a = int(input("Introduce el numero a: "))
b = int(input("Introduce el numero b: "))

resultado = (( (3+5*8 < 3) and (( (-6/3) * 4) + 2 < 2) ) or (a > b) )

print(resultado)