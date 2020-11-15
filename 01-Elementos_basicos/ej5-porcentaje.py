_PORCENTAJE = 0.85
#Solicitamos el importe de la compra al usuario:
importeCompra = float(input("Introduce el importe total de la compra: "))

#Zona de operaciones
importeCompra *= _PORCENTAJE

print(f"El importe de la compra con el {100 * (1 - _PORCENTAJE): .2f}% descuento es {importeCompra: .2f}")