import random
nomes = ("Alice", "Bob", "Carl", "Daniele", "Edgard")
for n in range(5):
    nomes = random.sample (nomes, k = len(nomes))
    print(f"Na passagem de número {n + 1}, a tupla estava assim: {nomes}")