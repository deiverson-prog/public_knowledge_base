#Ex029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizem que ele foi multado.
#A multa vai custa R$ 7,00 por cada Km acima do limite.

#Metodo 1
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade >80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa no valor de R${.:2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')