''' MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUARIO SE ELE QUER 
MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE
QUER MOSTRAR 0 TERMOS.'''

#METODO 1

print('='*21)
print('{:^20}'.format(' GERADOR DE PA '))
print('='*21)
t1=int(input('Primeiro termo: '))
r=int(input('Razão da PA: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' → ')
        termo += r
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} temos mostrados.'.format(total))