class king():
    def __init__(self,col
                 
                 
                 ):
        self.color=color
        self.x=None
        self.y=None
        self.availableMoves=[['i']*8 for i in range(8)]
    def updateCoordinate(self,pos):
        self.x=pos[0]
        self.y=pos[1]

    def updateMoves(self,board):
        if board.boards[self.x][self.y][0]==self.color:
            if self.color=='w':
                if board.boards[self.x-1][self.y+1][0]=='b':
                    self.availableMoves[self.x-1][self.y+1]='v'
                if board.boards[self.x+1][self.y+1][0]=='b':
                    self.availableMoves[self.x+1][self.y+1]='v'
                if board.boards[self.x][self.y+1]!='empty':
                    self.availableMoves[self.x][self.y-1]='i'
                else:
                    if self.y==1:
                        self.availableMoves[self.x][self.y+2]='v'
                    self.availableMoves[self.x][self.y+1]='v'
            elif self.color=='b':
                if board.boards[self.x-1][self.y-1][0]=='w':
                    self.availableMoves[self.x-1][self.y-1]='v'
                if board.boards[self.x+1][self.y-1][0]=='w':
                    self.availableMoves[self.x+1][self.y-1]='v'
                if board.boards[self.x][self.y-1]!='empty':
                    self.availableMoves[self.x][self.y-1]='i'
                else:
                    if self.y==6:
                        self.availableMoves[self.x][self.y-2]='v'
                    self.availableMoves[self.x][self.y-1]='v'
    def checkMove(self,pos):
        if self.availableMoves[pos[0]][pos[1]]=='v':
            return True
        else:
            return False


