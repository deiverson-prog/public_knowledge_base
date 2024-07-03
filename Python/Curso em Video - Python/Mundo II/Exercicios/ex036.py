#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMOS BANCÁRIO PARA A COMPRA DE UMA 
#CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM 
#QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL. SABENDO QUE ELA NÃO PODE EXCEDER 30% DO 
#SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.


#METODO 1

casa = float(input('Qual o valor do imóvel? '))
comprador = float(input('Quanto você ganha? '))
anos = int(input('Em quantos anos será pago? '))
casa_mês = casa/(anos*12)
percentual = 30
salario_ap = comprador * (percentual/100)

if salario_ap >= casa_mês:
    print('Sua prestação mensal custará R$ {:.2f} \n para pagar em {} anos.'.format(casa_mês,anos))
    print('Parabéns! O seu empréstimo foi aprovado!')
else:
    print('Oh não! Seu empréstimo foi negado! \nAumente sua linha de crédito e retorne futuramente!')


#METODO 2
casa = float(input('Qual o valor do imóvel? R$ '))
comprador = float(input('Quanto você ganha? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
minimo = comprador *30 / 100
print('Para comprar uma casa no valor de R$ {:.2f} em {} anos.'.format(casa,anos), end='')
print('A prestação será de R$ {:.2f}'.format (prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')