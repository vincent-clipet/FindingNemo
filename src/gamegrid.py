# from .entity import Shark as Shark
# from entity import Fish as Fish
from .gamegridcell import GameGridCell
from .entity import Entity as Entity
from .entity import Shark as Shark
from .entity import Fish as Fish
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
    
    def random_fill_sharks(self, shark_number, max_energy, energy_gain):
        for i in range(0, shark_number):
            rand_x, rand_y = self.get_random_xy()
            cell = self.get_cell(rand_x, rand_y)
            cell.set_entity(Shark(max_energy, energy_gain))

    def random_fill_fishs(self, fish_number, birth_interval):
        for i in range(0, fish_number):
            rand_x, rand_y = self.get_random_xy()
            cell = self.get_cell(rand_x, rand_y)
            cell.set_entity(Fish(birth_interval))



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
    


    def get_cell(self, x, y):
        return self.grid[y % self.height][x % self.width]

    def set_cell(self, cell, x, y):
        self.grid[y % self.height][x % self.width] = cell

    
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
                
                # Fish
                if cell.is_fish():
                    cell.entity.update(
                        self,
                        cell,
                        self.get_surroundings(cell.x, cell.y)
                    )
