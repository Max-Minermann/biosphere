import random

def flat(world, worldx, worldy, worldz):
	for i in range(worldx):
		for i2 in range(worldy):
			for i3 in range(0,100):
				world[i][i2][i3][0] = 1
				world[i][i2][i3][1] = 0
			for i3 in range(100,126):
				world[i][i2][i3][0] = 1
				world[i][i2][i3][1] = 1
	return world
