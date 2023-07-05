lista_frutas = []
lista_frutas.append("Melância")
lista_frutas.append("Mamão")
lista_frutas.append("Abacate")
lista_frutas.append("Maça")
lista_frutas.append("Pera")
lista_frutas.remove("Melância")
print(lista_frutas) 

uma_fruta = input("Digite uma fruta: ")

if uma_fruta not in lista_frutas:
    print("A fruta não esta na lista")
else:
    print("A fruta está na lista")