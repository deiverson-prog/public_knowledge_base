def aumentar(v=0,t=0):
    res = v + (v * t/100)
    return res

def diminuir(v=0,t=0):
    res = v - (v * t/100)
    return res

def dobro(v=0):
    d = v * 2
    return d

def metade(v=0):
    m = v / 2
    return m

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:>8.2f}'.replace('.',',')
