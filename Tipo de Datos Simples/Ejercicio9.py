cant = int(input("Introduce la cantidad a invertir:"))
interes = float(input("Interes Anual (%):"))
años = float(input("Numero de años:"))

capital = cantidad * (1 + interes / 100) ** años

print("El capital obtenido es:", capital)