#ESTRUTURAS DE CONTROLE
#CONDIÇÕES ANINHADAS    ANINHAR(JUNTAR UMA NA OUTRA OU COLOCAR UMA DENTRO DA OUTRA) FORMA DE NINHO.

#POSSIBILIDADES
#carro.siga()
#se carro.esquerda()                
    #carro.siga()
    #carro.direita()
    #carro.siga()
    #carro.direita()
    #carro.esquerda()
    #carro.siga()
    #carro.direita()
    #carro.siga()
#senão se carro.direita()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
#senão
    #carro.siga()
#carro.pare()

#EM PY

#3 possibilidades
#carro.siga()
#if carro.esquerda():              
    #carro.siga()
    #carro.direita()
    #carro.siga()
    #carro.direita()
    #carro.esquerda()
    #carro.siga()
    #carro.direita()
    #carro.siga()
#elif carro.direita():
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
#else:
    #carro.siga()
#carro.pare()

#4 possibilidades (ao incluir outra condição, basta incluir outro elif)
#carro.siga()
#if carro.esquerda():              
    #carro.siga()
    #carro.direita()
    #carro.siga()
    #carro.direita()
    #carro.esquerda()
    #carro.siga()
    #carro.direita()
    #carro.siga()
#elif carro.direita():
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
#elif carro.ré():    
#else:
    #carro.siga()
#carro.pare()

#CONDIÇÃO SIMPLES
nome = str(input('Qual é o seu nome?'))
if nome == 'Deive':
    print('Que nome sexy!')
print('Tenha um bom dia, {}!'.format(nome))

#CONDIÇÃO COMPOSTA
nome = str(input('Qual é o seu nome?'))
if nome == 'Deive':
    print('Que nome sexy!')
else:
    print('Que nome comum!')
print('Tenha um bom dia, {}!'.format(nome))

#CONDIÇÃO COMPOSTA (ESTRUTURA CONDICIONAL ANINHADA)
nome = str(input('Qual é o seu nome?'))
if nome == 'Deive':
    print('Que nome sexy!')
elif nome == 'Deivid' or nome == 'Lucas' or nome == 'Danubia' or nome == 'Daiana'
    print('Seu nome é bem familiar!')
elif nome in 'SOUZA MOURA SILVA OLIVEIRA PEREIRA'
    print('Que nome de pobre você tem!')
else:
    print('Que nome comum!')
print('Tenha um bom dia, {}!'.format(nome))

#CONDIÇÃO COMPOSTA (ESTRUTURA CONDICIONAL ANINHADA SEM ELSE) - #RETIRANDO O ELSE, SEGUIMOS COM A ESTRUTURA NORMALMENTE.
nome = str(input('Qual é o seu nome?'))
if nome == 'Deive':
    print('Que nome sexy!')
elif nome == 'Deivid' or nome == 'Lucas' or nome == 'Danubia' or nome == 'Daiana'
    print('Seu nome é bem familiar!')
elif nome in 'SOUZA MOURA SILVA OLIVEIRA PEREIRA'
    print('Que nome de pobre você tem!')
print('Tenha um bom dia, {}!'.format(nome))

