continua = "S"
somatorio = 0.0
quantidade = 0
while(True):
    preco = float(input("Entre com o preço do próximo produto: "))
    somatorio = somatorio + preco
    continua = input("Acrescentar mais produtos? (S/N)")
    if(continua != "S"):
        break
print("O valor total dos produtos é R$ %.2f" % somatorio)
