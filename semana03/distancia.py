import math

x1 = float(input("Digite a coordenada do primeiro ponto X: "))
y1 = float(input("Digite a coordenada do primeiro ponto Y: "))
x2 = float(input("Digite a coordenada do segundo ponto X: "))
y2 = float(input("Digite a coordenada do segundo ponto Y: "))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if distancia >= 10:
    print("longe")
else:
    print("perto")