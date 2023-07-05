print("Cálculo de Volume")
comprimento = float(input("Entre com o comprimento em metros da caixa d\"água: "))
largura = float(input("Entre com o valor da largura em metros da caixa d\"água:  "))
profundidade = float(input("Entre com o valor da profundidade em metros da caixa d\"água:  "))
volume_em_m3 = comprimento * largura * profundidade
volume_em_litros = volume_em_m3 * 1000 
print("A caixa d\"água tem %.2f em litros." % volume_em_litros)