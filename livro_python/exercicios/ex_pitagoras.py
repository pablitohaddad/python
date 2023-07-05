import math
lado1 = float(input("informe o primeiro lado: "))
lado2 = float(input("informe o segundo lado lado: "))
lado3 = float(input("informe o terceiro lado: "))
if (lado1 > lado2) and (lado1 > lado3) and (lado1 < (lado2 + lado3)):
    hipotenusa = lado1
    cateto_1 = lado2
    cateto_2 = lado3
    forma_triangulo = True
elif (lado2 > lado1) and (lado2 > lado3) and (lado2 < (lado1 + lado3)):
    hipotenusa = lado2
    cateto_1 = lado1
    cateto_2 = lado3
    forma_triangulo = True
elif (lado3 > lado2) and (lado3 > lado1) and (lado3 < (lado1 +lado2)):
    hipotenusa = lado3
    cateto_1 = lado1
    cateto_2 = lado2
    forma_triangulo = True
if forma_triangulo:
    if ((hipotenusa**2) == (cateto_1**2) + (cateto_2**2)):
        print(f"Os segmentos formam um triângulo retângulo de hipotenusa {hipotenusa} e catetos {cateto_1} e {cateto_2}")
    else:
        print("Os segmentos NAO formam um triângulo retângulo")
else:
    print("Os segmentos não formam triângulo algum.")
                       
