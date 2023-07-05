# Aqui vou fazer as escolhas de trás para frente
turma = ["Pablo", "Daniela", "Carol", "Sophia", "Agnes", "Diego"]

print("Sala original: ")
for alunos in turma:
    print(alunos, end=" ")

print("\n\'Fatiando\' os quatro primeiros de dois em dois, na ordem inversa")
for indice in range(3, 0, -2):
    print(turma[indice], end=" ")

print("\n Tirar o ultimo número e escolher somente 3 para tirar 2 em 2")
for indice in range(2, 5, 2 ):
    print(turma[indice], end=" ")

print("\n Pegando os cinco ultimos elementos, na ordem inversa:")
for indice in range(5, 0, -1):
    print(turma[indice], end=" ")

print("\nRetornando de 2 em 2 a partir do fim (ínices pares):")
for indice in range (len(turma)-2, -1, -2):
    print(turma[indice], end=" ")

print("\nRetornando de dois em dois a partir do fim (índices ímpares):")
for indice in range(len(turma) -1, -1, -2):
    print(turma[indice], end=" ")
    