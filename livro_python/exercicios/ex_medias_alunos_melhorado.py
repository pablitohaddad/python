nomes = ["", "", "", "", ""]
notas = [0.0, 0.0, 0.0, 0.0, 0.0]
for contador in range(5):
    print(f"Entre com o nome do aluno: {contador + 1}")
    nomes[contador] = input()
    print(f"Entre com a nota do aluno {nomes[contador]}:")
    notas [contador] = float(input())
media = (notas [0] + notas [1]+ notas [2]+ notas [3]+ notas [4]) / 5
print ("A média dos alunos é: {media}")
