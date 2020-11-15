''''
Escriba un programa que muestre una lista de las caracteristicas de estos 3 personajes
del señor de los anillos. Aragorn, Gandalf y Legolas, deben mostrar las siguientes carac-
teristicas: nombre, clase y raza. El:
Nombre: Aragorn
clase: Guerrero
Raza: Dúnedan del Norte
Mago e Istar para Gandalf; Arquero y elfo Sindar para Legolas
'''

personajes = []

aragonr = {"Nombre": "Aragorn", "Clase": "Guerrero", "Raza": "Dúnedan del Norte"}
gandalf = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
legolas = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}

personajes.append(aragonr)
personajes.append(gandalf)
personajes.append(legolas)

print(personajes)