import pygame
from pygame import mixer
import os
import sys
import class_dress_enemy

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
        self.input_text = ""
        self.equipe = []
        self.img_pokedex = pygame.image.load("image/pokedex.png")
        self.img_pokedex = pygame.transform.scale(self.img_pokedex,(100,100))

    def main(self):
        #reglage son
        self.sound=0.0
        mixer.music.set_volume(self.sound)
        mixer.music.play(-1)
        #1er ecran
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
        #2eme ecran
        while self.in_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #permet d'entrer un id et de l'ajouter à equipe
                    if event.key == pygame.K_RETURN:
                        if 1 <= int(self.input_text) <= 51 and len(self.equipe) <= 5:
                            self.equipe.append(self.input_text)
                            joueur.ajout_team_game(self.input_text)
                            self.input_text = ""
                    #effacer un caractere
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    #entrer un caractere
                    else:
                        self.input_text += event.unicode
            self.screen.blit(bg_choice,(0,0))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(300, 250, 200, 50), 2)
            font = pygame.font.Font(None, 36)
            text = font.render(self.input_text, 1, (10, 10, 10))
            id_texte = font.render("ID : ",1 ,(10,10,10))
            pokedex_text = font.render("pokedex ",1 ,(10,10,10))
            self.screen.blit(pokedex_text,(700,90))
            self.screen.blit(self.img_pokedex, (700, 5))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(325, 400, 150, 50), 5)
            play_text = font.render("PLAY",1 ,(10,10,10))
            self.screen.blit(play_text,(365, 415))
            self.screen.blit(id_texte, (310, 260))
            self.screen.blit(text, (360, 260))
            #affiche les poke dans l'equipe
            for i, number in enumerate(self.equipe):
                img = pygame.image.load(f"image/{number}/mini.png")
                img = pygame.transform.scale(img, (70, 70))
                self.screen.blit(img, (220 + i*60, 310))
            pygame.display.flip()

pygame.init()
joueur = class_dress_enemy.dress_enemy("Joueur")
adv = class_dress_enemy.dress_enemy("adversaire")
adv.random_team()
jeux().main()
pygame.quit()