alunos = []
total_individual = 0.0
continua_loop_alunos = "S"
continua_cadastro_notas = "S"
while continua_loop_alunos == "S":
    registro_alunos = {
        "nome": "",
        "notas": [],
        "media": 0.0
    }
    nome: input("Digite o nome do aluno: ")
    nome = registro_alunos["nome"]
    indice = 0
    total_individual = 0
    while continua_cadastro_notas == "S":
        indice = indice + 1
        print("Digite a nota n. %d: " %indice)
        nota = float(input())
        registro_alunos["notas"].append(nota)
        total_individual = total_individual + nota
        print("Deseja cadastrar outra nota? [S-continua/N-encerrar etapa")
        continua_cadastro_notas = str.capitalize(input())
    registro_alunos["media"] = total_individual / len(registro_alunos["notas"])
    print("Deseja cadastrar outro aluno? S-continua/ N-encerrar etapa")
    continua_loop_alunos = str.capitalize(input())
    continua_cadastro_notas = "S"
    for registro in alunos:
        if registro['alunos']['media'] >= 7.0:
            print(f"Nome: {registro['aluno']['nome']} - Notas: {registro['aluno']['notas']} - Média: {registro['aluno']['media']} - APROVADO")
        elif registro['alunos']['media'] >= 3.0:
             print(f"Nome: {registro['aluno']['nome']} - Notas: {registro['aluno']['notas']} - Média: {registro['aluno']['media']} - FARÁ PROVA FINAL")
        else:
           print(f"Nome: {registro['aluno']['nome']} - Notas: {registro['aluno']['notas']} - Média: {registro['aluno']['media']} - REPROVADO")
