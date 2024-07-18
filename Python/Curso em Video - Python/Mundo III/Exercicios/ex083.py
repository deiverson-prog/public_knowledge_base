'''Crie um programa onde o usuário digite uma expressão qualquer que use 
parenteses. Seu aplicativo deverá analisar se a expressão passada está com
os parenteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite uma expressão: '))
pilha = list()
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida! ')
else:    
    print('Sua expressão esta inválida! ')