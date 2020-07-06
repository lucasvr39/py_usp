# calcula a fórmula de bhaskara a partir dos inputs do usuários para as variáveis a, b e c
import math

a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    print ('a raiz desta equação é', int(raiz1))
else:
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)  
    print('as raízes da equação são', int(raiz2), 'e', int(raiz1))