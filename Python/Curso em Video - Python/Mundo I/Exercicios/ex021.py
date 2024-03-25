#Ex021
#Faça um programa em Python que abra e reproduza o audio de um arquivo MP3.

#METODO 1
from pygame import mixer, event
mixer.init()
mixer.music.load('ThisYear.mp3')
mixer.music.play()
input('Aperte Enter para encerrar!')

#METODO 2
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

mixer.init()
mixer.music.load('ThisYear.mp3')
mixer.music.play()

input('aperte Enter para encerrar!')
