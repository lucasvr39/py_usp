n = int(input('Digite o valor de n: '))
f = 1

# calculo o fatoria do numero inserido pelo usuário

while n > 1:
    f = f * n
    n = n - 1
else:
    print(f)
