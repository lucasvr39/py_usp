numero = int(input('Digite um número inteiro: '))

''' converte o inteiro para um string a fim de armazenar o caractere através da posição de dezena 
quand o numero for maior que 10 '''

dezena = str(numero)[-2]

# devolve a dezena do número inserido pelo usuário

if numero < 10:
    print('O dígito de dezenas é 0')
else:
    print('O dígito das dezenas é:', dezena)
