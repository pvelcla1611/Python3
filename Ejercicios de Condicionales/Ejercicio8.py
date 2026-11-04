puntuacion = float(input("Introduce tu puntuacion: "))

if puntuacion == 0.0:
    print("Nivel: Inaceptable")
elif puntuacion == 0.4:
    print("Nivel: Aceptable")
elif puntuacion >= 0.6:
    print("Nivel: Meritorio")
else:
    print("Puntuacion no valida")

dinero = 2400 * puntuacion
print("Dinero recibido:", dinero, "euros")