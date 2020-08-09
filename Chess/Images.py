import pygame
class image():
    def __init__(self):
        self.bpawn=pygame.image.load("imges/blackPawn.png")
        self.bbish=pygame.image.load("imges/blackBishop.png")
        self.bking=pygame.image.load("imges/blackKing.png")
        self.bknight=pygame.image.load("imges/blackKnight.png")
        self.bqueen=pygame.image.load("imges/blackQueen.png")
        self.brook=pygame.image.load("imges/blackRook.png")
        self.black=[self.brook,self.bknight,self.bbish,self.bqueen,self.bking,self.bbish,self.bknight,self.brook]
        self.wpawn=pygame.image.load("imges/whitePawn.png")
        self.wbish=pygame.image.load("imges/whiteBishop.png")
        self.wknight=pygame.image.load("imges/whiteKnight.png")
        self.wqueen=pygame.image.load("imges/whiteQueen.png")
        self.wrook=pygame.image.load("imges/whiteRook.png")
        self.wking=pygame.image.load("imges/whiteKing.png")
        self.white=[self.wrook,self.wknight,self.wbish,self.wqueen,self.wking,self.wbish,self.wknight,self.wrook]
