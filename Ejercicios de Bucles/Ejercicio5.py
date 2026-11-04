cantidad = float(input("Introduce una cantidad a invertir: "))
interes = float(input("Dime el interes: "))
años = int(input("Dime los años: "))

interes /= 100
for año in range (1,años + 1):
    capital = cantidad * (1 + interes) ** año
    print(f"año{año}: {capital:.2f}")