'''Crie um programa que leia vários números inteiros pelo teclado. No final 
da execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não 
continuar a digitar valores.'''

#Metodo 1
n = cont = média = soma = 0
n = int(input('Digite um número: '))
while n != 0:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
média = soma / cont    
print('Você digitou {} números e a média é de {:.2f}'.format(cont,média))


#Metodo 2

resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm	< menor:
            menor = núm    
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip() [0]
média = soma / quant
print('Você digitou {} números e a média foi de {:.2f}.'.format(quant, média))    
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
print('FIM')