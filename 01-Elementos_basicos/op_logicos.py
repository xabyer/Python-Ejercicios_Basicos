#Permiten construir operaciones lógicas obteniendo como resultado un boolean.

'''
Los operadores lógicos son:
and conjuncion (ambos ciertos o ambos falsos, los diferentes retornan falso siempre)
or  disyunción (uno de los 2 valores es cierto y el siguiente ya no se evalua)
not negación invierte el valor Boolean

Se ponen en minúscula.

Su prioridad es:
1º.-not
2º.-and
3º.-or
'''

#ejemplo:

a = 10
b = 12
c = 13
d = 10

#( (false) or (true) and ( (false) or (false) )
#( (false) or (true) and (false) )
#( (false) or (false) )
#false
print( (a > b) or (a < c) and ((a == c) or (a >= b)) )

'''
Prioridad Global de todos los operadores:
1.- Parentesis ()
2.- Potencia **
3º.- *, /, %, not
4.-+(suma), -(resta), and
5.-Relacionales : <, >, >=, <=, ==, |=, y también el or lógico.
'''

a = 10
b = 15
c = 20

resultado = ((a < b) and (b < c)) #True and True = True
print(resultado)

resultado = ((a > b) and (b < c)) #False and True = False
print(resultado)

resultado = (not(a > b) and (b < c)) #True and True = True
print(resultado)

resultado = ((a > b) or (b < c)) #False or True = True
print(resultado)