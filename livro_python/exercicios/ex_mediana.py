numero_um= int(input("Digite aqui o primeiro numero: "))
numero_dois= int(input("Digite aqui o segundo numero: "))
numero_tres= int(input("Digite aqui o terceiro numero: "))
media_aritmetica = (numero_um * numero_dois * numero_tres) / 3

if (numero_um > numero_dois > numero_tres):
    print("A mediana é o %d" % numero_dois)
elif (numero_um > numero_tres > numero_um):
    print ("A mediana é o %d" % numero_tres)
elif (numero_dois > numero_um > numero_tres):
    print("A mediana é %d" % numero_um)
elif (numero_dois > numero_tres > numero_um):
    print("A mediana é %d" % numero_tres)
elif (numero_tres > numero_um > numero_dois):
    print("A mediana é %d" % numero_um)
elif (numero_tres > numero_dois > numero_um):
    print("A mediana é %d" % numero_dois)
elif (numero_um == numero_dois == numero_tres):
    print("A mediana é %d" % media_aritmetica)
elif (numero_um == numero_dois > numero_tres):
    print("A mediana é %d" % numero_um)
elif (numero_um > numero_dois == numero_tres):
    print("A mediana é %d" % numero_dois)
elif (numero_um == numero_dois > numero_tres):
    print("A mediana é %d" % numero_dois)

print("A média aritmética dos números é %.2f" % media_aritmetica)