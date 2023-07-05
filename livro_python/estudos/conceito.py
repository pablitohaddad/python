nota = float(input("Digite a nota do aluno: "))
if (nota >= 8.0):
    conceito = "A"
elif (nota >= 5.0):
    conceito = "B"
else:
    conceito = "C"
print("Conceito do aluno: %s" % conceito)
