dezenas = input('Digite um número inteiro: ')
semDezena = 0

# devolve a dezena do número inserido pelo usuário utilizando o método len()

if len(dezenas) < 2:

    print('O dígito das dezenas é', semDezena)
else:
    print('O dígito das dezenas é', dezenas[-2])
