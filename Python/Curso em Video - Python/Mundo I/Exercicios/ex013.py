#Ex013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Com 15% de aumento.

sal = float ( input ('Salário atual: R$ '))
aum = sal * 1.15
print ('O seu salário de R$ {:.2f}, sofrerá um ajuste de 15% e a partir de hoje passa a ser R$ {:.2f}! \nCongratulations! '.format(sal, aum))


#outra forma:

Sal= float(input('Qual o salário de um funcionário? R$ '))
Aum = Sal + (Sal * 15 / 100) 
print ('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}! \nCongratulations! '.format(Sal, Aum))