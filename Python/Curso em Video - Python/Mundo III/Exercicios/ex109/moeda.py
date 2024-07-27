def aumentar(v=0,t=0,formato=False):
    res = v + (v * t/100)
    return res if formato is False else moeda(res)

def diminuir(v=0,t=0,formato=False):
    res = v - (v * t/100)
    return res if formato is False else moeda(res)

def dobro(v=0,formato=False):
    d = v * 2
    return d if not formato else moeda(d)

def metade(v=0,formato=False):
    m = v / 2
    return m if not formato else moeda(m)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:>.2f}'.replace('.',',')
