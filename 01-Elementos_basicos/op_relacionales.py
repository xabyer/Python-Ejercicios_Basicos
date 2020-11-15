#Operadores Relacionales --> siempre devuelven true o false y tienen menor prioridad que los aritméticos

'''
Los op relacionales son:
>   mayor que
<   menor que
>=  mayor o igual que
<=  menor o igual que
!=  distinto de
==  igual que
'''

resultado = 10 > 20 #False
print(resultado)
resultado = 10 < 20 #True
print (resultado)
resultado = 10 <= 20 #True
print (resultado)
resultado = 10 >= 20 #False
print (resultado)
resultado = 10 != 20 #True
print (resultado)
resultado = 10 == 20 #False
print (resultado)
resultado = 10 == 10 #True
print (resultado)

# Nota:Recuerda que en python false y true se escribe con la primera letra en mayúscula: False, True.

#Podemos combinar operadores aritméticos con relacionales

a = 10
b = 20
c = 30

resultado = a + b != c #False
print(resultado)
resultado = a + b == c #True
print(resultado)