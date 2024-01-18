import pygame

class affiche_pokedex :
    def __init__ (self) :
        pygame.init ()

        #fond d'ecran
        self.screen = pygame.display.set_mode((800, 600))
        #font
        self.font = pygame.font.Font(None, 30)



        #fond d'ecran
        self.fond = pygame.transform.scale( pygame.image.load ("sprites/pokedex_1.png"), (800, 600))

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
        sprite = pygame.transform.scale ( pygame.image.load ("sprites/image/" + str (id) + "/front.png"), (300, 300))

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
        import json
        button_size = (190,44)
        pos = [(570, 50), (590, 50)]
        self.bt = []

        for i in range (2) :
            self.bt.append (pygame.Rect(pos [i][0], pos [i][1], 20, 20))

            aff_bt1 = self.font.render ("<", True, (0, 0, 0))
            aff_bt2 = self.font.render (">", True, (0, 0, 0))

            self.screen.blit (aff_bt1, pos [0])
            self.screen.blit (aff_bt2, pos [1])




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
                    mouse_pos = event.pos
                    # Check if the mouse click was within the rectangle
                    for i in range (len (self.bt)) :
                        if self.bt [i].collidepoint(mouse_pos):

                            if i == 0:
                                id -= 1
                                print (id)
                                if id < 1 :
                                    id = 1
                                    
                            else:
                                id += 1
                                print (id)
                                if id > 51 :
                                    id = 51
            self.screen.fill((0, 0, 0))
            self.screen.blit (self.fond, (0, 0))
            self.crea_button ()
            self.affich_state (id)
            self.affiche_attaque (id)

            pygame.display.flip()


if __name__ == "__main__":
   screen = affiche_pokedex()
   screen.run()