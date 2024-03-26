#Ex024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

#MODULO 1
City = str(input('Qual sua cidade? '))
Dcity = City.upper().split()
print('SANTO' in Dcity[0])

#MODULO 2
City = str(input('Em que cidade você nasceu? ')).strip()
print(City[:5].upper() == 'SANTO')