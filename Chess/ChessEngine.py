import itertools
import pygame as pg


pg.init()

BLACK = pg.Color('black')
WHITE = pg.Color('white')

screen = pg.display.set_mode((800, 700))
clock = pg.time.Clock()
colors = itertools.cycle((WHITE, BLACK))
tile_size = 60
width, height = 8*tile_size, 8*tile_size
background = pg.Surface((width, height))
pawn=pg.image.load("blackPawn.png")
pawnRect=pawn.get_rect()
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pg.draw.rect(background, next(colors), rect)
    next(colors)

game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True
    
    screen.fill((60, 70, 90))
    screen.blit(background, (100, 100))
    screen.blit(pawn,pawnRect)
    if event.type == pg.MOUSEBUTTONUP:
        game_exit=True
    pg.display.flip()
    clock.tick(30)

pg.quit()