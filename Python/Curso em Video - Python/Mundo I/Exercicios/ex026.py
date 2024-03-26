#Ex026
#Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A";
# - Em que posição nela aparece a primeira vez;
# - Em que posição ela aparece a última vez.

#METODO 1
frase = str(input('Digite uma frase: ')).strip()
print(frase.lower().count('a'))
print(frase.lower().find('a')+1)
print(frase.lower().rfind('a')+1)

#METODO 2
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))
