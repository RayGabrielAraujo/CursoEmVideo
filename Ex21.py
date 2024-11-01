#Desafio 21, faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.mixer.init()

import pygame

pygame.init()
pygame.mixer.music.load("D:\Python\Curso em Vídeo\Ex21.mp3")
pygame.mixer.music.play()
pygame.event.wait()




