#Ex015  
#Escreva um programa que pergunte a quantidade de Km percorridos 
#Por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia 
#E R$0,15 por Km rodado.

kmini = float(input('Qual foi a Km/h Inicial ? '))
kmfin = float(input('Qual foi a Km/h final ? '))
qntdias = int(input('Por quantos dias o carro foi alugado ? '))
valordia = 60 * qntdias
valorkm = 0.15 * (kmfin - kmini)

print('O valor total a pagar é de R$ {:.2f}'.format((valordia + valorkm)))


#Outra forma:

dias = int(input('Quantos dias alugados ? '))
rodados = float(input('Quantos Km/h rodados ? '))

preçodia = dias * 60
preçokm = rodados * 0.15

print('O valor total a pagar é de R$ {:.2f}.'.format((preçodia + preçokm)))