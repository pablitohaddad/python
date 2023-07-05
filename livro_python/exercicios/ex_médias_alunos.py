nomes = (['', '', '', '', ''])
notas = ([0.0, 0.0, 0.0, 0.0, 0.0])

nome_0 = input("Entre com o nome do aluno: ")
nota_0 = float(input("Coloque a nota do aluno: "))
nomes [0] = nome_0
notas [0] = nota_0

nome_1 = input("Entre com o nome do aluno: ")
nota_1 = float(input("Coloque a nota do aluno: "))
nomes [1] = nome_1
notas [1] = nota_1

nome_2 = input("Entre com o nome do aluno: ")
nota_2 = float(input("Coloque a nota do aluno: "))
nomes [2] = nome_2
notas [2] = nota_2

nome_3 = input("Entre com o nome do aluno: ")
nota_3 = float(input("Coloque a nota do aluno: "))
nomes [3] = nome_3
notas [3] = nota_3

nome_4 = input("Entre com o nome do aluno: ")
nota_4 = float(input("Coloque a nota do aluno: "))
nomes [4] = nome_4
notas [4] = nota_4

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4]) / 5
print("A média dos alunos é %.2f" % media )