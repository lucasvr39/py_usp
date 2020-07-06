import math

a = float(input('Digite um número inteiro: '))
b = float(input('Digite outro número inteiro: '))
c = float(input('Digite mais um número inteiro: '))
d = float(input('Digite mais um número inteiro: '))

# calcula a distância entre os pontos inseridos pelo usuário no plano cartesiano

distancia = math.sqrt((a - b) ** 2 + (c - d) ** 2)

# informa ao usuário se os pontos estão perto ou longe um dos outros

if distancia >= 10:
    print('longe')
else:
    print('perto')
