''' n é o número de peças inicias e m é o número máximo de pças a serem retiradas numa rodada
se n % m + 1 == 0 o usuário inicia a partida, else o computador inicia
para ganhar, o computador deve deixar sempre um número de pças restantes que seja múltiplo de m + 1 
ou tirar o número máximo de peças possíveis que corresponde a m '''

# jogada do computado deixando sempre um múltiplo de m + 1 na mesa ou retirando valor igual a m


def computador_escolhe_jogada(n, m):
    computador_escolhe = 1
    while ((n - computador_escolhe) % (m + 1)) != 0:
        computador_escolhe = computador_escolhe + 1
    else:
        n = n - computador_escolhe
    return computador_escolhe

# input do usuário para definir a jogada dele que não pode ser maior que m


def usuario_escolhe_jogada(n, m):
    jogador_escolhe = int(input("Quantas peças você vai tirar? "))
    while jogador_escolhe > m or jogador_escolhe <= 0 or jogador_escolhe > n:
        print("Jogada inválida! Tente de novo!")
        jogador_escolhe = int(input("Quantas peças você vai tirar? "))
    else:
        n = n - jogador_escolhe
    return jogador_escolhe

# função que starta a partida e recebe o input do usuário que escolhe o n de peças no jogo


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    rodada_computador = True
    pecas_retiradas = int

    if (n % (m + 1)) == 0 and m < n: # define quem começa a partida de acordo com a estratégia vencedora
        rodada_computador = False  
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
        
    while n > 0:  # chama as jogadas alternadamente até as peças acabarem no tabuleiro
        if rodada_computador:
            pecas_retiradas = computador_escolhe_jogada(n, m)
            rodada_computador = False
            print("\nO computador retira {} do tabuleiro.".format(pecas_retiradas))
        else:
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            rodada_computador = True
            print("\nVocê retirou {} do tabuleiro.".format(pecas_retiradas))

        n = n - pecas_retiradas
        # estado atual do jogo
        print("Restam apenas {} no tabuleiro.\n".format(n))

    if rodada_computador == True:
        print("Vocẽ venceu!\n")
        return 0
    else:
        print("Game Over! O computador venceu!\n")
        return 1

# função que roda partida() 3x e retorna o placar no fim quando a escolha de modalidade for campeonato


def campeonato():
    ponto_computador = 0
    ponto_usuario = 0

    for i in range(3):
        print("**** Rodada ", i + 1, "****\n")
        placar = partida()
        if partida == 0:
            ponto_usuario = ponto_usuario + 1
        else:
            ponto_computador = ponto_computador + 1
    else:
        print("**** Fim do campeonato! ****\n")

    return print("Placar: Você ", ponto_usuario, "x", ponto_computador, "Computador")

# função que pede o input do usuário para definir entra partida única ou campeonato


def modalidade():
    escolhe_modalidade = int(input("""Bem-vindo ao jogo do NIM! Escolha!:
    \n1 - para jogar uma partida isolada
    \n2 - para jogar um campeonato
    """))

    # chama a função de acordo com a modalidade escolhida pelo usuário no input acima
    while escolhe_modalidade != 1 or escolhe_modalidade != 2: 
        if escolhe_modalidade == 1:
            print("\nVocê escolheu partida única!\n")
            partida()
            break
        elif escolhe_modalidade == 2:
            print("\nVocê escolheu um campeonato!\n")
            campeonato()
            break
        else:
            print("Opção inválida")


modalidade()
