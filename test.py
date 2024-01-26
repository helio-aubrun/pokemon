import pygame
from PIL import Image
import json

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

    def affiche_pkm (self) :
        pos = [(20, 48), (405, 48), (20, 229), (405, 229), (20, 410), (405, 410)]
        for i in range (6) :
            with open('list_pkm_joueur.json', 'r', encoding='utf-8') as f:
                list_pkm_joueur = json.load(f)
            image_joueur = pygame.transform.scale (pygame.image.load ("sprites/image/" + str (51) + "/mini.png"), (75, 75))
            image = pygame.transform.scale( pygame.image.load ("sprites/overlay_pkm_selection.png"), (375, 141))
            self.screen.blit (image , pos [i])

            self.screen.blit (image_joueur, (pos [i] [0] + 15, pos [i] [1] + 0))

    def main(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

        frames = self.load_gif('sprites\Sky driving.gif')
        frame_index = 0

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill ((0, 0, 0)) # Clear the screen
            self.screen.blit (pygame.transform.scale(frames[frame_index],  (800, 600)), (0, 0)) # Draw the current frame
            self.affiche_pkm ()
            pygame.display.flip() # Update the display

            frame_index += 1
            if frame_index >= len(frames):
                frame_index = 0 # Loop back to the first frame

            clock.tick(30) # Cap the frame rate at 30 FPS

        pygame.quit()

if __name__ == '__main__':
    ecran = changement ()
    ecran.main()