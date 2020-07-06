import math

# imprime a média aritmética das notas passadas pelo usuário

primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))
terceiraNota = float(input('Digite a terceira nota: '))
quartaNota = float(input('Digite a quarta nota: '))

mediaNotas = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

print('A média aritmética é:', mediaNotas)
