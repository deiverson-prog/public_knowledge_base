def aumentar(preço=0,taxa=0,formato=False):
    '''
    -> Calcula o aumento de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0,taxa=0,formato=False):
    '''
    -> Calcula a redução de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0,formato=False):
    '''
    -> Calcula o dobro de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer dobrar.
    :param formato: quer a saída formatada ou não?
    :return: o valor dobrado, com ou sem formato.
    '''    
    res = preço * 2
    return res if not formato else moeda(res)

def metade(preço=0,formato=False):
    '''
    -> Calcula a metade de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer dividir pela metade.
    :param formato: quer a saída formatada ou não?
    :return: o valor dividido pela metade, com ou sem formato.
    '''    
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    '''
    -> Formata um valor com os parametros do Real Brasileiro
    :param preço: recebe um valor.
    :param moeda: Cifrão ou moeda local.
    :return: o valor formatado com duas casas decimais e virgula ao final.
    '''    
    return f'{moeda} {preço:>.2f}'.replace('.',',')

def resumo(preço=0,taxaa=10,taxar=5):
        print('-'*35)
        print('RESUMO DO VALOR'.center(35))
        print('-'*35)
        print(f'Preço analisado: \t{moeda(preço)}')   #\t tabulação
        print(f'o Dobro do preço: \t{dobro(preço, True)}')
        print(f'A metade do preço: \t{metade(preço, True)}')
        print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa, True)}')
        print(f'{taxar}% de redução: \t{diminuir(preço,taxar, True)}')
        print('-'*35)