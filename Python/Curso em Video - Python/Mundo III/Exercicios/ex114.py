'''Crie um código em Python que teste se o site Pudim está acessível pelo 
computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request('https://www.pudim.com.br/')
except:
    print('Deu certo')
    print('O site Pudim não está acessível no momento.')
else:
    print('Tudo Ok')
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())