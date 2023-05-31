##########
# CONFIG #
##########

GRID_WIDTH = 60
GRID_HEIGHT = 15
ENTITY_SHARK_COUNT = 5
ENTITY_FISH_COUNT = 10



###########
# IMPORTS #
###########

import random
from src.gamegrid import GameGrid as Grid
from src.entity import Shark
from src.entity import Fish



#############
# FUNCTIONS #
#############

def get_random_xy(max_x, max_y):
	return random.randint(0, max_x - 1), random.randint(0, max_y - 1)



#######
# RUN #
#######

g = Grid(GRID_WIDTH, GRID_HEIGHT)

for i in range(1, ENTITY_SHARK_COUNT):
	rand_x, rand_y = get_random_xy(GRID_WIDTH, GRID_HEIGHT)
	g.grid[rand_y][rand_x] = Shark()

for i in range(1, ENTITY_FISH_COUNT):
	rand_x, rand_y = get_random_xy(GRID_WIDTH, GRID_HEIGHT)
	g.grid[rand_y][rand_x] = Fish()


g.draw_console()

