def computador_escolhe_jogada(n, m):
    pcRetira = 1
    while pcRetira != m:
        if(n - pcRetira) % (m+1) == 0:
            return pcRetira
        else:
            pcRetira += 1

    return pcRetira


def usuario_escolhe_jogada(n, m):
    jogValida = False
    while not jogValida:
        jogRemove = int(input("Quantas peças você vai tirar? "))
        if jogRemove > m or jogRemove < 1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jogValida = True

    return jogRemove

def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    pc = False

    if n % (m+1) == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        pc = True

    while n > 0:
        if pc:
            pcRemove = computador_escolhe_jogada(n, m)
            n = n - pcRemove
            if pcRemove == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou {} peças".format(pcRemove))
            pc = False
        else:
            jogRemove = usuario_escolhe_jogada(n, m)
            n = n - jogRemove
            if jogRemove == 1:
                print("Você tirou uma peça")
            else:
                print("Você tirou {} peças".format(jogRemove))
            pc = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if n != 0:
                print("Agora restam {} peças no tabuleiro.".format(n))

    print("Fim do jogo! O computador ganhou!")

print("1 - para jogar uma partida isolada")

tipoPartida = int(input("2 - para jogar um campeonato "))

if tipoPartida == 2:
    print("Voce escolheu um campeonato!")
else:
    if tipoPartida == 1:
        partida()

def campeonato():
    numRorada = 1
    while numRorada <= 3:
        print("**** Rodada {} ****".format(numRorada))
        partida()
        numRorada += 1

partida()