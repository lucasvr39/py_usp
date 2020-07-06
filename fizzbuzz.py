x = int(input('Digite um número inteiro: '))

# se o input do usuário for múltiplo de 3 e 5, imprime FizzBuzz, caso contrário imprime o input

if x % 3 == 0 and x % 5 == 0:
    print('FizzBuzz')
else:
    print(x)
