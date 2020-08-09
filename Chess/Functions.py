import sys,pygame
from pygame.locals import *
import math
import Pawn
import Rook
import Knight
import Bishop
import King
import Queen

def getPosition():#returns array position
    coordinate=pygame.mouse.get_pos()
    x=math.ceil(float((coordinate[0]-524)/64))+7
    y=-1*math.ceil(float((coordinate[1]-524)/64))
    z=[x,y]
    return z
def getPixel():#returns coordinate
    position=pygame.mouse.get_pos()
    grid=Grid.grid[position[0]][position[1]]
    mapped=Grid.mappedgrid[grid[0]][grid[1]]
    return mapped
def checkClick(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
        return True
def delay(a):
    pygame.time.delay(a)
def getColor(piece):
    if piece[0]=='w':
        return 'w'
    elif piece[0]=='b':
        return 'b'
    else:
        return 'empty'
def pieceKind(piece):
    if piece[1:]=='pawn':
        pawn=Pawn.Pawn(piece[0])
        return pawn
    elif piece[1:]=='rook':
        rook=Rook.Rook(piece[0])
        return rook
    elif piece[1:]=='knight':
        knight=Knight.Knight(piece[0])
        return knight
    elif piece[1:]=='king':
        king=King.king(piece[0])
        return king
    elif piece[1:]=='bish':
        bish=Bishop.Bishop(piece[0])
        return bish
    elif piece[1:]=='queen':
        queen=Queen.Queen(piece[0])
        return queen

