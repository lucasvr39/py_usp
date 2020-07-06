n = int(input('Digite o valor de n: '))
primo = True
i = 2
resto = 0

# testa o número dado pelo usuário para identificar se é primo ou não

while i < n - 1 and primo == True:
    resto = n % i
    if resto == 0 or n == 2:
        primo = False
    else:
        i = i + 1

# imprime se o número dado pelo o usuário é primo ou não primo

if primo == True:
    print('primo')
else:
    print('não primo')
