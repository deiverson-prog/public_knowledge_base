'''Faça um programa que tenha uma funçao chamada escreva(), que receba um
texto qualquer como parametro e mostre uma mensagem com tamanho adaptavél.

Ex.: 
escreva('Olá, Mundo!')

saida:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~ '''

def escreva(msg):
    tam=len(msg) +4 
    print('~'*tam)  #or print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*tam)


escreva('Hoje o céus está tão lindo!')
escreva('Que a sorte esteja convosco!')
escreva('Bora aprender PY!')