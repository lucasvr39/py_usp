nome = input('Digite o nome do cliente: ')
diaVencimento = input('Digite o dia de vencimento: ')
mesVencimento = input('Digite o mês de vencimento: ')
valor = input('Digite o valor da fatura: ')

# concatena os dados inserido pelo usuário para devolver a mensagem da fatura do cartão

print('Olá,', nome +
      '\nA sua fatura com vencimento em', str(diaVencimento) + ' de', mesVencimento +
      ' no valor de R$', valor + ' está fechada.')
