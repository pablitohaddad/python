import random

def jogar():

    print("***********************************")
    print("BEM VINDO AO JOGO DA ADVINHAÇÃO!!!!")
    print("***********************************")

    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual a dificuldade do jogo? ")
    print("Fácil(1) Médio(2) Difícil(3)")

    nivel = int(input("Digite o nível: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5
    else:
        print("VALOR INVÁLIDO")
        
    for rodada in range (1, total_tentativas + 1):
        print(f"Rodada {rodada} de {total_tentativas}")
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou:", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        if chute < 1 or chute > 100:
            print("Número inválido")
            continue

        if (acertou):

            print("Você acertou o número")
            break
        else: 
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - round(pontos_perdidos)

            if (maior):

                print("Você errou o número! O seu chute foi maior que o número secreto")

                if(rodada == total_tentativas):
                    print(f"Você errou, o número secreto era {numero_secreto}. Você fez {pontos} pontos")

            elif (menor):

                print("Você errou o número! O seu chute foi menor que o número secreto")

                if(rodada == total_tentativas):
                    print(f"Você errou, o número secreto era {numero_secreto}. Você fez {pontos} pontos")

    print("FIM DO JOGO!!!")
    print(f"A sua pontuação final foi de {pontos}")

if __name__ == "__main__":
    jogar()