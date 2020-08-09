class Rook():
    def __init__(self,color):
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
                if self.y!=7:
                    up=True
                    count=self.y+1
                    while up==True and count<8:
                        if board.boards[self.x][count]=='empty':
                            self.availableMoves[self.x][count]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[self.x][count]='v'
                            up=False
                        else:
                            up=False
                if self.y!=0:
                    down=True
                    count=self.y-1
                    while down==True and count>=0:
                        if board.boards[self.x][count]=='empty':
                            self.availableMoves[self.x][count]='v'
                            count-=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[self.x][count]='v'
                            down=False
                        else:
                            down=False
                if self.x!=7:
                    right=True
                    count=self.x+1
                    while right==True and count<8:
                        if board.boards[count][self.y]=='empty':
                            self.availableMoves[count][self.y]='v'
                            count+=1
                        elif board.boards[count][self.y][0]=='b':
                            self.availableMoves[count][self.y]='v'
                            right=False
                        else:
                            right=False
                if self.x!=0:
                    left=True
                    count=self.x-1
                    while left==True and count>=0:
                        if board.boards[count][self.y]=='empty':
                            self.availableMoves[count][self.y]='v'
                            count-=1
                        elif board.boards[count][self.y][0]=='b':
                            self.availableMoves[count][self.y]='v'
                            left=False
                        else:
                            left=False
            elif self.color=='b':
                if self.y!=7:
                    up=True
                    count=self.y+1
                    while up==True and count<8:
                        if board.boards[self.x][count]=='empty':
                            self.availableMoves[self.x][count]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='w':
                            self.availableMoves[self.x][count]='v'
                            up=False
                        else:
                            up=False
                if self.y!=0:
                    down=True
                    count=self.y-1
                    while down==True and count>=0:
                        if board.boards[self.x][count]=='empty':
                            self.availableMoves[self.x][count]='v'
                            count-=1
                        elif board.boards[self.x][count][0]=='w':
                            self.availableMoves[self.x][count]='v'
                            down=False
                        else:
                            down=False
                if self.x!=7:
                    right=True
                    count=self.x+1
                    while right==True and count<8:
                        if board.boards[count][self.y]=='empty':
                            self.availableMoves[count][self.y]='v'
                            count+=1
                        elif board.boards[count][self.y][0]=='w':
                            self.availableMoves[count][self.y]='v'
                            right=False
                        else:
                            right=False
                if self.x!=0:
                    left=True
                    count=self.x-1
                    while left==True and count>=0:
                        if board.boards[count][self.y]=='empty':
                            self.availableMoves[count][self.y]='v'
                            count-=1
                        elif board.boards[count][self.y][0]=='w':
                            self.availableMoves[count][self.y]='v'
                            left=False
                        else:
                            left=False
    def checkMove(self,pos):
        if self.availableMoves[pos[0]][pos[1]]=='v':
            return True
        else:
            return False

