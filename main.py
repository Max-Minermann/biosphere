import random
from blocks import*
from creatures import*
from ncursescolor import*

worldx = 24
worldy = 80
worldz = 20
world = [[[[0 for x in range(3)] for x in range(worldx)] for x in range(worldy)] for x in range(worldz)]

while True:	
	for x in range(worldx):
		for y in range(worldy):
			stdscr.bkgdset(curses.color_pair(nfc[creaturenummer[world[10][y][x][1]].sayfc()] + nbc[blocknummer[world[10][y][x][0]].saybg()]))
			try:
				stdscr.addstr(x, y, creaturenummer[world[10][y][x][1]].saychar())
			except curses.error:
				pass
	stdscr.refresh()
	ch = stdscr.get_wch()
	if ch == "q":
		break
	elif ch == "h":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 1
	elif ch == "c":
		world[10][random.randint(0,worldy - 1)][random.randint(0,worldx - 1)][1] = 2
	
end()
