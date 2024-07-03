#ESTRUTURAS CONDICIONAIS
#CONDIÇÕES SIMPLES E COMPOSTAS [ PY CONDIÇÃO SIMPLICADA ]

#EXEMPLO DO CARRO CHEGANDO AO DESTINO
#carro.siga() -> carro [objeto] siga[comando]       
#carro.esquerda()                             ||
#carro.siga()                                 ||
#carro.direita()                              ||
#carro.siga()                                 ||
#carro.direita()                              ||
#carro.siga()                                 ||
#carro.esquerda()                             ||
#carro.siga()                                 ||
#carro.pare()                                 \/

#POSSIBILIDADES
                      #carro.siga()
#se carro.esquerda()                #senão

#1 BLOCO DE COMANDOS                #2 BLOCO DE COMANDOS
#carro.siga()                       #carro.siga()
#carro.direita()                    #carro.esquerda()
#carro.siga()                       #carro.siga()
#carro.direita()                    #carro.esquerda()
#carro.esquerda()                   #carro.siga()
#carro.siga()
#carro.direita()
#carro.siga()
                      #carro.pare()

#Representação Estruturada ou Indentada

#carro.siga()           ->> colado (não indentado)
#se carro.esquerda()
#1 BLOCO DE COMANDOS
    #carro.siga()       ->> não colado (indentado)
    #carro.direita()
    #carro.siga()
    #carro.direita()
    #carro.esquerda()
    #carro.siga()
    #carro.direita()
    #carro.siga()

#senão
#2 BLOCO DE COMANDOS
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
    #carro.esquerda()
    #carro.siga()
#carro.pare()

#Se carro.esquerda()
    #bloco _V_ (bloco verdadeiro)

#Senão 
    #bloco _F_ (bloco falso)

#Para indentar sempre use a tecla TAB

#Comando no PY:
#if carro.esquerda():
    #bloco True

#else:
    #bloco False

#if para estrutura simples
#if and else para estrutura composta.

#CONDIÇÃO COMPOSTA
tempo = int(input('Quanto anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

#CONDIÇÃO SIMPLIFICADA
tempo = int(input('Quanto anos tem seu carro? '))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FIM--')

#Exemplos
#SIMPLES
nome = str(input('Qual é seu nome? '))
if nome == 'Deive':
    print('Que nome lindo você tem!')   
print('Bom dia, {}!'.format(nome))

#COMPOSTO
nome = str(input('Qual é seu nome? '))
if nome == 'Deive':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')    
print('Bom dia, {}!'.format(nome))

#CONDIÇÃO COMPOSTA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#CONDIÇÃO SIMPLIFICADA
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >=6.0 else 'ESTUDE MAIS!')