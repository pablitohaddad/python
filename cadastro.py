cadastros = []
print("\nBem vindo a central de cadastros!\n")

print("Digite algum dos números abaixo para inicializar o programa\n")

# Enquanto eu não der break, o programa vai rodar
while True:
   
    print("\n1- para cadastrar uma pessoa")
    print("2- para listar as pessoa(s) cadastrada(s)")
    print("3- para atualizar cadastro")
    print("4- para excluir cadastro")
    print("5- para sair\n")

    opcao = int(input("Digite o número escolhido: ")) 

    # Esse é o Creating do CRUD
    if opcao == 1:

        print("\nMuito bem, vamos inicar o cadastro\n")

        nome = input("Digite o nome: ") 
         # Na variável idade quero apenas números, e não strings.
        idade = (input("Digite a idade: "))
        while not idade.isdigit(): 
            idade = input("Digite apenas números: ")
        curso = input("Digite o curso: ")

        # Criei um dicionário e adicionei ele na lista cadastros
        cadastro = {
            "nome": nome, "idade": idade, "curso": curso
        }
        cadastros.append(cadastro)
        # Criando o arquivo TXT

        with open("cadastros.txt", "a") as arquivo:
            
            arquivo.write(f"Nome: {nome}\nIdade: {idade}\nCurso: {curso}\n\n")

        print("\nCadastro realizado com sucesso.\n")
    # O Reading do CRUD
    if opcao == 2:
        if not cadastros:
            print("\nNenhum cadastro foi realizado ainda!\n")
        else:
            print("\nOk! Esta é a lista de pessoas cadastradas:\n")

            # Colocando meus cadastrados na ordem, do primeiro cadastrado em diante
            # x = numero da pessoa // pessoa: onde poderei mudar depois 
            for x, pessoa in enumerate(cadastros):
                print(f"{x} - Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Curso: {pessoa['curso']}")

    # O Update do CRUD
    if opcao == 3:
        if not cadastros:
            print("\nNenhum cadastro foi realizado ainda!\n")
    
        numero_pessoa = int(input("Digite o número da pessoa que você quer atualizar: "))

        if numero_pessoa < 0 or numero_pessoa > len(cadastros):
            print("\nNúmero inválido\n")

        # A pessoa recebe um número de acordo com o indice do seu cadastro
        pessoa = cadastros[numero_pessoa] 
        nome = input(f"Digite o novo nome de {pessoa['nome']} : ")
        idade = input(f"Digite o novo nome de {pessoa['idade']} : ")
        curso = input(f"Digite o novo nome de {pessoa['curso']} : ")
        # Atribuindo a atualização
        pessoa["nome"] = nome
        pessoa["idade"] = idade
        pessoa["curso"] = curso
        print("A atualização foi concluida")
    
    if opcao == 4:
        if not cadastros:
            print("\nNenhum cadastro foi realizado ainda!\n")
        
        numero_pessoa = int(input("Digite o número da pessoa que você quer deletar: "))
        del cadastros[numero_pessoa]

    if opcao == 5:

        print("Programa encerrado")
        break