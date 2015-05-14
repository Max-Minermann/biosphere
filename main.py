import tty
import curses
from tput import*
from blocks import*
from creatures import*

world = [[[[0 for x in range(3)] for x in range(20)] for x in range(20)] for x in range(20)]
tty.setcbreak

world[10][15][13][1] = 1

for x in range(20):
	for y in range(20):
		print(bc[blocknummer[world[10][x][y][0]].saybg()] + fc[creaturenummer[world[10][x][y][1]].sayfc()] + creaturenummer[world[10][x][y][1]].saychar(), end="")
	print("")
	
