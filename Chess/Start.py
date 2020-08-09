import sys,pygame
from pygame.locals import *
import Images
import Functions as func
import Grid
import Display
board=Grid.Board()
board.SetBoard()
click=1
position=[None]*2
color=[None]*2
turn='w'
def clicks():
    global click,color,position,turn,piece
    Display.updateDisplay(board)
    for event in pygame.event.get():
        if func.checkClick(event):
            if click==1:
                Display.updateDisplay(board)
                position[0]=func.getPosition()
                Piececlicked1=board.getPiece()
                if Piececlicked1!='empty':
                    piece=func.pieceKind(Piececlicked1)
                    piece.updateCoordinate(position[0])
                    piece.updateMoves(board)
                    color[0]=func.getColor(Piececlicked1)
                    if color[0]==turn:
                        if Piececlicked1!='empty':
                            click=2
                            break
                    else:
                        print("Not your turn ya ahbal")
                        break
            if func.checkClick(event) and click==2:
                    Piececlicked2=board.getPiece()
                    color[1]=func.getColor(Piececlicked2)
                    position[1]=func.getPosition()
                    piece.updateMoves(board)
                    if piece.checkMove(position[1]):
                        if color[0]==color[1]:
                            print("Invalid Move")
                            click=1
                            break
                        board.update(position[0],position[1])
                        Display.updateDisplay(board)
                        click=1
                        if turn=='w':
                            turn='b'
                            print("Black Turn")
                        else:
                            turn='w'
                            print("White Turn")
                        break
                    else:
                        print("Invalid move 2")
                        click=1
                        break


