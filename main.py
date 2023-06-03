##########
# CONFIG #
##########

REFRESH_SPEED = 0.2
CLEAR_EACH_FRAME = True
CLEAR_WINDOWS = True # 'True' for Windows, 'False' for Unix-based consoles
BUFFERED_PRINT = False

GRID_WIDTH = 150
GRID_HEIGHT = 50

ENTITY_SHARK_COUNT = 50
ENTITY_SHARK_ENERGY_GAIN = 5
ENTITY_SHARK_BASE_ENERGY = 10
ENTITY_SHARK_BIRTH_INTERVAL = 15
ENTITY_SHARK_MAX_ENERGY = 20

ENTITY_FISH_COUNT = 70
ENTITY_FISH_BIRTH_INTERVAL = 4
ENTITY_FISH_DEATH_AGE = 40



###########
# IMPORTS #
###########

import random
import os
import time
from src.gamegrid import GameGrid as GameGrid
from src.shark import Shark
from src.fish import Fish



#######
# RUN #
#######

g = GameGrid(GRID_WIDTH, GRID_HEIGHT)
g.random_fill_sharks(
	ENTITY_SHARK_COUNT,
	ENTITY_SHARK_ENERGY_GAIN,
	ENTITY_SHARK_BASE_ENERGY,
	ENTITY_SHARK_BIRTH_INTERVAL,
	ENTITY_SHARK_MAX_ENERGY)
g.random_fill_fishs(
	ENTITY_FISH_COUNT,
	ENTITY_FISH_BIRTH_INTERVAL,
	ENTITY_FISH_DEATH_AGE)



while True:
	if CLEAR_EACH_FRAME:
		os.system("cls") if CLEAR_WINDOWS else os.system("cls")
	print("turn = ", g.turn)
	g.update()
	if BUFFERED_PRINT: g.draw_console_buffered()
	else: g.draw_console()
	time.sleep(REFRESH_SPEED)


