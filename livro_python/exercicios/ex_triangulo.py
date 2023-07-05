numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))
numero_tres = int(input("Digite o terceiro número: "))

if numero_um > numero_dois > numero_tres or numero_um > numero_tres > numero_dois or numero_um > numero_dois == numero_tres:
    hipotenusa = numero_um  
    cateto_a = numero_dois
    cateto_b = numero_tres
elif numero_dois > numero_um > numero_tres or numero_dois > numero_tres > numero_um or numero_dois > numero_tres == numero_um:
    hipotenusa = numero_dois
    cateto_a = numero_tres
    cateto_b = numero_um
elif numero_tres > numero_um > numero_dois or numero_tres > numero_dois > numero_um or numero_tres > numero_um == numero_dois:
    hipotenusa = numero_tres
    cateto_a = numero_dois
    cateto_b = numero_um


hipotenusa = cateto_a ^ 2 + cateto_b ^ 2