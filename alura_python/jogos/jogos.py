import forca
import jogo_advinhacao

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo você quer jogar?\n"))

    if jogo == 1:

        print("Jogo da forca")
        forca.jogar()

    elif jogo == 2:

        print("Jogo da advinhação")
        jogo_advinhacao.jogar()
    else:
        print("Comando inválido")

if __name__ == "__main__":
    escolhe_jogo()

