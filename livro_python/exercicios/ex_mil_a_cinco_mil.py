contador = 0
for x in range(1000, 5001):
    if (x % 3 == 0) and (x % 5 == 0):
        print(f"{x} é divisível por 3 e 5 simultaneamente")
        contador = contador + 1
print(f"Há {contador} números divisiveis por 3 e 5 entre 1000 e 5000")