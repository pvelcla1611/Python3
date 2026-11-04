numero = int(input("Introduce un número entero positivo: "))

primer = 1

while primer <= numero:
    if primer % 2 != 0:
        print(primer, end=", ")
    primer = primer + 1