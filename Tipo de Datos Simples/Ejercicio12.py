precio = 3.49
descuento = 0.60

barras = int(input("Introduce el número de barras que no son del día: "))

precio_descuento = precio * descuento
precio_final = precio - precio_descuento
total = barras * precio_final

print("Precio habitual de una barra:", precio, "€")
print("Descuento por no ser fresca:", precio_descuento, "€")
print("Coste final total:", round(total, 2), "€")