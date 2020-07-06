
def fatorial(n):  # função que calcula o fatorial da variável n passada como argumento
    n_fat = 1
    while n > 1:
        n_fat = n_fat * n
        n = n - 1
    return n_fat


''' função que cálcula o binômio de Newton 
 e chama a função fatorial para o cálculo dos fatoriais das variáveis passadas como argumento '''


def binomio_de_newton(n, k):
    return fatorial(n) / (fatorial(k)*fatorial(n - k))


print(binomio_de_newton(20, 10))
