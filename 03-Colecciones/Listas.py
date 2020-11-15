# Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista[0])

print(lista[-1])  # Las listas permiten imprimir así el último elemento, -1 es el ultimo elemento

# Si nos excedemos nos aparecerá un List index out of range error.

print(lista[1:4])  # Imprime desde la posicion 1, martes, hasta n-1 jueves

print(lista[:4])  # Imprime desde el inicio hasta n-1 jueves

print(lista[3: 4])  # Imprime desde 3 hasta n-1 solo Jueves.
# Si no ponemos nada a ambos lados de los 2 puntos es como solicitar todo el array
# O lo que es lo mismo:
print(lista)  # Equivale a print(lista[:])

print(len(lista))  # Ver el tamaño de una lista

# Las listas son como los arrays de JavaScript, admiten todo tipo de valores mezclados

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 1, 5.6, [1, 2, 3], True]
print(lista)

######################################################################################

# Parte 2, funciones propias de las listas:

lista2 = [1, 2, 3, 4, 5]

lista2.append(6)  # Insertar al final
lista2.append("Juan")

lista2.insert(2, "Tres")  # Insertar en una posición determinada

lista2.extend([7, 8, 9])  # Concatena 2 arrays

print(lista2)

lista3 = lista + lista2
print(lista3)  # Otra forma de concatenar 2 listas en una tercera.

# Busquedas en listas

print("Martes" in lista)  # True
print(6 in lista2)  # True
print(10 in lista3)  # False

# Muestra la primera posicion en la que aparce un elemento. Si se le pasa un elemento que no existe da error
print(lista.index("Miercoles"))# 2
print(lista3.index(1)) #5 pese a que aparece despues otra vez

# buscar valores repetidos en una lista
print(lista3.count(1))# 3 Como puedes ver es capaz de encontrarlo hasta dentro de las listas anidadas

print(lista.count(10))# 0 veces

# Eliminar elementos de una lista

lista.pop()  # Elimina el ultimo valor de una lista
print(lista)
# También podemos especificarle una posición determinada a borrar:
lista.pop(-2)
print(lista)
# Si queremos qutar un valor determinado de la Lista sin conocer su posición podemos:

lista.remove(1)
print(lista)
lista.remove([1, 2, 3])

# Para borrar toda una lista podemos usar el método clear
copiaLista = [1, 2, 3, 4 ,5]
print(copiaLista)
copiaLista.clear()
print(copiaLista)

#Podemos darle la vuelta a una lista con reverse

lista.reverse()
print(lista)

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"] * 2
# Ahora los elementos estan duplicados en el mismo orden
print(lista)

lista4 = [5, 6, 3, 2, 9, 0, 8, 1, 4, -7]
print(lista4)

# podemos ordenar los elementos de una lista:

lista4.sort()
print(lista4)

# También podemos ordenarlos descendentemente:
lista4.sort(reverse=True)
print(lista4)
