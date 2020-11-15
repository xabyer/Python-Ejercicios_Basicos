# Funciones Integradas:

# En el data_input vimos 2 para convertir strings en enteros y float:
# int(numeroString)
# float(numeroString)

# Number to String:

n = str(10)
print(type(n))
n = str(10.5)
print(type(n))

# Num a Binario:

n = bin(10)
print(n)
print(type(n))

# Num a Octal:

n = oct(10)
print(n)
print(type(n))

# Numb a Hex:

n = hex(10)
print(n)
print(type(n))

# bin, oct, hex to int:

n = int("0b1010", 2) # num y base
print(n)
n = int("0o12", 8)
print(n)
n = int("0xa", 16)
print(n)

# valor absoluto de un Número

n = abs (-15)
print(n)

# Redondeo:

n = round(5.6)
print(n)
n = round(5.4)
print(n)

# Contar tamaño de 1 string:

n = len ("Califragilisticoespialidoso")
print(n)