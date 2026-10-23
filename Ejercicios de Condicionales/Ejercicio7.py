renta = int(input("Dime tu renta anual: "))
if renta <= 10000:
    print ("5% tipo impositivo")
elif renta >=10001 and renta <=20000:
    print ("15% tipo impositivo")
elif renta >=20001 and renta <=35000:
    print ("20% tipo impositivo")
elif renta >=35001 and renta <=60000:
    print ("30% tipo impositivo")
elif renta >=60000:
    print ("45% tipo impositivo")