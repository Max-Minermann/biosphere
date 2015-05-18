#!/usr/bin/env python3
import random, generator
from things import*
from ncursescolor import*


worldx = 24
worldy = 80
worldz = 256
viewz = 125
world = [[[[0 for x in range(3)] for x in range(worldz)] for x in range(worldy)] for x in range(worldx)]

height, width = stdscr.getmaxyx()
world = generator.flat(world, worldx, worldy, worldz)


while True:	
	for x in range(worldx):
		for y in range(worldy):
			if world[x][y][viewz][0] == 0:
				stdscr.bkgdset(curses.color_pair(nfc[thingnummer[world[x][y][viewz][0]].sayfc()] + nbc[thingnummer[world[x][y][viewz][0]].saybc()]))
				try:
					stdscr.addch(x, y, thingnummer[world[x][y][viewz][0]].saychar())
				except curses.error:
					pass
			elif world[x][y][viewz][0] == 1:
				stdscr.bkgdset(curses.color_pair(nfc[blocknummer[world[x][y][viewz][1]].sayfc()] + nbc[blocknummer[world[x][y][viewz][1]].saybc()]))
				try:
					stdscr.addch(x, y, blocknummer[world[x][y][viewz][1]].saychar())
				except curses.error:
					pass
			elif world[x][y][viewz][0] == 2:
				stdscr.bkgdset(curses.color_pair(nfc[creaturenummer[world[x][y][viewz][1]].sayfc()] + nbc[creaturenummer[world[x][y][viewz][1]].saybc()]))
				try:
					stdscr.addch(x, y, creaturenummer[world[x][y][viewz][1]].saychar())
				except curses.error:
					pass
	stdscr.refresh()
	ch = stdscr.getkey()
	if ch == "q":
		break
	elif ch == "w":
		for i in range(worldx):
			for i2 in range(worldy):
				if world[i][i2][viewz][0] == 2 and world[i][i2][viewz][1] == 1:
					world[i][i2][viewz][0] = 0
					world[i][i2][viewz][1] = 0
					world[i - 1][i2][viewz][0] = 2
					world[i - 1][i2][viewz][1] = 1
					break
	elif ch == "a":
		for i in range(worldx):
			for i2 in range(worldy):
				if world[i][i2][viewz][0] == 2 and world[i][i2][viewz][1] == 1:
					world[i][i2][viewz][0] = 0
					world[i][i2][viewz][1] = 0
					world[i][i2 - 1][viewz][0] = 2
					world[i][i2 - 1][viewz][1] = 1
					break
	elif ch == "c":
		y = random.randint(0, worldy - 1)
		x = random.randint(0, worldx - 1)
		world[x][y][viewz][0] = 2
		world[x][y][viewz][1] = 1

end()
