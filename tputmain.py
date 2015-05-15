import os, sys, tty, random, time
from tput import*
from blocks import*
from creatures import*

worldx = 24
worldy = 80
worldz = 20
world = [[[[0 for x in range(3)] for x in range(worldx)] for x in range(worldy)] for x in range(worldz)]
tty.setcbreak(sys.stdin)
os.system("setterm -cursor off")
	
while True:	
	for x in range(worldx):
		line = ""
		for y in range(worldy):
			line += (tbc[blocknummer[world[10][y][x][0]].saybg()] + tfc[creaturenummer[world[10][y][x][1]].sayfc()] + creaturenummer[world[10][y][x][1]].saychar())
		if x == worldx -1:
			print(line, end="\r")
		else:
			print(line)
#	not sure
#	time.sleep(0.10)
	ch = sys.stdin.read(1)
	if ch == "h":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 1
	elif ch == "c":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 2
	elif ch == "q":
		break
