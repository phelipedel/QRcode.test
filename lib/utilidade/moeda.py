def metade(p,formato=False):
    s = p / 2
    return s if formato is False else moeda(s)



def dobro(p):
    s = p * 2
    return s


def aumento(p, a):
    s = p + (p * a / 100)
    z = s - p
    return z


def diminuir(p, a):
    s = p - (p * a / 100)
    z = p + s
    return z, p


def moeda(preco= 0, moeda='R$'):
   return f'{moeda}{preco:>.2f}'.replace('.',',')
