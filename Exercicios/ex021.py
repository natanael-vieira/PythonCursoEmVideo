from turtle import delay
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
# permite que eu consiga executar a música, quanto maior o número, maior o tempo de reprodução.
pygame.time.delay(200000000)
