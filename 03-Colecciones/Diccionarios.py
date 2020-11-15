###############################Diccionarios#####################################
# Equivalen a lo que son los JSON en JavaScript. No tienen un orden especifico para guardarse
# Y tienen 2 elementos por posición, clave y valor.

diccionario = {}  # Así se declara un diccionario vacío.
diccionario = {"azul": "blue", "rojo": "red", "verde": "green"}

print(diccionario)
print(diccionario["azul"])

diccionario["amarillo"] = "yellow"
print(diccionario)

diccionario["azul"] = "BLUE"
print(diccionario)

del(diccionario["verde"])
print(diccionario)

agenda = {"Juan": [22, 1.79], "Javi": [38, 1.80], "Marta": [25, 1.67]}
print(agenda)
agenda = {"Juan": {"edad": 22, "estatura": 1.79}, "Javi": {"edad": 38, "estatura": 1.80}, "Marta": {"edad": 25,
                                                                                                 "estatura": 1.67}}
print(agenda)
print(agenda["Marta"])

# Diccionarios Parte 2

equipo = {10: "Paulo Dybala", 11: "Douglas Costa", 7: "Cristiano Ronaldo", 17: "Mario Mandzukic"}
print(equipo[10])
# Si se pone un indice que no existe da error el interprete

print(equipo.get(7, "Jugador no disponible"))
print(equipo.get(6, "Jugador no disponible"))  # Con get dispara el mensaje de error e interpreta todo el código

# Busquedas

print(10 in equipo)  # True
print(12 in equipo)  # False

print(equipo.keys())  # Mostrar solo las claves
print(equipo.values())  # Mostrar solo los valores
print(equipo.items())  # Crea una lista de tuplas con los indices y valores de un Diccionario
print(len(equipo))

equipo.clear()
print(equipo)