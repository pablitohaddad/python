idade = int(input("Qual a sua idade?: "))
tem_titulo = input("Possui titulo de eleitor? [S/N]: ")
if (idade >= 16) and (tem_titulo == "S"):
    print("Você pode votar.")
if (idade >= 18):
    print("Você é maior de idade.")
    print("Você pode comprar bebidas alcoolicas.")
