fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

partes = fecha.split("/")

dia = partes[0]
mes = partes[1]
año = partes[2]

print("Día:", dia)
print("Mes:", mes)
print("Año:", año)