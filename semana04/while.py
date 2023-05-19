tamanho = int(input("Digite o tamanho da sequência de números: "))
valor = int(input("Digite um valor a ser informado: "))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto *= valor
    i += 1

print(f"A produto dos valores digitados é {produto}")