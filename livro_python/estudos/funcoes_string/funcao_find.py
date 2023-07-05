frase =  "Ser ou não ser, eis a questão"
print("Usando o método da classe: ")
print("Procurando pela substring \'algo\' dentro da frase %s..." % frase)
substring = "algo"
posicao = str.find(frase, substring)
if(posicao != -1):
    print(f"Escontrada na posição {posicao}")
else:
    print("Substring não encontrada")
print("Procurnaodo pela substring \'ser\' dentro da frase %s..." % frase)
substring_1 = "ser"
posicao_1 = str.find(frase, substring_1)
if(posicao_1 != -1):
    print(f"Encontrada na posição {posicao_1}")
else:
    print("Substring não encotrada")