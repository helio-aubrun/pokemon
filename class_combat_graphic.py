import pygame
import class_pkm
import json
import class_dress_enemy
import class_pkm
import class_attaque
import class_combat
import random
import json
import class_dress_enemy
import ia
from math import floor

class Screen:
    def __init__(self):
        pygame.init()
        
        #font , nom et taille de la fenetre 
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("pokemon")
        self.font = pygame.font.Font(None, 30)

        #fond d'ecran
        self.back = pygame.transform.scale( pygame.image.load ("sprites/field_bg.png"), (800, 600))

    #creation de lequipe du joueur
    def crea_list_joueur (self) :
        with open('list_pkm_joueur.json', 'r', encoding='utf-8') as f:
            list_pkm_joueur = json.load(f)
        self.joueur = class_dress_enemy.dress_enemy ("joueur")
        for pkm in list_pkm_joueur :
            self.joueur.ajout_team_game(str (list_pkm_joueur [pkm]["id"]))
        self.pkm_joueur = self.joueur.equipe [0]

    #ecran du chois du pokemon suivant
        

    #creation et affichage des plateforme
    def plateforme (self) :
        #plateforme pokemon joueur
        self.plat_joueur = pygame.image.load ("sprites/field_base0.png")

        #plateforme pokemon adverse
        self.plate_adv = pygame.image.load ("sprites/field_base1.png")


        #affichage des plateforme
        self.screen.blit (self.back, (0, 0))
        self.screen.blit (self.plat_joueur, (0, 400))
        self.screen.blit (self.plate_adv, (500, 240))


    #creation random des pokemon enemy
    def crea_list_adv (self) :
        self.adv = class_dress_enemy.dress_enemy ("adversaire")
        self.adv.random_team ()
        self.pkm_adv = self.adv.equipe [0]

    #changement de pokemon ko de l'adversaire
    def switch_adv (self) :
        temp = []
        for i in range (1, len (self.adv.equipe)) :
            temp.append (self.adv.equipe [i])
        print (temp)
        self.adv.equipe = temp
        self.pkm_adv = self.adv.equipe [0]
            

    #affichage du pokemon du joueur
    def affich_joueur (self) :
        #chargement du sprite
        self.affiche_pkm_joueur = pygame.transform.scale (pygame.image.load ("sprites/image/" + str (self.pkm_joueur.id) + "/back.png"), (400, 400))

        #affichage du sprites
        self.screen.blit (self.affiche_pkm_joueur, (50, 200))

    #affichage du pokemon adverse
    def affiche_adv (self) :
        #chargement du sprite
        self.affich_pkm_adv = pygame.transform.scale (pygame.image.load ("sprites/image/" + str (self.pkm_adv.id) + "/front.png"), (400, 400))

        #affichage du sprites
        self.screen.blit (self.affich_pkm_adv, (440, 8))

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
            for i in pokedex[str (self.pkm_joueur.id)]["attaques"] :
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
            nb_button = len (pokedex [str (self.pkm_joueur.id)]["attaques"])
        
        pos = [(300,490), (550, 490), (300, 540), (550, 540)]
        self.bt = []

        for i in range (nb_button) :
            self.bt.append (pygame.Rect(pos [i][0], pos [i][1], 190, 44))

    #creation de bar de vie
    def draw_health_bar(self, x, y, width, height, color, pv, pv_max):
        #creation du contour
        pygame.draw.rect(self.screen, (0, 0, 0), (x - 1, y - 1, width + 2 , height + 2))

        # Draw the background of the health bar
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, width, height))

        #recuperation du pourcentage de pv
        pourcentage = floor (float (pv) / (float (pv_max) / 100))

        # Calculate the width of the health bar fill
        fill_width = int(pourcentage / 100 * width)

        # Draw the fill of the health bar
        pygame.draw.rect(self.screen, color, (x, y, fill_width, height))

    #creation pkm joueur
    def pkm_joueur_crea (self, id, lvl):
        with open("pokedex.json", "r", encoding='utf-8') as f:
            pokedex = json.load(f)
        pokemon_29 = pokedex.get(str (id))
        self.pkm_joueur = class_pkm.pkm_dress(pokemon_29, lvl)

    #creation pkm edversse
    def pkm_adv_crea (self, id, lvl):
        with open("pokedex.json", "r", encoding='utf-8') as f:
            pokedex = json.load(f)
        pokemon_2 = pokedex.get(str (id))
        self.pkm_adv = class_pkm.pkm(pokemon_2, lvl)

    #creation overlay bar de vie joueur et nom/lvl
    def affich_overlay_vie_joueur (self) :
        #ovely
        overlay = pygame.transform.scale (pygame.image.load ("sprites/pkm_joueur_bare_vie.png"), (312, 111))
        self.screen.blit (overlay, (620 - 144, 400 - 51))
        font = pygame.font.Font(None, 34)

        #nom
        text = font.render(self.pkm_joueur.nom, True, (51, 51, 51))
        self.screen.blit(text, (520, 365))
        #lvl
        text = font.render(str (self.pkm_joueur.lv), True, (51, 51, 51))
        self.screen.blit(text, (680, 365))

    #creation overlay bar de vie adversaire et nom/lvl
    def affich_overlay_vie_adversaire (self) :
        overlay = pygame.transform.scale (pygame.image.load ("sprites/overlay_bar_vie_adversaire.png"), (300, 87))
        self.screen.blit (overlay, (0, 50))
        font = pygame.font.Font(None, 34)

        #nom
        text = font.render(self.pkm_adv.nom, True, (51, 51, 51))
        self.screen.blit(text, (14, 64))
        #lvl
        text = font.render(str (self.pkm_adv.lv), True, (51, 51, 51))
        self.screen.blit(text, (175, 64))

    #fin du combat
    def fin_combat (self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.blit (self.back, (0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Fin du jeu", True, (255, 0, 0))
            text_rect = text.get_rect(center=(400, 300))
            self.screen.blit(text, text_rect)
            pygame.display.update()


    #affichage general
    def run(self):
        running = True
        #creation class combat
        combat_pkm = class_combat.combat ()

        #creation adversaire
        self.crea_list_adv ()

        #crreation joueur
        self.crea_list_joueur ()
        

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
                            combat_pkm.choose_attack (self.pkm_joueur, self.pkm_adv, int (i))
                            if self.pkm_adv.pv <= 0:
                                    if len (self.adv.equipe) == 1 :
                                        self.fin_combat ()
                                        running = False
                                        break
                                    
                                    #changement de pokemon ko
                                    self.switch_adv ()
                            if self.pkm_joueur.pv <= 0:
                                self.chois_pkm_joueur ()

        
                            
                    
            #fond ecran
            self.screen.blit (self.back, (0, 0))

            #plateforme
            self.plateforme ()

            #affichage plateforme
            self.screen.blit (self.plat_joueur, (0, 400))
            self.screen.blit (self.plate_adv, (500, 240))

            #affichage pokemon
            self.affich_joueur ()
            self.affiche_adv ()

            #affichage overlay
            self.affich_overlay ()
            self.attaque ()
            self.crea_button ()

            self.affich_overlay_vie_joueur ()
            self.draw_health_bar(620, 400, 144, 9, (0, 255, 0), self.pkm_joueur.pv, self.pkm_joueur.hp_max)
            self.affich_overlay_vie_adversaire ()
            self.draw_health_bar(117, 101, 144, 9, (0, 255, 0), self.pkm_adv.pv, self.pkm_adv.hp_max)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
   screen = Screen()
   screen.run()