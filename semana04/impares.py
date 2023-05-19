numero = int(input("Digite um numero: "))
i = 0
impar = 1

while (impar <= numero):
    if i % 2 != 0:
        print(i)
        impar += 1
    i += 1