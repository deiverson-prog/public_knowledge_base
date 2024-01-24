#Ex007
#Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre a sua média.

nota1 = float ( input ('Insira uma nota:'))
nota2 = float ( input ('Insira outra nota:'))
média = (nota1 + nota2)/2
print ('Primeira nota: {} \nSegunda nota: {} \nMédia: {}'.format(nota1, nota2, média))