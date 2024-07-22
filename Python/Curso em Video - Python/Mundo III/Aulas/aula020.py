''' FUNÇÕES

FUNÇÃO = ROTINA

EXEMPLOS DE FUNÇÕES NO PY ->  LEN(), INPUT(), PRINT(), INT, FLOAT()...

EXEMPLO DE CRIAÇÃO PRÓPRIA DE FUNÇÃO OU 'DEF' - função personalizada.

mostrarlinha(-------)

--------------------------------
        SISTEMA DE ALUNOS
--------------------------------

--------------------------------
    CADASTRO DE FUNCIONÁRIOS
--------------------------------

--------------------------------
        ERRO DO SISTEMA
--------------------------------

 TRABALHOSO E REPETITIVO = ROTINA

escrevendo código:

print('--------------------------------')
print('        SISTEMA DE ALUNOS       ')
print('--------------------------------')

print('--------------------------------')
print('    CADASTRO DE FUNCIONÁRIOS    ')
print('--------------------------------')

print('--------------------------------')
print('        ERRO DO SISTEMA         ')
print('--------------------------------')

contruindo a rotina:
def mostralinha():              #todas as funções são identificadas com parenteses no final.
    print('--------------------------------')

mostralinha():
print('        SISTEMA DE ALUNOS       ')
mostralinha():

mostralinha():
print('    CADASTRO DE FUNCIONÁRIOS    ')
mostralinha():

mostralinha():
print('        ERRO DO SISTEMA         ')
mostralinha():

PARAMETROS:
def mensagem(msg):              #todas as funções são identificadas com parenteses no final.
    print('--------------------------------')
    print(msg)
    print('--------------------------------')

mensagem('SISTEMA DE ALUNOS')
--------------------------------
        SISTEMA DE ALUNOS       
--------------------------------

mensagem('CADASTRO DE FUNCIONÁRIOS')
--------------------------------
    CADASTRO DE FUNCIONÁRIOS    
--------------------------------

mensagem('ERRO DO SISTEMA')
--------------------------------
        ERRO DO SISTEMA         
--------------------------------'''

'''PARTE PRATICA'''
#EXEMPLO        #TIPO DE ROTINA PRATICA    
A = 4           #soma(4, 5)
B = 5
S = A+B
print(S)

A = 8           #soma(8, 9)
B = 9
S = A+B
print(S)

A = 2           #soma(2, 1)
B = 1
S = A+B
print(S)

def soma (a,b):
    s = a+b
    print(s)


#PROGRAMA PRINCIPAL
soma(4, 5)
soma(8, 9)
soma(2, 1)
#soma(4) #retornará erro, pois a definição da função neste caso exige dois parametros

def soma (a,b):
    print(f'A={a} e B={b}')
    s = a+b
    print(f'A soma A + B = {s}')


#PROGRAMA PRINCIPAL
soma(a=4, b=5)

soma(b=4, a=5) #inversão permitida

soma(5, 4)

#soma(b=4, 5) #retornará erro de incoerência

#soma(5, 4, 2) #retonará erro de parametros excedidos de acordo com a função.

#EMPACOTAR PARAMETROS#

def contador (* núm):   # * 'coringa' -> significa desempacotar (vários parametros sem padrão ou limite)
    for valor in núm:
        print(f'{valor} ',end='') #função criada com for

def contador (* núm):
    tam = len(núm)
        print(f'recebi os valores {núm} e são ao todo {tam} números') #função criada com len

contador(5,7,3,1,4) #tuplas
contador(8,4,7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)