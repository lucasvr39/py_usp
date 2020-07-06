n = int(input('Digite um número inteiro: '))
resto = 0
soma = 0

# soma os dígitos do número inteiro passado pelo usuário

while n > 0:
    resto = n % 10
    soma = resto + soma
    n = n // 10
else:
    print(soma)
