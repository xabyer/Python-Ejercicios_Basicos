# Pilas (simuladas con Listas ya que no tiene python por defecto de momento).

'''
Estructura de datos donde los elementos se añaden y quitan por el final. Como en una pila de libros
que añades al ultimo y quitas del último (los desapilas).
'''

pila = [1, 2, 3]
print(pila)

# Agregando elementos por el final:
pila.append(4)
pila.append(5)

print(pila)

# Sacando elementos por el final de la pila
number = pila.pop()  # Como en JavaScript puedes almacenar el valor del numero que sacas
print(pila)
print(number)