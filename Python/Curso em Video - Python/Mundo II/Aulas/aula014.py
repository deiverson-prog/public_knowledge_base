'''ESTRUTURA DE REPETIÇÃO - LAÇOS PARTE 2

FOR - PRECISA DE UMA LIMITE (INICIO E FIM)

WHILE - (ENQUANTO)

EXEMPLO DA MAÇÃ  -->   ENQUANTO NÃO CHEGAR NA MAÇÃ

ESTRUTURA DE REPETIÇÃO COM TESTE LOGICO

ENQUANTO NÃO 'CHEGAR NA MAÇÃ'
   PASSO
PEGA

while not 'maçã':
    passo
pega

cenário:
passos irregulares, pulos, moedas e a maçã


enquanto não chegar na maçã:
    se tiver chão:
        passo
    se tiver buraco:
        pule
    se tive moeda:
        pegue
pegue a maçã

while not chegar na maçã:
    if tiver chão:
        de passos
    if tiver buraco:
        pule
    if tive moeda:
        pegue        
pegue a maçã

exemplo:'''

for c in range (1, 10):
    print(c, end=' ')
print('FIM')

c = 1
while c < 10:
    print(c, end=' ')
    c += 1  #or c = c + 1
print('FIM')

for c in range (1, 5):
    n = int(input('DIGITE UM VALOR: '))
print('FIM')

n = 1
while n != 0:  #flag (ponto de parada)
    n = int(input('DIGITE UM VALOR: '))
print('FIM')

R = 'S'
while R == 'S':  
    n = int(input('DIGITE UM VALOR: '))
    R = str(input('QUER CONTINUAR? [S/N] ')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))
