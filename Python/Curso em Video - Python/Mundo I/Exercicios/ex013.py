#Ex013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Com 15% de aumento.

sal = float ( input ('Salário atual: R$ '))
aum = sal * 1.015
print ('O seu salário de R$ {:.2f}, sofrerá um ajuste de 15% e a partir de hoje passa a ser R$ {:.2f}! \nCongratulations! '.format(sal, aum))
