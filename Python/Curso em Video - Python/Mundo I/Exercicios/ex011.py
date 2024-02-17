#Ex011
#Faça um programa que leia a largura e a altura de uma parede em metros. 
#Calcule sua area e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma àrea de 2m².

Al = float(input('Qual a altura da parede? '))
La = float(input('Qual a largura da parede? '))
area = Al * La

print('Para pintar uma area de {:.3f}m², será necessário {:.4f} litros de tinta.'.format((Al*La),(area/2)))

#Outra forma

La = float(input('Largura da parede: '))
Al = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.3f}m². \n Para pintar essa parede, você precisará de {:.4f}l de tinta.'.format(la, al, (la*al), (la*al/2)))
