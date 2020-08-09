import pygame
import Images
import Functions as func
import Grid
image=Images.image()
size=width,height=524,524
color=75,0,130
screen=pygame.display.set_mode(size)
def init():
    print("White Turn")
    pygame.init()
    pygame.display.set_caption("Chess")
    pygame.display.set_icon(image.wking)
    boards=pygame.image.load("pict.png")
    boardRect=boards.get_rect()
    screen.fill(color)
    screen.blit(boards,boardRect)
def Start():
    x,y=10,0
    for i in range(0,8):
        screen.blit(image.bpawn,(x,y+70))
        screen.blit(image.black[i],(x,y+10))
        screen.blit(image.wpawn,(x,y+400))
        screen.blit(image.white[i],(x,y+460))
        x+=65.5
def updateDisplay(board):
    x=8
    boards=pygame.image.load("pict.png")
    boardRect=boards.get_rect()
    screen.fill(color)
    screen.blit(boards,boardRect)
    for i in range(8):
        for j in range(8):
            map=Grid.mappedgrid[i][j]
            if board.boards[i][j]=='wpawn':
                screen.blit(image.wpawn,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='bpawn':
                screen.blit(image.bpawn,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='wrook':
                screen.blit(image.wrook,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='brook':
                screen.blit(image.brook,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='wknight':
                screen.blit(image.wknight,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='bknight':
                screen.blit(image.bknight,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='wbish':
                screen.blit(image.wbish,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='bbish':
                screen.blit(image.bbish,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='wking':
                screen.blit(image.wking,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='bking':
                screen.blit(image.bking,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='wqueen':
                screen.blit(image.wqueen,(map[0]+x,map[1]+x))
            elif board.boards[i][j]=='bqueen':
                screen.blit(image.bqueen,(map[0]+x,map[1]+x))