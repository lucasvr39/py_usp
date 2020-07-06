# testa o argumento para ver se é primo

def ePrimo(k):
    for i in range(2, k):
        if k % i == 0:
            return False
            break
    return True

# devolve o maior número primo se até n se o n não for primo


def maior_primo(n):
    maiorPrimo = 0
    if ePrimo(n) == True:
        return n
    else:
        for i in range(2, n):
            if ePrimo(i) == True:
                maiorPrimo = i
        return maiorPrimo
