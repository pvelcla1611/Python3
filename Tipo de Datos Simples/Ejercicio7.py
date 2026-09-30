peso = float(input("¿Cual es tu peso en KG"))
medida = float(input("Cual es tu estatura en metros"))

masa = peso / (medida ** 2)
print("Tu indice de masa corporal es", round(masa, 2))