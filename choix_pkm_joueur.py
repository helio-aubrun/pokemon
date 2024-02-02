import pygame
from PIL import Image
import json
from math import floor

class changement () :
    def __init__(self) -> None:
        pass

    def load_gif(self, filename):
        """Load a GIF and split it into individual frames"""
        im = Image.open(filename)
        frames = []
        try:
            while True:
                frames.append(pygame.image.fromstring(im.convert('RGBA').tobytes(), im.size, 'RGBA'))
                im.seek(len(frames))
        except EOFError:
            pass # End of sequence
        return frames

    #creation de bar de vie
    def draw_health_bar(self, x, y, width, height, pv, pv_max):

        #creation du contour
        pygame.draw.rect(self.screen, (0, 0, 0), (x - 1, y - 1, width + 2 , height + 2))

        # Draw the background of the health bar
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, width, height))

        #recuperation du pourcentage de pv
        pourcentage = floor (float (pv) / (float (pv_max) / 100))

        # Calculate the width of the health bar fill
        fill_width = int(pourcentage / 100 * width)

        # Draw the fill of the health bar
        pygame.draw.rect(self.screen, (0, 255, 0), (x, y, fill_width, height))

    #affiche nom
    def affiche_nom (self, pkm, pos) :
        font = pygame.font.Font(None, 34)
        text = font.render(pkm ["nom"], True, (30, 30, 30))
        self.screen.blit(text, (pos [0] + 108 , pos [1] + 30))

    #affiche lvl
    def affiche_lvl (self, pkm, pos) :
        font = pygame.font.Font(None, 36)
        text = font.render(str (pkm ["lvl"]), True, (30, 30, 30))
        self.screen.blit(text, (pos [0] + 47 , pos [1] + 82))    

    #affiche info pkm
    def info_pkm ( self, pkm, pos) :
        #affiche icon
        img_pkm = pygame.transform.scale (pygame.image.load ("image/" + str (pkm ["id"]) + "/mini.png"), (75, 75))
        self.screen.blit (img_pkm, (pos[0] + 15, pos [1] + 0))
        #affiche nom
        self.affiche_nom (pkm, pos)

        #affiche pv
        self.draw_health_bar (pos [0] + 144, pos [1] + 80, 144, 9, pkm ["pv"], pkm ["pv_max"])

        #affiche lvl
        self.affiche_lvl (pkm, pos)
            

    #affichage des pokemon
    def affiche_pkm (self) :
        pos = [(20, 48), (405, 48), (20, 229), (405, 229), (20, 410), (405, 410)]
        
        with open('list_pkm_joueur.json', 'r', encoding='utf-8') as f:
                list_pkm_joueur = json.load(f)

        self.bt = []
        for i in range (len (list_pkm_joueur)) :
            image = pygame.transform.scale( pygame.image.load ("image/overlay_pkm_selection.png"), (375, 141))
            self.screen.blit (image , pos [i])

            self.info_pkm (list_pkm_joueur [str (i + 1)] ,pos [i])


            self.bt.append (pygame.Rect(pos [i] [0], pos [i] [1], 375, 141))

    '''    #affcihe message 
    def affiche_message (test = 0) :
        '''


    #retiur du chois 
    def retourne (self) :
        self.i = -1
        while self.i == -1 :
            self.main ()
        return self.i
        

    def main(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        frames = self.load_gif('image\Sky driving.gif')
        frame_index = 0

        clock = pygame.time.Clock()
        test = True
        while test:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    test = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    mouse_pos = event.pos
                    # Check if the mouse click was within the rectangle
                    for i in range (len (self.bt)) :
                        if self.bt [i].collidepoint(mouse_pos):
                            with open('list_pkm_joueur.json', 'r', encoding='utf-8') as f:
                                list_pkm_joueur = json.load(f)
                            if list_pkm_joueur [str (i + 1)] ["pv"] <= 0 :
                                #self.affiche_message (1)
                                print("Rectangle clicked! " + str (i))
                            else :
                                self.i = i

                                test = False
                            

            self.screen.fill ((0, 0, 0))
            self.screen.blit (pygame.transform.scale(frames[frame_index],  (800, 600)), (0, 0))

            self.affiche_pkm ()



            pygame.display.flip()


            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0
            
            #fps cap
            clock.tick(30)
    
    pygame.quit()



if __name__ == '__main__':
    ecran = changement ()
    ecran.main()