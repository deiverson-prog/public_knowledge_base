#Ex010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere: US$ 1.00 = R$ 3.27

valor = float(input('Insira um valor:'))
US= 3.27

print('Com R$ {:.2f} em carteira, você consegue comprar cerca de US${:.2f}.'.format(valor, valor/US))

#outra forma:

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
US= real/3.27
Euro= real/5.33

print('Com R$ {:.2f} em carteira, você consegue comprar cerca de US$ {:.2f} ou {:.2f} Euros.'.format(real, US, Euro))
