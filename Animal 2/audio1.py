import pygame
pygame.mixer.init()
pygame.mixer.music.load("gun.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue