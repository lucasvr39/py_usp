vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]  # array das vogais

# devolve True quando o argumento passado for vogal ou False quando for consoante ou um número


def vogal(letra):
    if letra in vogais:
        return True
    else:
        return False


print(vogal("a"))
