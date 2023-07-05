n  = int(input("Quantos números da sequência de Fibonacci você quer ver? "))
contador = 0
x1 = 1
x2 = 1
fb_n = 0
while (contador <= n):
    contador = contador + 1
    fib_n = x1 + x2
    print(f"{x1}")
    x1 = x2
    x2 = fib_n
