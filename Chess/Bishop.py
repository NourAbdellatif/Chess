class Bishop():
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
                if not(self.x!=7 and self.y!=7):
                    count=1
                    Trx=self.x
                    Try=self.y
                    tr=True
                    while tr and Trx<8 and Try<8:
                        Trx+=count
                        Try+=count
                        if board.boards[Trx][Try]=='empty':
                            self.availableMoves[Trx][Try]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[Trx][Try]='v'
                            tr=False
                        else:
                            tr=False
                if not(self.x!=0 and self.y!=7):
                    count=1
                    Trx=self.x
                    Try=self.y
                    tr=True
                    while tr and Trx<8 and Try>=0:
                        Trx+=count
                        Try-=count
                        if board.boards[Trx][Try]=='empty':
                            self.availableMoves[Trx][Try]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[Trx][Try]='v'
                            tr=False
                        else:
                            tr=False
                if not(self.x!=7 and self.y!=0):
                    count=1
                    Trx=self.x
                    Try=self.y
                    tr=True
                    while tr and Trx>=0 and Try<8:
                        Trx-=count
                        Try+=count
                        if board.boards[Trx][Try]=='empty':
                            self.availableMoves[Trx][Try]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[Trx][Try]='v'
                            tr=False
                        else:
                            tr=False
                if not(self.x!=0 and self.y!=0):
                    count=1
                    Trx=self.x
                    Try=self.y
                    tr=True
                    while tr and Trx>=0 and Try>=0:
                        Trx-=count
                        Try-=count
                        if board.boards[Trx][Try]=='empty':
                            self.availableMoves[Trx][Try]='v'
                            count+=1
                        elif board.boards[self.x][count][0]=='b':
                            self.availableMoves[Trx][Try]='v'
                            tr=False
                        else:
                            tr=False
            elif self.color=='b':
                self.availableMoves[self.x][self.y-1]='v'
    def checkMove(self,pos):
        if self.availableMoves[pos[0]][pos[1]]=='v':
            return True
        else:
            return False
