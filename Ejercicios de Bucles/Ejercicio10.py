numero = int(input("Introduce un numero entero: "))
i = 2
primo = 0

while (i != numero):
    if (numero%i == 0):
        primo = 1
    i = i + 1

if (primo == 0):
    print("El numero es primo")
else:
    print("El numero no es primo")