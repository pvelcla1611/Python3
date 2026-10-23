nombre = input("Dime tu nombre: ")
sexo = input("Dime tu sexo: ")

if sexo == "M" and nombre[0] < "M":
    print("Tu grupo es el A")
elif sexo == "H" and nombre[0] > "N":
    print("Tu grupo es el A")
else:
    print("Tu grupo es el B")