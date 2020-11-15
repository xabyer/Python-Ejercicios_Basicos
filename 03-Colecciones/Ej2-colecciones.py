'''
Escriba un programa que tenga 2 listas y que, a continuación, cree las siguientes listas
(en las que no puede haber repeticiones):
1º.-Lista de palabras que aparecen en las 2 listas
2º.-Lista de palabras que aparecen en la primera lista, pero no en la segunda
3º.-Lista de palabras que aparecen en la segunda lista, pero no en la primera
4º.-Lista de palabras que coinciden en ambas listas.
'''

lista1 = ["Pedro", "Juan", "Alberto", "Paco", "Pedro", "Alberto", "Juan", "Maria", "Alejandra", "Isabel"]
lista2 = ["Isabel", "Juan", "Javi", "Anabel", "Tomas", "Alberto", "Javi", "Homer", "Alejandra", "Paco"]

lista3 = list(set(lista1) | set(lista2))
print(lista3)

lista4 = list(set(lista1) - set(lista2))
print(lista4)
lista5 = list(set(lista2) - set(lista1))
print(lista5)
lista6 = list(set(lista1) & set(lista2))
print(lista6)