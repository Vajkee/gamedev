import pygame

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

WIDTH = 800
HEIGHT = 600
TITLE = "Simple 2D Movement"
FPS = 60
BGCOLOR = CORNFLOWERBLUE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
done = False
clock = pygame.time.Clock()

player_surface = pygame.image.load("player.png")
player_scale = 10
player_surface = pygame.transform.scale(player_surface, (player_surface.get_width() * player_scale, player_surface.get_height() * player_scale))
player_location = [100, 100]
player_rect = pygame.Rect(player_location[0], player_location[1], player_surface.get_width(), player_surface.get_height())
player_speed = 5
move_up = False
move_down = False
move_left = False
move_right = False
flipped = False

while not done:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_UP:
                move_up = True
            if e.key == pygame.K_DOWN:
                move_down = True
            if e.key == pygame.K_LEFT:
                move_left = True
            if e.key == pygame.K_RIGHT:
                move_right = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                move_up = False
            if e.key == pygame.K_DOWN:
                move_down = False
            if e.key == pygame.K_LEFT:
                move_left = False
            if e.key == pygame.K_RIGHT:
                move_right = False

    if flipped == True:
        pygame.transform.flip(player_surface, True, False)
    if move_up == True:
        player_location[1] -= player_speed
    if move_down == True:
        player_location[1] += player_speed
    if move_left == True:
        player_location[0] -= player_speed
        flipped = True
    if move_right == True:
        player_location[0] += player_speed

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    pygame.display.flip()

    screen.fill(BGCOLOR)
    screen.blit(player_surface, player_rect)

    clock.tick(FPS)

pygame.quit()