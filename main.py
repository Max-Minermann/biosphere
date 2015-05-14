import tty
import sys
import random
from tput import*
from blocks import*
from creatures import*

world = [[[[0 for x in range(3)] for x in range(20)] for x in range(20)] for x in range(20)]
tty.setcbreak(sys.stdin)

world[10][15][13][1] = 1
	
while True:
	for x in range(20):
		for y in range(20):
			print(bc[blocknummer[world[10][x][y][0]].saybg()] + fc[creaturenummer[world[10][x][y][1]].sayfc()] + creaturenummer[world[10][x][y][1]].saychar(), end="")
		print(bc[1] + fc[2] + "")
	ch = sys.stdin.read(1)
	if ch == "a":
		world[10][random.randint(0,19)][random.randint(0,19)][1] = 1
	elif ch == "b":
		world[10][random.randint(0,19)][random.randint(0,19)][1] = 2
	elif ch == "q":
		break
