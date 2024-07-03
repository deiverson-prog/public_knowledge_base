#Ex031
#Desenvolva um programa que pergunte a distancia de uma viage em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e 
#R$ 0,45 para viagens mais longas.

#Metodo 1
distancia = float(input('qual é a distância da viagem?'))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

#Metodo 2
distancia = float(input('qual é a distância da viagem?'))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

