import pygame
from pygame import mixer
import os
import sys

mixer.init()
mixer.music.load("ost/title.mp3")
bg = pygame.image.load("image/title_screen.jpg")
bg = pygame.transform.scale(bg,(800,600))
bg_choice = pygame.image.load("image/selection_bg.png")
bg_choice = pygame.transform.scale(bg_choice,(800,600))
button_sound = mixer.Sound("ost/button_click.mp3")

class jeux():

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pkm")
        self.in_game = True
        self.in_choice = True

    def main(self):
        self.sound=0.3
        mixer.music.set_volume(self.sound)
        mixer.music.play(-1)
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        button_sound.play()
                        self.in_game = False
            self.screen.blit(bg,(0,0))
            pygame.display.flip()
        while self.in_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        button_sound.play()
                        self.in_choice = False
                elif event.key == pygame.K_BACKSPACE:
                   self.input_text = self.input_text[:-1]
                else:
                   self.input_text += event.unicode
            self.screen.blit(bg_choice,(0,0))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(300, 250, 200, 50), 2)
            font = pygame.font.Font(None, 36)
            text = font.render(self.input_text, 1, (10, 10, 10))
            self.screen.blit(text, (310, 260))
            pygame.display.flip()

pygame.init()
jeux().main()
pygame.quit()