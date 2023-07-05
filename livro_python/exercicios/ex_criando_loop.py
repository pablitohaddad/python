poema = "Soneto de Fidelidade \n\n"
poema += "De tudo ao meu amor serei atento antes\n"
poema += "E com tal zelo, e sempre, e atento\n"
poema += "Que mesmo em face do maior encanto\n"
poema += "Dele se encante mais meu pensamento\n\n"
poema += "Quero vivê-lo em cada vão momento\n"
poema += "E em seu louvou hei de espalhar meu canto\n"
poema += "E rir meu riso e derramar meu pranto \n"
poema += "Ao seu pesar ou seu contentamento\n\n"
poema += "Vinicius de morais"
print('\n' *  100)
linha = 0
coluna = 0
for letra in poema:
    coluna = coluna + 1
    linha = linha + 1
    if letra == "\n":
        coluna = 0
        linha = linha + 1
        if (str.isupper(letra)):
            print("linha: ", letra, "coluna: ", coluna, "letra: ", letra, "Maiúscula")
        else:
            print("linha: ", linha, "coluna: ", coluna, "letra: ", letra)
 




