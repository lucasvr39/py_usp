# recebe um número inteiro positivo e verifica se há dígitos adjacentes iguais

n = int(input('Digite um número inteiro: '))
x = 0
y = 0
adj = True

while n > 0:
    x = n % 10
    n = n // 10
    y = n % 10
    if x == y:
        adj = False

if adj:
    print('não')
else:
    print('sim')
