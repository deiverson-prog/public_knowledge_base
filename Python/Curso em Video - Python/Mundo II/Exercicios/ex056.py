#EX.056
#DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE QUATRO PESSOAS. NO FINAL DO PROGRAMA, MOSTRE:
#A MÉDIA DE IDADE DO GRUPO.
#QUAL É O NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TEM MENOS DE 20 ANOS

#Metodo 1
somaidade = 0
médiaidade = 0
maioridadeH = 0
nomevelho = 0
totmulher20 = 0
for p in range (1,5):
    print('------ {}ª Pessoa ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade/4
print('A média de idade do Grupo é de {}'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeH, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))