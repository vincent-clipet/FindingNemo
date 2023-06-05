# from .entity import Shark as Shark
# from entity import Fish as Fish
from .gui_tkinter import GuiTkinter
from .gamegridcell import GameGridCell
from .entity import Entity
from .shark import Shark
from .fish import Fish
import random





class GameGrid():

    
    turn = 0


    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.grid = [[0 for j in range(width)] for i in range(height)]
        self.grid = [[GameGridCell(j, i, None) for j in range(width)] for i in range(height)]



    # Random Fish & Shark generation

    def get_random_xy(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def random_fill_sharks(self, shark_number, energy_gain, base_energy, birth_interval, max_energy):
        for i in range(0, shark_number):
            while True:
                rand_x, rand_y = self.get_random_xy()
                cell = self.get_cell(rand_x, rand_y)
                if cell.is_empty():
                    cell.set_entity(Shark(energy_gain, base_energy, birth_interval, max_energy))
                    break

    def random_fill_fishs(self, fish_number, birth_interval, death_age):
        for i in range(0, fish_number):
            while True:
                rand_x, rand_y = self.get_random_xy()
                cell = self.get_cell(rand_x, rand_y)
                if cell.is_empty():
                    cell.set_entity(Fish(birth_interval, death_age))
                    break



    def draw_console(self):
        print("-" * (self.width+2))

        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                value = self.get_cell(x, y)
                line += value.draw()
            line += "|"
            print(line)
        print("-" * (self.width+2))

    def draw_console_buffered(self):
        buffer = ""
        buffer += "-" * (self.width+2)

        for y in range(self.height):
            buffer += "|"
            for x in range(self.width):
                value = self.get_cell(x, y)
                buffer += value.draw()
            buffer += "\n"
        buffer += "-" * (self.width+2)
        print(buffer)
    
    def draw_tkinter(self, gui: GuiTkinter):
        gui.update_turn(self.turn)
        gui.canvas.delete("all")
        gui.canvas.configure(bg="#202040")
        print("turn = ", self.turn)
        for y in range(self.height):
            for x in range(self.width):
                value = self.get_cell(x, y)
                if value.is_fish():
                    gui.draw_fish(x, y)
                elif value.is_shark():
                    gui.draw_shark(x, y)
                elif value.is_empty():
                    gui.draw_water(x, y)
        # gui.canvas.pack()


    def get_cell(self, x, y) -> GameGridCell: 
        return self.grid[y % self.height][x % self.width]

    def set_cell(self, cell, x, y):
        self.grid[y % self.height][x % self.width] = cell



    # get a list of currently available cells
    def get_surrounding_free_cells(self, x, y):
        free_cells = []
        surrounding_cells = self.get_surroundings(x, y)
        for i in range(0, len(surrounding_cells)):
            adjacent_cell = surrounding_cells[i]
            if adjacent_cell.is_empty():
                free_cells.append(adjacent_cell)
        return free_cells
    
    # get a list of nearby fishes (N-S-E-W)
    def get_surrounding_fishs(self, x, y):
        fish_cells = []
        surrounding_cells = self.get_surroundings(x, y)
        for i in range(0, len(surrounding_cells)):
            adjacent_cell = surrounding_cells[i]
            if adjacent_cell.is_fish():
                fish_cells.append(adjacent_cell)
        return fish_cells
    
    # get a list of nearby sharks (N-S-E-W)
    def get_surrounding_sharks(self, x, y):
        shark_cells = []
        surrounding_cells = self.get_surroundings(x, y)
        for i in range(0, len(surrounding_cells)):
            adjacent_cell = surrounding_cells[i]
            if adjacent_cell.is_shark():
                shark_cells.append(adjacent_cell)
        return shark_cells

    # get a list of all 4 neighbours (N-S-E-W)
    def get_surroundings(self, x, y):
        ret = []
        ret.append(self.get_cell(x, y-1)) # North
        ret.append(self.get_cell(x+1, y)) # East
        ret.append(self.get_cell(x, y+1)) # South
        ret.append(self.get_cell(x-1, y)) # West
        return ret
    

    def update(self):
        self.turn += 1
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                # empty cell
                if cell.is_empty():
                    continue
                # Update
                cell.entity.update(self, cell)
