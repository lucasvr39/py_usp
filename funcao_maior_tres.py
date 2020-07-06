# devolver o maior número passado como argumento // três argumentos

def maximo(x, y, z):  # implementação com método MAX
    return max(x, y, z)


# OU

def maior(a, b, c):  # implementação com if/else

    z = 0

    if a > b and a > c:
        z = a
    elif b > a and b > c:
        z = b
    else:
        z = c
    return z
