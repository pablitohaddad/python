login_ok = True
numeros = 0
letras = 0
login = input("Digite aqui a sua senha: ")
normal = str.capitalize(login)
if login != normal:
    login_ok = False
    print("A sua senha deverá ter somente uma letra maiuscula no começod")
if len(login) < 6:
    login_ok = False
    print("A sua senha deverá ter no mínimo 6 caracteres")
for letra in login:
    if str.isdigit:
        numeros = numeros + 1
    if str.isalpha:
        letras = letras + 1
if letras < 3:
    login_ok = False
    print("O login deve ter no mínimo 3 letras")
if numeros < 2:
    login_ok = False
    print("O login deve ter no mínimo 2 números")
if len(login) > 10:
    login_ok = False
    print("A sua senha não pode passar de 10 caracteres")
if login_ok:
    print(f"O seu login escolhido, {login}, é válido")
else:
    print("Login inválido")