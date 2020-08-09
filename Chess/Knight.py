class Knight():
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
            ax=self.x-2
            ay=self.y+1
            bx=self.x-1
            by=self.y+2
            cx=self.x+1
            cy=self.y+2
            dx=self.x+2
            dy=self.y+1
            ex=self.x+2
            ey=self.y-1
            fx=self.x+1
            fy=self.y-2
            gx=self.x-1
            gy=self.y-2
            hx=self.x-2
            hy=self.y-1
            arra=[ax,ay,bx,by,cx,cy,dx,dy,ex,ey,fx,fy,gx,gy,hx,hy]
            for i in range(15):
                if arra[i]==-1:
                    arra[i]+=2
                elif arra[i]==-2:
                    arra[i]+=4
                elif arra[i]==8:
                    arra[i]-=2
                elif arra[i]==9:
                    arra[i]-=4
            print (arra)
            if self.color=='w':
                for i in range(0,15,2):
                    if board.boards[arra[i]][arra[i+1]][0]=='b' or board.boards[arra[i]][arra[i+1]]=='empty':
                        self.availableMoves[arra[i]][arra[i+1]]='v'
                    
            elif self.color=='b':
                for i in range(0,15,2):
                    if board.boards[arra[i]][arra[i+1]][0]=='w' or board.boards[arra[i]][arra[i+1]]=='empty':
                        self.availableMoves[arra[i]][arra[i+1]]='v'
    def checkMove(self,pos):
        if self.availableMoves[pos[0]][pos[1]]=='v':
            return True
        else:
            return False


