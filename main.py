import tty
import curses
from tput import*
from blocks import*

world = [[[[0 for x in range(3)] for x in range(20)] for x in range(20)] for x in range(20)]
tty.setcbreak


for x in range(20):
	for y in range(20):
		print(bc[blocknummer[world[10][x][y][0]].saybg()] + " ", end="")
	print("")
	
