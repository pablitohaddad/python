print("Criando uma lista...")
lista_documentos = ["doc1", "doc2", "doc3", "doc4"]

print("Copiando da forma errada...")
lista_tpm = lista_documentos
print(f"lista_documentos = {lista_documentos}")
print(f"lista_tpm        = {lista_tpm}")

print("Alterando um elemento de lista_documentos e verificando novamente")
lista_documentos[2] = "doc10"
print(f"lista_documentos = {lista_documentos}")
print(f"lista_tpm        = {lista_tpm}")

print("Resolvendo o problema...")
lista_tpm = lista_documentos.copy()
print("Alterando um elemento de lista_documentos e verificando mais uma vez...")
lista_documentos[2] = "doc3"

print(f"lista_documentos = {lista_documentos}")
print(f"lista_tpm        = {lista_tpm}")
