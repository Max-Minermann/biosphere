#!/usr/bin/env python3
import random, generator
from things import*
from ncursescolor import*


worldx = 24
worldy = 80
worldz = 20
world = [[[[0 for x in range(3)] for x in range(worldx)] for x in range(worldy)] for x in range(worldz)]

height, width = stdscr.getmaxyx()
world = generator.flat(world, worldx, worldy, worldz)


while True:	
	for x in range(worldx):
		for y in range(worldy):
			if world[10][y][x][0] == 0:
				stdscr.bkgdset(curses.color_pair(nfc[thingnummer[world[10][y][x][0]].sayfc()] + nbc[thingnummer[world[10][y][x][0]].saybc()]))
				try:
					stdscr.addch(x, y, thingnummer[world[10][y][x][0]].saychar())
				except curses.error:
					pass
			elif world[10][y][x][0] == 1:
				stdscr.bkgdset(curses.color_pair(nfc[blocknummer[world[10][y][x][1]].sayfc()] + nbc[blocknummer[world[10][y][x][1]].saybc()]))
				try:
					stdscr.addch(x, y, blocknummer[world[10][y][x][1]].saychar())
				except curses.error:
					pass
			elif world[10][y][x][0] == 2:
				stdscr.bkgdset(curses.color_pair(nfc[creaturenummer[world[10][y][x][1]].sayfc()] + nbc[creaturenummer[world[10][y][x][1]].saybc()]))
				try:
					stdscr.addch(x, y, creaturenummer[world[10][y][x][1]].saychar())
				except curses.error:
					pass
	stdscr.refresh()
	ch = stdscr.get_wch()
	if ch == "q":
		break
	elif ch == "h":
		y = random.randint(0, worldy - 1)
		x = random.randint(0, worldx - 1)	
		world[10][y][x][0] = 2
		world[10][y][x][1] = 0
	elif ch == "c":
		y = random.randint(0, worldy - 1)
		x = random.randint(0, worldx - 1)
		world[10][y][x][0] = 2
		world[10][y][x][1] = 1

end()
