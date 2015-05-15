import curses

def end():
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	return 0

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)
curses.curs_set(False)

curses.start_color()

for i2 in range(curses.COLORS):
	x = i2 * 8
	for i in range(curses.COLORS):
		curses.init_pair(i + x + 1, i, i2)

class ncfc:
	black = 1
	red = 2
	green = 3
	orange = 4
	blue = 5
	pink = 6
	magenta = 7
	grey = 8

class ncbc:
	black = 0
	red = 8
	green = 16
	orange = 24
	blue = 32
	pink = 40
	magenta = 48
	grey = 56

nfc = [ncfc.black, ncfc.red, ncfc.green, ncfc.orange, ncfc.blue, ncfc.pink, ncfc.magenta, ncfc.grey]

nbc = [ncbc.black, ncbc.red, ncbc.green, ncbc.orange, ncbc.blue, ncbc.pink, ncbc.magenta, ncbc.grey]

