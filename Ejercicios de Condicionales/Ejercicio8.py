puntuacion = float(input("Introduce tu puntuacion: "))

if puntuacion == 0.0:
    print("Nivel: Inaceptable")
    dinero = 2400 * puntuacion
    print("Dinero recibido:", dinero, "euros")

elif puntuacion == 0.4:
    print("Nivel: Aceptable")
    dinero = 2400 * puntuacion
    print("Dinero recibido:", dinero, "euros")

elif puntuacion >= 0.6:
    print("Nivel: Meritorio")
    dinero = 2400 * puntuacion
    print("Dinero recibido:", dinero, "euros")

else:
    print("Puntuacion no valida")