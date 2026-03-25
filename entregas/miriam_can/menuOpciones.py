print("Menu de opciones matemáticas")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opc = int(input("Escribe el numero de la opción deseada: "))

if opc == 1:
    print("Seleccionaste suma")
elif opc == 2:
    print("Seleccionaste resta")
elif opc == 3:
    print("Seleccionaste multiplicación")
elif opc == 4:
    print("Seleccionaste división")
else:
    print("La opción seleccionada no es válida")