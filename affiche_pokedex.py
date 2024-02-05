import pygame

class affiche_pokedex :
    def __init__ (self) :
        pygame.init ()

        #fond d'ecran
        self.screen = pygame.display.set_mode((800, 600))
        #font
        self.font = pygame.font.Font(None, 30)

        self.left = pygame.transform.scale(pygame.image.load("image/left.png"), (50,50))
        self.right = pygame.transform.scale(pygame.image.load("image/right.png"), (50,50))

        #fond d'ecran
        self.fond = pygame.transform.scale( pygame.image.load ("image/pokedex_1.png"), (800, 600))

        #affichage des plateforme
        self.screen.blit (self.fond, (0, 0))


    def handle_click(self, event):
        if event.button == 1: # Left mouse button
            x, y = pygame.mouse.get_pos()
            print(f"Mouse clicked at ({x}, {y})")


    #affichage des state
    def affich_state (self, id) :
        import json
        list = ["pv", "atk", "def", "atk_spe", "def_spe", "spe", "talent", "nom", "id", "Type"]
        list_pos = [(255, 90), (255, 170), (255, 220), (255, 270), (255, 320), (255, 380), (220, 460), (570, 110), (570, 170), (520, 530)]
        with open ("pokedex.json", "r", encoding='utf-8') as li_pokedex :
            pokedex = json.load (li_pokedex)
            info = pokedex [str (id)]
        for i in range (10) :
            affiche_info = self.font.render (str( info [list [i]]), True, (0, 0, 0))

            self.screen.blit (affiche_info, list_pos [i])
        sprite = pygame.transform.scale ( pygame.image.load ("image/" + str (id) + "/front.png"), (300, 300))

        self.screen.blit (sprite, (470, 200))

    #affichage d'attaque
    def affiche_attaque (self, id) :
        import json
        attaques_pos = [(10, 510), (250, 510), (10,560), (250, 560)]
        with open ("pokedex.json", "r", encoding='utf-8') as li_pokedex, open ("attaque_list.json", "r", encoding='utf-8') as attaque:
            pokedex = json.load (li_pokedex)
            attaque = json.load (attaque)
            list_attaques_pokedex = []
            for i in range (len (pokedex [str (id)]["attaques"])) :
                list_attaques_pokedex.append (attaque [(pokedex [str (id)]["attaques"][i])]["nom"])

            for i in range (len (list_attaques_pokedex)) :
                aff_attaque = self.font.render (list_attaques_pokedex [i], True, (0, 0, 0))
                self.screen.blit (aff_attaque, attaques_pos [i])



    #creation des buton
    def crea_button (self) :
        self.screen.blit (self.left, (500,30))
        self.screen.blit (self.right, (600,30))
        font = pygame.font.Font(None, 36)
        back_texte = font.render("Echap ",1 ,(10,10,10))
        self.screen.blit(back_texte,(690,40))




    #affichage general
    def run(self):
        id = 1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    x,y = event.pos
                    # Check if the mouse click was within the rectangle
                    if 38 <= y <= 70:
                        if 501 <= x <= 547:
                            id -= 1
                            if id < 1 :
                                    id = 1
                        elif 603 <= x <= 647:
                            id += 1
                            if id > 51:
                                id = 51
                        elif 690 <= x <= 768:
                            running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        id -= 1
                        if id < 1 :
                            id = 1
                    elif event.key == pygame.K_RIGHT:
                        id += 1
                        if id > 51:
                            id = 51
                    elif event.key == pygame.K_ESCAPE:
                        running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit (self.fond, (0, 0))
            self.crea_button ()
            self.affich_state (id)
            self.affiche_attaque (id)
            pygame.display.flip()


if __name__ == "__main__":
   screen = affiche_pokedex()
   screen.run()