segundos = int(
    input('Por favor, entre com o número de segundos que deseja converter: '))

# converte os segundos para as outras unidades de medida de tempo

a = segundos // 86400
b = segundos % 86400 // 3600
c = segundos % 86400 % 3600 // 60
d = segundos % 86400 % 3600 % 60

# imprime o número de segundos convertidos em outras unidades de medida

print(str(a) + ' dias,', str(b) + ' horas,',
      str(c) + ' minutos e', str(d) + ' segundos.')
