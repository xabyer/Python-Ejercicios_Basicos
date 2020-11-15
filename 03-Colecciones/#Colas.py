# Colas con listas

#from collections import deque

'''
Estructura de datos tipo FIFO (first input first ouput). Como en una cola de personas el primero en llegar
es atentido y luego se marcha. El ultimo se pone al final de la cola.
'''

# Nota investigar las colas en python con la librería (o módulo) collections

cola = ["Maria", "Juan", "Jose", "Fran"]
print(cola)

# Agregamos elementos a la cola:
cola.append("Pepe")
cola.append("Rosa")
print(cola)

#Sacando elementos por la cola:
n = cola.pop(0)
print(f"Atendiendo a {n}")
print(cola)