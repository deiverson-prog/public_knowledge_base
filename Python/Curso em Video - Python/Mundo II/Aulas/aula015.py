'''             LAÇOS DE REPETIÇÃO

Normalmente existem 3 estruturas ou iterações: For, While, Repit ou Duo while

Em Python usamos apenas While e For.

Cenário:
passos irregulares, pulos, pegar, moedas, maçã, troféu

enquanto verdadeiro:
    se tiver chão:
        passo
    se tiver buraco:
        pule
    se tiver moeda:
        pegue
    se tiver troféu:
        pule
        interrompa
pegue

while True:
    if tiver chão:
        passo
    if tiver buraco:
        pule
    if tiver moeda:
        pegue
    if tiver troféu:
        pula
        break
pegue'''

'''ENQUANTO ETERNO'''
'''
#Exemplos:
cont = 1
while cont <= 10:
    print(cont,'-> ', end='')
    cont += 1
print('ACABOU!')'''

'''cont = 1
while True:
    print(cont,'-> ', end='')
    cont += 1
print('ACABOU!') ''' #----> nesse código entrará em looping.

'''n = 0 
while n != 999:
    n = int(input('Digite um número: '))''' #----> vai executar a ação sem parar até digitar '999'

'''n = cont = 0 
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1'''  # ----> indicando a quantidade de números escritos

'''n = s = 0 
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))'''  #----> somará o ponto de parada ou seja o '999'.
'''
n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s)) # ----> com o break desconsiderará o ponto de parada.


''' '''F strings''' '''

n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')  #----> utilizando o 'f' minusculo no inicio de "format" e dentro do colchete a variavel.
'''

#exemplos de F str.

nome = 'Deive'
idade = 25
print(f'meu nome é {nome} e tenho {idade} anos.') #atual PY 3.6+
print('meu nome é {} e tenho {} anos.'format(nome,idade)) #antigo  PY 3
print('meu nome é %s e tenho %d anos.' % (nome, idade)) #mais antigo PY 2

nome = 'Deive'
idade = 25
Salário = 150.200
print(f'meu nome é {nome}, tenho {idade} anos e ganho R$ {Salário:.2f}.')