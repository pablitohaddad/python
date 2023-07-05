continua = 'S'
somatorio = 0.0
quantidade = 0 
while(continua == "S"):
    preco = float(input("Entre com o preço do próximo produto: "))
    somatorio = somatorio + preco
    continua = input("Acrescentar produtos? (S/N) ")
print("O valor total dos produtos é R$ %.2f" % somatorio)