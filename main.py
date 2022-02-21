import pygame
from pygame.draw import *

pygame.init()

FPS=30
screen=pygame.display.set_mode((500, 500))
screen.fill((127, 127, 127))
circle(screen, (255, 255, 0), (250, 250), 230)
circle(screen, (0, 0, 0), (250, 250), 230, 3)
circle(screen, (255, 0, 0), (125, 190), 50)
circle(screen, (255, 0, 0), (375, 190), 35)
circle(screen, (0, 0, 0), (375, 190), 20)
circle(screen, (0, 0, 0), (125, 190), 25)
circle(screen, (0, 0, 0), (125, 190), 50, 3)
circle(screen, (0, 0, 0), (375, 190), 35, 3)
rect(screen, (0, 0, 0), (125, 355, 250, 35))
line(screen, (0, 0, 0), (200, 160), (10, 65), 25)
line(screen, (0, 0, 0), (305, 170), (490, 90), 25)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()