lista_duplicada = ["Pablo", "Daniela", "Pablo", "Sophia", "Daniela", "Sophia"]
print(f"O conteúdo original da lista é = {lista_duplicada}")

print("Agora, convertendo a lista para um conjunto...")
s1 = set(lista_duplicada)
print("Convertendo o conjunto em uma lista sem duplicações")
lista1 = list(s1)

print(f"Conteúdo da lista sem valores duplicados: {lista1}")
