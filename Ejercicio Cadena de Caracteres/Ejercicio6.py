frase = input("Frase: ")
vocal = input("Mayusculas: ")

vocalm = vocal.upper(vocal)
frasem = frase.replace(vocal, vocalm)
print(frasem)