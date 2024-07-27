def aumentar(v,t):
#    aum = (v * ((t/100)+1))
#    return v + aum 
    res = v + (v * t/100)
    return res

def diminuir(v,t):
    res = v - (v * t/100)
    return res

def dobro(v):
    d = v * 2
    return d

def metade(v):
    m = v / 2
    return m
