turma = []
lista_alunos = ["Leandro", "Marcus", "Pablo"]
lista_alunas = ["Daniela", "Sophia", "Carol"]
print("Turma vazia", turma)
print("Lista dos alunos: ", lista_alunos)
print("Lista das alunas: ", lista_alunas)
print("Primeiro vamos adicionar as damas:")
turma.extend(lista_alunas)
print(turma)
print("Agora os cavalheiros:")
turma.extend(lista_alunos)
print(turma)