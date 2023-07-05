resultado = float(input("imprima o valor do resultado do exercicio contabil anterior:"))
if (resultado >= 0):
    print(f"Houve lucro de R$ %.2f" % resultado)
else:
    resultado = abs(resultado)
    print(f"Houve um prejuzo de R$ %.2f" % resultado)
    