import pygame
import class_pkm
import json
import class_dress_enemy
import class_pkm
import class_attaque
import random
import json
import class_dress_enemy
import ia
from math import floor

class Screen:
    def __init__(self, id_joueur, id_adv, ):
        pygame.init()

        self.id_joueur = id_joueur
        self.id_adv = id_adv
        with open("pokedex.json", "r") as f:
            pokedex = json.load(f)

        #creation
        self.pokemon_joueur = pokedex.get(str ( id_joueur))
        self.pokemon_adversaire = pokedex.get(str (id_adv))

        #creation des pokemon de chaqun
        self.pkm_joueur = class_pkm.pkm_dress(self.pokemon_joueur, 39)
        self.pkm_adv = class_pkm.pkm_dress(self.pokemon_adversaire, 39)


        '''self.joueur = class_dress_enemy.dress_enemy("joueur")
        self.joueur.ajout_team_game (id_joueur)

        self.adv = class_dress_enemy.dress_enemy("adversaire")
        self.adv.ajout_team_game (id_adv)'''
        
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 30)

        #fond d'ecran
        self.back = pygame.transform.scale( pygame.image.load ("sprites/field_bg.png"), (800, 600))


        #plateforme pokemon joueur
        self.plat_joueur = pygame.image.load ("sprites/field_base0.png")

        #plateforme pokemon adverse
        self.plate_adv = pygame.image.load ("sprites/field_base1.png")


        #affichage des plateforme
        self.screen.blit (self.back, (0, 0))
        self.screen.blit (self.plat_joueur, (0, 400))
        self.screen.blit (self.plate_adv, (500, 240))


    #affichage du pokemon du joueur
    def affich_joueur (self) :
        #chargement du sprite
        self.pkm_j = pygame.transform.scale (pygame.image.load ("sprites/image/" + str (self.id_joueur) + "/back.png"), (400, 400))

        #affichage du sprites
        self.screen.blit (self.pkm_j, (50, 200))

    #affichage du pokemon adverse
    def affiche_adv (self) :
        #chargement du sprite
        self.pkm_adv = pygame.transform.scale (pygame.image.load ("sprites/image/" + str (self.id_adv) + "/front.png"), (400, 400))

        #affichage du sprites
        self.screen.blit (self.pkm_adv, (440, 8))

    #affichae overlay
    def affich_overlay (self) :
        #overlay
        self.overlay = pygame.transform.scale (pygame.image.load ("sprites/overlay_message.png"), (800,150))
        self.box = pygame.transform.scale (pygame.image.load ("sprites/overlay_fight1.png"), ((800 / 100) * 60, 100))

        self.screen.blit (self.overlay, (0, 450))
        self.screen.blit (self.box, (290, 478))

    #affichage des attaque
    def attaque (self) :
        import json
        #creation de la list d'attaque
        with open ("pokedex.json", "r", encoding='utf-8') as pokedex_l, open ("attaque_list.json", "r", encoding='utf-8') as attaque_l:
            pokedex = json.load (pokedex_l)
            l_attaques = json.load (attaque_l)
            self.list_attaques = []
            for i in pokedex[str (self.id_joueur)]["attaques"] :
                self.list_attaques.append (l_attaques[i]["nom"])

        pos = [(300,490), (550, 490), (300, 540), (550, 540)]
        for i in range (len (self.list_attaques)) :
            self.attaques = self.font.render (self.list_attaques [i], True, (255, 255, 255))

            self.screen.blit(self.attaques, pos [i])


    #creation des buton
    def crea_button (self) :
        import json

        
        button_size = (190,44)

        with open ("pokedex.json", "r", encoding='utf-8') as pokedex_l:
            pokedex = json.load (pokedex_l)
            nb_button = len (pokedex [str (self.id_joueur)]["attaques"])
        
        pos = [(300,490), (550, 490), (300, 540), (550, 540)]
        self.bt = []

        for i in range (nb_button) :
            self.bt.append (pygame.Rect(pos [i][0], pos [i][1], 190, 44))

    #creation de bar de vie
    def draw_health_bar(self, x, y, width, height, color, vie, lvl, id):
        #creation du contour
        pygame.draw.rect(self.screen, (0, 0, 0), (x - 1, y - 1, width + 2 , height + 2))

        # Draw the background of the health bar
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, width, height))

        #recuperation du pourcentage de pv
        with open("pokedex.json", "r") as f:
            pokedex = json.load(f)
        test = pokedex.get [str (id)]
        pokemon = class_pkm.pkm_dress(test, lvl)
        pourcentage = floor (float (vie) / (float (pokemon.vie) / 100))

        # Calculate the width of the health bar fill
        fill_width = int(pourcentage / 100 * width)

        # Draw the fill of the health bar
        pygame.draw.rect(self.screen, color, (x, y, fill_width, height))

    #creation pkm joueur
    def pkm_joueur_crea (self, id, lvl):
        with open("pokedex.json", "r", encoding='utf-8') as f:
            pokedex = json.load(f)
        pokemon_29 = pokedex.get("id")
        self.pkm_joueur = class_pkm.pkm_dress(pokemon_29, lvl)

    #creation pkm edversse
    def pkm_adv_crea (self, id, lvl):
        with open("pokedex.json", "r", encoding='utf-8') as f:
            pokedex = json.load(f)
        pokemon_2 = pokedex.get("id")
        self.pkm_adv = class_pkm.pkm(pokemon_2, lvl)

    

    #affichage general
    def run(self):
        running = True
        '''pkm_joueur = pokedex.get ["5"]
        pkm_adv = pokedex.get ["4"]'''
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    mouse_pos = event.pos
                    # Check if the mouse click was within the rectangle
                    for i in range (len (self.bt)) :
                        if self.bt [i].collidepoint(mouse_pos):
                            print("Rectangle clicked! " + str (i))
                    


            self.affich_joueur ()
            self.affiche_adv ()
            self.affich_overlay ()
            self.attaque ()
            self.crea_button ()
            vie_joueur  = 50#vie en pourcentage
            self.draw_health_bar(10, 430, 200, 20, (0, 255, 0), self.pkm_joueur.pv, self.pkm_joueur.lv, self.id_joueur)
            vie_ene = 50#vie en pourcentage
            self.draw_health_bar(530, 350, 200, 20, (0, 255, 0), self.pkm_adv.pv, self.pkm_adv.lv, self.id_adv)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
   screen = Screen(51, 1)
   screen.run()
