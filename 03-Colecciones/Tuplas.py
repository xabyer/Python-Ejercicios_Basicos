# Tuplas. Las tuplas son listas inmutables, no se pueden modificar, pero si se puede buscar dentro de ellas

tupla = (4, "Adios", 3.45, [1, 2, 3], 8, "a", 4)

print(tupla)

# Podemos mostrar 1 elemento
print(tupla[1])
print(tupla[2:])

# Busquedas
print(8 in tupla)  # True
print(tupla.index(8))  # 4
print(tupla.count(4))  # 2
print(len(tupla))  #7

# Transformando tuplas en listas y viceversa
lista = list(tupla)
print(lista)

lista.append(55)
tupla2 = tuple(lista)
print(tupla2)