import math

a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

# calcula o delta a partir dos valores de a, b e c passados pelo usuário

delta = b ** 2 - 4 * a * c

# imprime que não há raizes quando delta for menor que 0
# calcula e imprime as raízes quando delta for maior que 0

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    print('a raiz desta equação é', int(raiz1))
else:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    print('as raízes da equação são', int(raiz2), 'e', int(raiz1))
