##########
# CONFIG #
##########

REFRESH_SPEED = 0.5
CLEAR_EACH_FRAME = True

GRID_WIDTH = 60
GRID_HEIGHT = 15

ENTITY_SHARK_COUNT = 5
ENTITY_SHARK_MAX_ENERGY = 10
ENTITY_SHARK_ENERGY_GAIN = 4

ENTITY_FISH_COUNT = 1
ENTITY_FISH_BIRTH_INTERVAL = 5



###########
# IMPORTS #
###########

import random
import os
import time
from src.gamegrid import GameGrid as GameGrid
from src.entity import Shark
from src.entity import Fish



#############
# FUNCTIONS #
#############





#######
# RUN #
#######

g = GameGrid(GRID_WIDTH, GRID_HEIGHT)
g.random_fill_sharks(ENTITY_SHARK_COUNT, ENTITY_SHARK_MAX_ENERGY, ENTITY_SHARK_ENERGY_GAIN)
g.random_fill_fishs(ENTITY_FISH_COUNT, ENTITY_FISH_BIRTH_INTERVAL)



while True:
	if CLEAR_EACH_FRAME: os.system("cls")
	print("turn = ", g.turn)
	g.update()
	g.draw_console()
	time.sleep(REFRESH_SPEED)


