#!/usr/bin/python
import sys,pygame
from pygame.locals import *
import Display
import Functions as func
import Start
Display.init()
while 1:
    Start.clicks()
    pygame.display.flip()
