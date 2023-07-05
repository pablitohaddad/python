lista = ["A_lista", "B_lista", "C_lista"]
tupla = ("A_tupla", "B_tupla", "C_tupla")
dicionario = {"A_dicionario": "1", "B_dicionario": "2", "C_dicionario": "3"}
separador = ' * '

print("Lista: ", lista)
print("Tupla: ", tupla)
print("Dicionario: ", dicionario)

print("Agora, apois o join")
print("Lista: ", str.join(separador, lista))
print("Tupla: ", str.join(separador, tupla))
print("dicionario: ", str.join(separador, dicionario))
