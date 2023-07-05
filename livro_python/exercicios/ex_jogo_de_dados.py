import random
nome_1 = input("Informe o nome do jogador 1: ")
nome_2 = input("Informe o nome do jogador 2: ")
numeros = 1, 2 , 3, 4, 5, 6
numero_j1 = random.choice(numeros)
numero_j2 = random.choice(numeros)

print(f"O seu número {nome_1} é {numero_j1}")
print(f"O seu número {nome_2} é {numero_j2}")

if numero_j1 > numero_j2:
    print(f"Parabéns {nome_1}, você ganhou!!")
elif numero_j2 > numero_j1:
    print(f"Parabéns {nome_2}, você ganhou!!")
else:
    print("Houve um empate, ninguém venceu")
