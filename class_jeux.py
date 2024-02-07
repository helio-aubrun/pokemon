import pygame
from pygame import mixer
import sys
import class_dress_enemy
import affiche_pokedex
import json
import class_combat_graphic
import class_pkm

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
        self.pokedex = affiche_pokedex.affiche_pokedex()
        self.combat = class_combat_graphic.Screen()

    def main(self):
        #reglage son
        self.sound=0.2
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
                        mixer.music.load("ost/prof.mp3")
                        mixer.music.play(-1)
                        self.in_game = False
            self.screen.blit(bg,(0,0))
            pygame.display.flip()
        #2eme ecran
        with open('list_pkm_joueur.json', 'w') as f:
            f.truncate()
            f.write('{}')
        while self.in_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #permet d'entrer un id et de l'ajouter à equipe
                    if event.key == pygame.K_RETURN:
                        if 1 <= int(self.input_text) <= 51 and len(self.equipe) <= 5:
                            with open('list_pkm_joueur.json', 'r') as f:
                                pkm_joueur_data = json.load(f)

                    # Get data from pokedex.json
                            with open('pokedex.json', 'r', encoding='utf-8') as f:
                                pokedex_data = json.load(f)
                                pokemon_data = pokedex_data.get(self.input_text)

                    # Add new entry to pkm_joueur_data
                            new_key = len(pkm_joueur_data) + 1 # Auto-increment key

                            pokemon_instance = class_pkm.pkm(pokemon_data,  50)

                            # Add new entry to pkm_joueur_data with pv_max
                            new_entry = {
                                'id' : pokemon_instance.id,
                                'nom' : pokemon_instance.nom,
                                'Type' : pokemon_instance.type,
                                'nom' : pokemon_instance.nom,
                                'talent' : pokemon_instance.talent,
                                'pv' : pokemon_instance.pv,
                                'atk' : pokemon_instance.atk,
                                'def' : pokemon_instance.defense,
                                'atk_spe' : pokemon_instance.atk_spe,
                                'def_spe' : pokemon_instance.def_spe,
                                'spe' : pokemon_instance.spe,
                                'exp' : pokemon_instance.exp,
                                'evo' : pokemon_instance.evo,
                                'attaques' : pokemon_instance.attaques,
                                'pv_max': pokemon_instance.pv_max,  # Add pv_max key with its value
                                'lvl': pokemon_instance.lv
                            }
                            pkm_joueur_data[str(new_key)] = new_entry
                    # Write updated data back to list_pkm_joueur.json
                            with open('list_pkm_joueur.json', 'w') as f:
                                json.dump(pkm_joueur_data, f)

                            self.equipe.append(self.input_text)
                            joueur.ajout_team_game(self.input_text)
                            self.input_text = ""
                    #effacer un caractere
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    #entrer un caractere
                    else:
                        self.input_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #bouton pokedex et play
                    x,y = event.pos
                    if 703 <= x <= 796 and 18 <= y <= 94:
                        self.pokedex.run()
                    elif 326 <= x <= 471 and 402 <= y <= 448:
                        print ("Play")
                        mixer.music.load("ost/dress.mp3")
                        mixer.music.play(-1)
                        self.combat.run()
                        
            #affichage de tout les elements
            self.screen.blit(bg_choice,(0,0))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(300, 250, 200, 50), 2)
            font = pygame.font.Font(None, 36)
            text = font.render(self.input_text, 1, (10, 10, 10))
            id_texte = font.render("N° : ",1 ,(10,10,10))
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
adv.random_team(4)
jeux().main()
pygame.quit()