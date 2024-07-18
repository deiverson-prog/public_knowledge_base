''' Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela. 
c) Uma lista com os times em ordem alfabética.
d) Em que posição da tabela está o time da Bahia.'''

Brasileirão = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia','Cruzeiro',
'São Paulo', 'Fortaleza','Athletico-PR','Bragantino','Atlético-MG','Vasco da Gama',
'Juventude','Internacional','Criciúma', 'Cuiabá', 'EC Vitória', 'Corinthians', 
'Grêmio', 'Atlético-GO', 'Fluminense')

print(f'Os 5 primeiros colocados são: {Brasileirão[0:5]}')
print(f'Os 4 últimos colocados são: {Brasileirão[-4:]}')
print(sorted(Brasileirão))

time = str(input('qual time deseja saber a posição? ')).strip().capitalize()
print(f'O time {time} está na {Brasileirão.index(time)+1}ª posição.')

#or
print(f'O time Bahia está na {Brasileirão.index("Bahia")+1}ª posição.')


