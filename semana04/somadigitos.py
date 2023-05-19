numero = int(input("Digite um numero: "))

soma = 0
i = 0
restoDivisao = 0

while numero != 0:
    restoDivisao = numero % 10
    soma += restoDivisao
    numero = numero // 10
    i += 1

print(soma)