import math
coordenadas_x_a = int(input("Digite aqui as coordenadas Xa: "))
coordenadas_x_b = int(input("Digite aqui as coordenadas Xb: ")) # Contas com o xa e xb

coordenadas_y_a = int(input("Digite aqui as coordenadas Ya: "))
coordenadas_y_b = int(input("Digite aqui as coordenadas Yb: ")) # ya e yb

coordenadas_z_a = int(input("Digite aqui as coordenadas Za: "))
coordenadas_z_b = int(input("Digite aqui as coordenadas Zb: ")) #za e zb

contas_x = coordenadas_x_b - coordenadas_x_a 
contas_y = coordenadas_y_b - coordenadas_y_a
contas_z = coordenadas_z_b - coordenadas_z_a # a subtração
math.pow(contas_x, 2) and math.pow(contas_y, 2) and math.pow(contas_z, 2) #pow para potência
soma = (contas_x + contas_y + contas_z) 

if (soma > 0):
    math.sqrt(soma)
    print("Os valores formam um triângulo")
elif (soma < 0):
    soma * -1
    math.sqrt(soma)
    print("Os valores formam um triângulo")
else:
    print("Essas coordenadas não formam um triângulo existênte")
 










