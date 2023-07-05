camisetas = ["azul", "vermelha", "amarela"]
shorts = ["branco", "preto"]
x = 0
y = 0
for x in range (3):
    for y in range(2):
        print(f"Você pode combinar uma camiseta {camisetas[x]} com um short {shorts[y]}")

camisetas_02 = ["azul", "vermelha", "amarela"]
shorts_02 = ["branco", "preto"]
for cor_camiseta in camisetas_02:
    for cor_short in shorts_02:
        print(f"Você pode combinar uma camiseta {cor_camiseta} com um short {cor_short}")
