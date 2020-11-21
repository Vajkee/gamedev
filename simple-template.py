import pygame

# ---- Define colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
PURPLE = (128, 0, 128)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)
CORNFLOWERBLUE = (100, 149, 237)

# ---- Window settings
WIDTH = 800
HEIGHT = 600
TITLE = "Simple Template"
FPS = 60
BGCOLOR = CORNFLOWERBLUE

# ---- Init pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---- Game objects
# ---- Example:
# player_surface = pygame.Surface((50, 50)) 
# player_surface.fill(GREEN)
# player_location = [100, 100]
# player_rect = pygame.Rect(player_location[0], player_location[1], player_surface.get_width(), player_surface.get_height())

# ---- Game loop
while not done:
    # ---- Game events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
        # ---- More game logic

    # ---- Update method
    # pygame.display.update() or
    pygame.display.flip()

    # ---- Draw / Render method
    # -- Screen clearing
    screen.fill(BGCOLOR)
    # -- More Draw / Render code
    # screen.blit(player_surface, player_rect)

    # ---- Limit to 60 frames per second
    clock.tick(FPS)

pygame.quit()