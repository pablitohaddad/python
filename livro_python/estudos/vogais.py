vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
outros = []
entrada = input("Digite aqui uma palavra a ser filtrada: ")

for letras in entrada:
    if letras not in vogais:
        outros.append(letras)
if len(outros) > 0:
    print(f"A palavra {entrada}, possui {len(outros)} caracteres que não são vogais")
else:
    print(f"A palavra {entrada} só possui vogais")