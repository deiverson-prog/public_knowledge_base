#ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, 
#CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

#À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#À VISTA NO CARTÃO: 5% DE DESCONTO
#EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
#3X OU MAIS NO CARTÃO: 20% DE JUROS

#METODO 1 
print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1
    total = preco - (preco *0.1)
elif opcao == 2
    total = preco - (preco * 0.05)
elif opcao == 3
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R$ {:.2} SEM JUROS'.format(parcela))
elif opcao == 4
    total = preco + (preco* 0.2)
    totalparcelas= int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R$ {:.2} COM JUROS'.format(totalparcelas,parcela))
else:
    total = preco
    print('Opção INVALIDA tente novamente!')    
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco,total))
 

