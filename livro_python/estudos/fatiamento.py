turma = ["Pablo", "Daniela", "Carol", "Sophia", "Agnes", "Diego"]
print("Lista original: turma = ", turma)
print("\'Fatiando\' os quatro primeiros de dois em dois: turma [0:4:2] = ", turma[0:4:2])
print("Ignorando os dois primeiros da turma: ", turma[2:])
print("Ignorando o primeiro, escolhendo só mais 3 e pulando de 2 em 2:", turma[1:4:2])
print("Pegando até o quinto elemento", turma[:5])
print("Retornando todo mundo de doids em dois a partir do início (índices pares)", turma[::2])
print("Retornando todo mundo de dois em dois a partir do segundo (índices ímpares)", turma[1::2])


#Basicamente para você escolher as "fatias", use um [:::] sendo o primeiro para o início, o segundo para o fim, e o ultimo o salto que a fatia da 