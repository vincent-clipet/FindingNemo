##########
# CONFIG #
##########

# console
REFRESH_SPEED = 2
CLEAR_EACH_FRAME = True
BUFFERED_PRINT = False

# tkinter GUI
USE_GUI = True
GUI_WIDTH = 1200
GUI_HEIGHT = 800
GUI_OFFSET_WINDOW_POSITION = -1500 # pixels, can be +-
GUI_CELL_SIZE = 10
GUI_UPDATE_INTERVAL = 1 # ms

# Grid param
GRID_WIDTH = 120
GRID_HEIGHT = 80
# Shark
ENTITY_SHARK_COUNT = 50
ENTITY_SHARK_ENERGY_GAIN = 5
ENTITY_SHARK_BASE_ENERGY = 10
ENTITY_SHARK_BIRTH_INTERVAL = 15
ENTITY_SHARK_MAX_ENERGY = 20
# Fish
ENTITY_FISH_COUNT = 70
ENTITY_FISH_BIRTH_INTERVAL = 4
ENTITY_FISH_DEATH_AGE = 40



###########
# IMPORTS #
###########

import random
import os
import time
from tkinter import Canvas, Label, StringVar, Tk
from src.gui_tkinter import GuiTkinter
from src.gamegrid import GameGrid as GameGrid
from src.shark import Shark
from src.fish import Fish

#######
# RUN #
#######

grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)
grid.random_fill_sharks(ENTITY_SHARK_COUNT, ENTITY_SHARK_ENERGY_GAIN, ENTITY_SHARK_BASE_ENERGY, ENTITY_SHARK_BIRTH_INTERVAL, ENTITY_SHARK_MAX_ENERGY)
grid.random_fill_fishs(ENTITY_FISH_COUNT, ENTITY_FISH_BIRTH_INTERVAL, ENTITY_FISH_DEATH_AGE)




def loop():
    grid.update()
    gui.canvas.delete("all")
    grid.draw_tkinter(gui)
    gui.window.after(GUI_UPDATE_INTERVAL, loop)


if USE_GUI:
    gui = GuiTkinter(GUI_WIDTH, GUI_HEIGHT, GUI_CELL_SIZE, GUI_OFFSET_WINDOW_POSITION)
    loop()
    gui.window.mainloop()
else:
    while True:
        if CLEAR_EACH_FRAME: os.system("cls")
        print("turn = ", grid.turn)
        grid.update()
        if BUFFERED_PRINT: grid.draw_console_buffered()
        else: grid.draw_console()
        time.sleep(REFRESH_SPEED)
