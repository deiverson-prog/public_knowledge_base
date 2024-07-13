'''REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA. MOSTRANDO
OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.'''

#METODO 1

print('='*21)
print('{:^20}'.format(' GERADOR DE PA '))
print('='*21)
t1=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
termo = t1
cont = 1
while cont <=10:
    print('{}'.format(termo), end=' → ')
    termo += r
    cont += 1
print('FIM!')