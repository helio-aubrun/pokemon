import pygame
from pygame import mixer
import os
import sys

mixer.init()
mixer.music.load("ost/title.mp3")
bg = pygame.image.load("image/title_screen.jpg")
bg = pygame.transform.scale(bg,(800,600))

class jeux():

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pkm")
        self.in_game = True

    def main(self):
        self.sound=0.3
        mixer.music.set_volume(self.sound)
        mixer.music.play(-1)
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.blit(bg,(0,0))
            pygame.display.flip()
pygame.init()
jeux().main()
pygame.quit()