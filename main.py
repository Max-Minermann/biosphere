import os, sys, tty, random
from tput import*
from blocks import*
from creatures import*

worldx = 24
worldy = 80
worldz = 20
world = [[[[0 for x in range(3)] for x in range(worldx)] for x in range(worldy)] for x in range(worldz)]
tty.setraw(sys.stdin)
os.system('setterm -cursor off')
	
while True:
	line = ""
	for x in range(worldx):		
		for y in range(worldy):
			line += (bc[blocknummer[world[10][y][x][0]].saybg()] + fc[creaturenummer[world[10][y][x][1]].sayfc()] + creaturenummer[world[10][y][x][1]].saychar())
		if x != worldx - 1:
			line += ("\r\n")
		else:
			line += ("\r")
	print(line)
	ch = sys.stdin.read(1)
	if ch == "h":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 1
	elif ch == "c":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 2
	elif ch == "q":
		break
