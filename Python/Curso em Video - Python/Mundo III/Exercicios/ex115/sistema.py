from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'programaDeive.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        #Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:    
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)