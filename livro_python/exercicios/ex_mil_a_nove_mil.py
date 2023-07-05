numero = 0
for x in range (1000, 9001):
    if (x % 4 == 0) and (x % 3 == 0) and ( -x % 2 == 0):
        print(f"{x} é divisivel por 3 e 4, além de ser par")
        numero = numero + 1
print(f"Há {numero} números divisiveis por 3 e 4 e pares entre 1000 e 9000")

        
