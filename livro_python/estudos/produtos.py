import pprint
produtos = {}
produtos[1] = {
    "Descrição" : "Mouse óptico sem fio",
    "Preço" : 50,
    "Estoque" : 130
}
produtos[2] = {
    "Descrição" : "Teclado USB",
    "Preço" : 42,
    "Estoque" : 100
}
produtos[3] = {
    "Descrição" : "Monitor colorido 20 pol.",
    "Preço" : 850,
    "Estoque" : 20
}
produtos[4] = {
    "Descrição" : "Par caixas de som",
    "Preço" : 90,
    "Estoque" : 17
}
pprint.pprint(produtos)