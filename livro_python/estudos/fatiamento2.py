turma = ["Pablo", "Daniela", "Carol", "Sophia", "Agnes", "Diego"]
print("Lista original:")
for aluno in turma:
    print(aluno, end=" ")
print("\n\'Fatiando\' os quatro primeiros elementos de dois em dois: ")
for indice in range (0, 4, 2):
    print(turma[indice], end=" ")
print("\nIgnorando o primeiro, escolhendo só mais 3 e pulando de 2 em 2:")
for indice in range (1, 4, 2):
    print(turma[indice], end= " ")
print("\n Tirando os dois primeiros, escolhendo até o 5 elemento e pulando de dois em dois: ")
for indice in range(2, 6, 1):
    print(turma[indice], end= " ")
