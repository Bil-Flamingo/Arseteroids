import pygame
from CONSTANTS import SCREENHEIGHT, SCREENWIDTH, pc_edge,
from LOGGER import
from MOBS import


pygame.init()

screen = pygame.display.Set_mode((SCREENHEIGHT, SCREENWIDTH))
clock = pygame.time.Clock()
running = True
dt = 0

pc_pos = pygame.Vector2(SCREENWIDTH/2, SCREENHEIGHT/2)

#load images here, blit in loop.
screen_sprite = pygame.image.load("screen-art").convert()
pc_sprite = pygame.image.load("pc.jpeg").convert()
smAst_sprite =
mdAst_sprite =
bgAst_sprite =

while running == True:
    for event in pygame.event_get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    #this may be a blit rather than fill later, once im using a jpg for the screen. it will still be initialised by
    #pixels/resolution but blitted over rather than filled here, i believe.
    pygame.draw.rect(screen, "green", rect, pc_edge) #idfk help

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.QUIT()