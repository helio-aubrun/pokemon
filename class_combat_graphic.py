import pygame

class Screen:
    def __init__(self, id_joueur, id_adv, ):
        self.id_joueur = id_joueur
        self.id_adv = id_adv
        pygame.init()
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
        


    #affichage general
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.affich_joueur ()
            self.affiche_adv ()
            self.affich_overlay ()
            self.attaque ()
            pygame.display.flip()

        pygame.quit()


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

 
if __name__ == "__main__":
   screen = Screen(24, 25)
   screen.run()