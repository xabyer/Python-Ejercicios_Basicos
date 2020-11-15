# Condicionales anidados

edad = int(input("Introduce tu edad: "))

# if edad > 0 and edad <= 120:
if 0 < edad <= 120: # Son formas equivalentes de hacer un rango
    print ("El dato introducido esta entre el rango de edad permitida")
    if edad > 18:
        print("Es usted mayor de edad")
    else:
        print ("Es usted menor de edad")
else:
    print ("El dato introducido no es un valor permitido para la edad")