from entity import Shark as Shark
from entity import Fish as Fish
from entity import Entity as Entity



class GameGrid():

    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for j in range(width)] for i in range(height)]
    

    def draw_console(self):
        print("-" * (self.width+2))

        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                value = self.grid[y][x]
                if value == 0:
                    line += ' '
                elif isinstance(value, Entity):
                    line += value.draw()
            line += "|"
            print(line)
        print("-" * (self.width+2))
            
