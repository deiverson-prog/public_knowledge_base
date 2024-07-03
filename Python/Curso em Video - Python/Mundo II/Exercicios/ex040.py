#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA. 
#MOSTRANDO UMA MENSAGEM NO FINAL. DE ACORDO COM A MÉDIA ATINGIDA:

#MÉDIA ABAIXO DE 5.0:
#REPROVADO

#MÉDIA ENTRE 5.0 E 6.9:
#RECUPERAÇÃO

#MÉDIAS 7.0 OU SUPERIOR:
#APROVADO

#METODO 1

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media < 5:
    print('O aluno com média {:.1f}, foi Reprovado'.format(media))
elif media >=5 and media <=6.9:
    print('O aluno com média {:.1f}, foi para Recuperação'.format(media))
elif media >=7:
    print('O aluno com média {:.1f}, foi Aprovado'.format(media))

#METODO 2

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media < 5:
    print('O aluno está REPROVADO')
elif 7 > media >=5:
    print('O aluno está em RECUPERAÇÃO')
#elif media >=5 and media < 7:
#    print('O aluno está em RECUPERAÇÃO'.format(media))
elif media >=7:
    print('O aluno está APROVADO')