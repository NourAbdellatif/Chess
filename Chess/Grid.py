import math
import Functions as func
grid=[[0]*524 for i in range(524)]
for i in range (524):
    for j in range (524):
        x=math.ceil(float((i-524)/64))+7
        y=-1*math.ceil(float((j-524)/64))
        z=[x,y]
        grid[i][j]=z
mappedgrid=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        mappedgrid[i][j]=[i*65.5,abs(j*65.5-524+65.5)]
class Board():
    def __init__(self):
        self.white=['wrook','wknight','wbish','wqueen','wking','wbish','wknight','wrook']
        self.black=['brook','bknight','bbish','bqueen','bking','bbish','bknight','brook']
        self.boards=[['']*8 for i in range (8)]
    
    def SetBoard(self):
        for i in range(8):
            for j in range(8):
                self.boards[i][j]='empty'
        for i in range(8):
            self.boards[i][1]='wpawn'
            self.boards[i][6]='bpawn'
            self.boards[i][0]=self.white[i]
            self.boards[i][7]=self.black[i]

    def getPiece(self):
        pos=func.getPosition()
        return self.boards[pos[0]][pos[1]]
    def update(self,old,new):
        if self.boards[old[0]][old[1]]!='empty':
            piece=self.boards[old[0]][old[1]]
            self.boards[old[0]][old[1]]='empty'
            self.boards[new[0]][new[1]]=piece
    def returnBoard(self):
        return self.boards