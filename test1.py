import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define the rectangle (x, y, width, height)
button_rect = pygame.Rect(100, 100, 150, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = event.pos
            # Check if the mouse click was within the rectangle
            if button_rect.collidepoint(mouse_pos):
                print("Rectangle clicked!")

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    overlay = pygame.transform.scale (pygame.image.load ("sprites/pkm_joueur_bare_vie.png"), (800,150))
    screen.blit (overlay, (200, 200))

    pygame.display.flip()

# Quit Pygame
pygame.quit()