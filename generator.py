import random

def flat(world, worldx, worldy, worldz):
	for i in range(worldx):
		for i2 in range(worldy):
			world[10][i2][i][0] = 1
			world[10][i2][i][1] = random.randint(0,1)
	return world
