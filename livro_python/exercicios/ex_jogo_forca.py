palavra_resposta = input("Digite a palavra a ser adivinhada: ")
palavra_resposta = palavra_resposta.capitalize()

tamanho_palavra = len(palavra_resposta)
print("A palavra possui", tamanho_palavra, "letras.")

tentativas = 6
letras_digitadas = []
for x in range (tentativas):
    letra: input("Digite uma letra")
    str.capitalize(letra)
    letras_digitadas.append(letra)

    if letra in palavra_resposta:
        print("A letra", letra, "está na palavra")
    else:
        print("A letra", letra,"não está na palavra")
    