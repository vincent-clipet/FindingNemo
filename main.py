##########
# CONFIG #
##########

REFRESH_SPEED = 0.5
CLEAR_EACH_FRAME = True
BUFFERED_PRINT = False
USE_GUI = True
GUI_WIDTH = 800
GUI_HEIGHT = 600
GUI_CELL_SIZE = 6

GRID_WIDTH = 10
GRID_HEIGHT = 8

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
from src.gui_tkinter import GuiTkinter
from src.gamegrid import GameGrid as GameGrid
from src.shark import Shark
from src.fish import Fish



#######
# RUN #
#######

grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)
grid.random_fill_sharks(
	ENTITY_SHARK_COUNT,
	ENTITY_SHARK_ENERGY_GAIN,
	ENTITY_SHARK_BASE_ENERGY,
	ENTITY_SHARK_BIRTH_INTERVAL,
	ENTITY_SHARK_MAX_ENERGY)
grid.random_fill_fishs(
	ENTITY_FISH_COUNT,
	ENTITY_FISH_BIRTH_INTERVAL,
	ENTITY_FISH_DEATH_AGE)





def update_gui(g, gui):
	g.update()
	g.draw_tkinter(gui)
	gui.after(int(REFRESH_SPEED * 1000), update_gui(g, gui))

# if USE_GUI:
# 	gui = GuiTkinter(GUI_WIDTH, GUI_HEIGHT, GUI_CELL_SIZE)
# 	gui.after(int(REFRESH_SPEED * 1000), update_gui(grid, gui))
# 	gui.mainloop()

if USE_GUI:
	gui = GuiTkinter(GUI_WIDTH, GUI_HEIGHT, GUI_CELL_SIZE)
	while True:
		grid.update()
		grid.draw_tkinter(gui)
		gui.window.update()
		time.sleep(REFRESH_SPEED)
	gui.window.after(int(REFRESH_SPEED * 1000))
	gui.window.mainloop()

else:
	while True:
		if CLEAR_EACH_FRAME: os.system("cls")
		print("turn = ", grid.turn)
		grid.update()
		if BUFFERED_PRINT: grid.draw_console_buffered()
		else: grid.draw_console()
		time.sleep(REFRESH_SPEED)