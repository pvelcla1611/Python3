contraseña = "pablo1234"

usuario = input("Introduce la contraseña: ")

if usuario.lower() == contraseña.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")