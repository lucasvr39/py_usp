n = int(input('Digite o valor de n: '))
i = 0

# imprime os primeiros n números ímpares

while i < n * 2:
    if i % 2 != 0 and i % 4 != 0:
        print(i)
        i = i + 1
    else:
        i = i + 1
