import math

# calcula as raiz soma implementando bhaskara em uma função


def raiz_soma(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c))

# calcula as raiz subtração implementando bhaskara em uma função


def raiz_sub(a, b, c):
    return (-b - math.sqrt(b ** 2 - 4 * a * c))


print(raiz_soma(2, 6, 1))
print(raiz_sub(2, 6, 1))
