#CORES DO TERMINAL

#PADRAO ANSI (PADRAO DE NORMALIZAÇÃO INTERNACIONAL) - 
#ESCAPE SEQUENCE - FUNCIONA EM VÁRIOS AMBIENTES
#UTILIZAR COM CONTRA BARRA "\"+"COD"
#EXISTE UMA FAIXA DE CÓDIGOS (PARA O PY UTILIZAR 033)
#SEM QUE FOR UTILIZAR O CÓD ANSI NO PY INICIAR COM:
#\033[(inserir o código)m   -> \033[m

#STYLE = 'ESTILO OU COMPORTAMENTO' EX.: NEGRITO, ITALICO, SUBLINHADO
#CÓD. PARA ESTILO: 0;1;4;7 
#0 = NONE (NENHUM)
#1 = BOLD (NEGRITO)
#4 = UNDERLINE (SUBLINHADO)
#7 = NEGATIVE (INVERTER)

#TEXT = 'COR TEXTO'
#CÓD. PARA TEXTO: 30;31;32;33;34;35;36;37
#30 = WHITE (BRANCO)
#31 = RED (VERMELHO)
#32 = GREEN (VERDE)
#33 = YELLOW (AMARELO)
#34 = BLUE (AZUL)
#35 = MAGENTA (MAGENTA - ROXO)
#36 = CYAN (CIANO)
#37 = GRAY (CINZA)

#PARA USAR OUTRAS CORES INCLUIR BIBLIOTECA

#BACK = 'COR DO FUNDO'
#CÓD. PARA FUNDO: 40,41,42,43,44,45,46,47
#40 = WHITE (BRANCO)
#41 = RED (VERMELHO)
#42 = GREEN (VERDE)
#43 = YELLOW (AMARELO)
#44 = BLUE (AZUL)
#45 = MAGENTA (MAGENTA - ROXO)
#46 = CYAN (CIANO)
#47 = GRAY (CINZA)

#EXEMPLO DE CÓD. MONTADO -> \033[0;33;44m

#TESTE = FUNDO VEMELHO, LETRA BRANCA, NEGRITO   -> \033[0;30;41m
#TESTE = FUNDO AZUL, LETRA AMARELA, SUBLINHADO  -> \033[4;33,44m
#TESTE = FUNDO AMARELO, LETRA ROXA, NEGRITO     -> \033[1;35;43m
#TESTE = FUNDO VERDE, LETRA BRANCA, NEGRITO     -> \033[30;42m
#TESTE = FUNDO PRETO, LETRA BRANCA, NEGRITO     -> \033[m (PADRAO DO TERMINAL) 
#TESTE = FUNDO BRANCO, LETRA PRETA, NEGRITO     -> \033[7;30m

#PRATICANDO

#print('\033[31mHELLO, WORLD') #letra vermelha

#print('\033[31;43mHELLO, WORLD') #letra vermelha, fundo amarelo

#print('\033[31;43;1mHELLO, WORLD') #letra vermelha, fundo amarelo, negrito

#print('\033[31;43;1mHELLO, WORLD\033[m') #letra vermelha, fundo amarelo até o fim da frase, negrito

#print('\033[45;4mHELLO, WORLD\033[m') #letra branca, fundo lilás até o fim da frase, sublinhado

#print('\033[4mHELLO, WORLD\033[m') #letra branca, fundo preto até o fim da frase, sublinhado

#print('\033[7;40mHELLO, WORLD\033[m') #letra preta, fundo branco.

#print('\033[33;44mHELLO, WORLD\033[m') #letra amarela, fundo azul.

#print('\033[7;33;44mHELLO, WORLD\033[m') #letra azul, fundo amarelo (usando inversão)

#EXEMPLO COM VARIÁVEIS

a=3
b=5
print('Os valores são \033[35m{}\033[m e \033[31m{}\033[m!!!'.format(a,b)) #valor "a" em magenta e valor "b" em vermelho.

#EXEMPLO DE CORES NO FORMAT

Nome = input('Qual o seu nome?')
print('Olá! {}{}{}, Prazer em te conhecer!!!'.format('\033[1;34m',Nome,'\033[m')) #Variavel nome letra azul em negrito


Nome = input('Qual o seu nome?')
cores = {'limpa':'\033[m',
         'azul':'\033[35m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[1;7;40m'}
print('Olá! {}{}{}, Prazer em te conhecer!!!'.format(cores['pretoebranco'],Nome, cores['limpa'])) #Variavel nome letra azul em negrito



