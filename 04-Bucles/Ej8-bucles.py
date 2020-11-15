'''
Hacer un programa que simule un cajero automático con un saldo inicial de 1000€ el Menú tendrá
las siguientes opciones:
1.-Ingresar dinero en la cuenta
2.-Retirar dinero de la cuenta
3.-Mostrar saldo disponible:
4.-Salir

El menú se deberá repetir hasta que el usuario escoja la opción de salir
'''

saldo = 1000.00
operacion = "0"

#Informamos al usuario:
while(operacion != "4"):
    print("Hola, bienvenido a su cajero automatico.\n" +
            "Puede realizar una de las siguientes operaciones:" +
            "\n1.-Ingresar dinero en la cuenta" +
            "\n2.-Retirar dinero de la cuenta" +
            "\n3.-Mostrar saldo disponible" +
            "\n4.-Salir"
          )

    operacion = input("Indique con un número la operación que desea realizar: ")

    if operacion == "1":
        ingreso = float(input("Introduce el importe a ingresar: "))
        saldo += ingreso
        print(f"Operación realizada con exito. Su saldo actual es {saldo: .2f}")
    elif operacion == "2":
        retirar = float(input("Introduce el importe a ingresar: "))
        if saldo < retirar:
            print("Esa cantidad excede su saldo actual. No dispone de tanto dinero.")
        else:
            saldo -= retirar
            print(f"Operación realizada con exito. Su saldo actual es {saldo: .2f}")
    elif operacion == "3":
        print(f"Su saldo actual es {SALDO_INICIAL: .2f}")
    elif operacion == "4":
        print("Adios, ¡¡que pase un buen día!!")
    else:
        print(f"El dato introducido no es una operación valida: {operacion}")
