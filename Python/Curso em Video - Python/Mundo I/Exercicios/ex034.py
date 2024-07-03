#Ex034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

#Metodo 1
salário = float(input('qual é o salário do funcionário? R$ '))
if salário <=2500:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(salário, novo))

#Metodo 2
salário = float(input('qual é o salário do funcionário? R$ '))
if salário <=2500:
    novo = salário * 1.15
else:
    novo = salário * 1.10
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(salário, novo))
