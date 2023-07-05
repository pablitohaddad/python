while(True):
    letra = input("Digite alguma letra diferente de X (Q para sair) ")
    if(letra == "X"):
        continue
    elif(letra == "Q"):
        break
    else:
        print(f"Você digitou {letra}")
print("Programa encerrado!")

