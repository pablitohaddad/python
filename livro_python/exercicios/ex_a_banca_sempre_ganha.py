import random
numero_jogador = int(input("Escolha um número de 1 a 100: "))
numero_sorteado = random.randint(1,101)
print("o número sorteado pela banca é o ", numero_sorteado)
if numero_jogador == numero_sorteado:
    print("Parabéns, você ganhou!!")
else:
    print("A banca sempre vence!!")

