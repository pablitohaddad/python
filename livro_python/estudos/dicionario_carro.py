print("Criando um dicionário para armazenar os dados de um carro...")
carro = {
    "marca": "Hyundai",
    "modelo": "Hb20", 
    "ano": 2015,
    "motorizacao": 1.6,
    "cambio": "automárico",
    "acessorios": [],
}
print("Dicionario criado!", carro)
carro["ano"] = 2018
carro["modelo"] = "HB20 R-Spec"
print("Troquei de carro - comprei um mais novo!", carro)
print("Colocando acessórios no carro:")
carro["acessorios"] = ["alarme"]
print("instalei um alarme novo:", carro)
carro["acessorios"].append("som")
print("Instalei um som no carro", carro)
carro["acessorios"][1] = "som diferente"
print("Troquei o modelo do som: ", carro)

del carro["acessorios"]
print(carro)