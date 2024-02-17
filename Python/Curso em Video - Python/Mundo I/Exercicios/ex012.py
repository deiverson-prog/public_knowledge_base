#Ex012
#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

prod = float ( input ('Indique o preço do produto: R$ '))
desc = prod * 0.05
newprod = prod - desc
print ('Este produto custa: R$ {:.2f}, Devido ao grande saldão de desconto de 5% em toda a loja.\nLeve por: R$ {:.2f}!'.format(prod, newprod))


#Outra forma
preço = float ( input ( 'Qual o preço do produto ? R$ '))
novo = preço - (preço * 5 / 100)

print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(preço, novo))