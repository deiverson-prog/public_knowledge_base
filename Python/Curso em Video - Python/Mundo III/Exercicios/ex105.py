'''Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).

Adicione também as docstrings da função.'''

def notas(*n,situação=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situação: Valor opcional, indicando se deve o não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    r=dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if situação:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 2.5, 9, 8.5) #Sem parâmetro opcional
resp = notas(5.5, 2.5, 9, 8.5, situação=True) #Com parâmetro opcional
print(resp)
help(notas)