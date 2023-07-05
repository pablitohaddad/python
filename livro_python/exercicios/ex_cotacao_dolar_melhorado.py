dolar_hoje = float(input("Qual o valor do dolar hoje?: "))
quantidade_real = float(input("Qual o valor em reais que você possui?: "))

valor_convertido = quantidade_real // dolar_hoje

print("O valor de %.2f" % quantidade_real, "R$ equivale-se a %.2f" % valor_convertido, "$")