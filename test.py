import pygame
import os
pygame.init()
screen = pygame.display.set_mode((800, 600))
image_folder = 'image\maitre_fight'
images = []
clock = pygame.time.Clock()
for filename in os.listdir(image_folder):
   if filename.endswith('.png'):
       img = pygame.image.load(os.path.join(image_folder, filename))
       images.append(img)
current_image_index = 0
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RETURN:
               while current_image_index <= len(images)-1:
                screen.fill((0,0,0))
                screen.blit(images[current_image_index], (0, 0))
                pygame.display.flip()
                current_image_index += 1
                clock.tick(8)
           if current_image_index >= len(images):
            current_image_index = 0

pygame.quit()