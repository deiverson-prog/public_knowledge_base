'''Crie um programa onde o usuário possa digitar cinco valores númericos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela.'''

valores = list()
for v in range(0,5):
    v =int(input('Digite um valor: '))
    if v == 0 or v > valores[-1]:
        valores.append (v)
        print(f'Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if v <= valores[posicao]:
                valores.insert(posicao,v)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}.')
