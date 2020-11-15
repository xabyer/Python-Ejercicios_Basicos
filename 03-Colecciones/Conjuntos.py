# Conjuntos

conjunto = set()  # Declaración de un conjuto vacio
conjunto = {}
print(conjunto)
# Para la declaracion de un conjuto vacio es necesario usar primero la palabra set porque sino
# entendería que se trata de un Diccionario, pues las llaves se usan para ambos. Un diccionario
# Equivale a lo que sería un JSON en JavaScript.

#Si se inicia un conjuto en su declaración no es necesario usar la palabra set pues se dierencian
#claramente de los diccionarios como veremos ahora:

# Los conjuntos se caracterizan por no poder tener valores duplicados, ni contener otras colecciones.
conjunto = {1, 2, 3, "Hola", 4.56, "Spider-Man", 'a'}
print(conjunto)
conjunto = {1, 2, 3, "Hola", 4.56, "Spider-Man", 'a', 1, 2, 3}
print(conjunto)  # Como puedes comprobar ignora los valores repetidos, aunque no da fallo el interprete

'''
Los conjuntos no pueden tener colecciones de ningún tipo en su interior:
conjunto = {1, 2, 3, "Hola", 4.56, "Spider-Man", 'a', [1, 2, 3]} --> El interprete
lanzaría un error porque no puede haber otro tipo de coleccion dentro de un conjunto
'''

# Añadir elementos a un conjunto.

conjunto.add(5)
print(conjunto)
# Los conjuntos son grupos de valores primitivos desordenados, por eso se añade aleatoriamente al conjunto

#  Otro ejemplo:
conjunto.add("Ironman es el mejor")
print(conjunto)

# Eliminando elementos:

conjunto.discard('a')
print(conjunto)

# Busquedas:
print( 3 in conjunto)  # True
print(3 not in conjunto) #False

# Con el método clear vaciamos el conjunto:

conjunto.clear()
print(conjunto)

# Parte 2 conjuntos:

a = {1, 2, 3}
b = {3, 4, 5}
c= {3, 1, 2}

print(a == b)
print(a == c)
print(len(a))

# Unión de dos conjuntos (como en mates)

d = a | b
print(d)  # Puesto que el 3 es repetido lo excluye en la unión.

# Intersección de conjuntos
e = a & b
print(e)  # 3 es el único elemento en común de ambos

# Diferencia de conjuntos --> Elementos de a que no estan en b

f = a - b
print(f)  # 1 y 2


# Diferencia simétrica --> Elementos de a y b no repetidos
g = a ^ b
print(g) # 1, 2, 4, 5

# Subconjuntos
h = {1, 2, 3, 4, 5}
print(a.issubset(h))  # True. A es un subconjuto de h
print(f.issubset(e))  # False

# Superconjuntos
print(d.issuperset(a))
print(d.issuperset(g))

# Conjuntos disconexos --> No comparten ningún elemento en común
print(f.isdisjoint(e))  #True, no comparten elementos
print(a.isdisjoint(b))  #False

# Conjuntos inmutables:
i = frozenset({1, 2, 7})   #Con frozenset convertimos el conjunto en inmutable

''''
Si intentase hacer esto:
i.add(3)
El interprete daría error y detendría el proceso en ese punto. Ni siquiera interpretaría la siguiente linea
print(i)
'''