#Ex007
#Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre a sua média.

nota1 = float ( input ('Insira uma nota:'))
nota2 = float ( input ('Insira outra nota:'))
média = (nota1 + nota2)/2
print ('Primeira nota: {:.2f} \n Segunda nota: {:.2f} \n Média: {:.2f}'.format(nota1, nota2, média))

#Outra Forma:
n1 = float ( input ('Insira uma nota:'))
n2 = float ( input ('Insira outra nota:'))
m = (n1 + n2)/2
print ('A média entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, m))