frase = input("Frase: ")
vocal = input("Mayusculas: ")

vocalm = vocal.upper()
frasem = frase.replace(vocal, vocalm)
print(frasem)