#ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO
#ESCOLHER EM QUAL SERÁ A BASE DE CONVERSÃO:

#1 PARA BINÁRIO
#2 PARA OCTAL
#3 PARA HEXADECIMAL

#METODO 1

num = int(input('Escreva um número: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))

#condicao aninhada

if opcao == 1:
    print('{} Convertido para Binário é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção INVALIDA tente novamente.')