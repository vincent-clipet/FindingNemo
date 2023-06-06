import pygame

class GuiPygame():

    COLOR_SHARK = (205, 24, 24)
    COLOR_FISH = (252, 218, 23)
    COLOR_WATER = (32, 32, 64)


    def __init__(self, window_width, window_height, cell_size):
        pygame.init()
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Wa-Tor")
        


    def draw_square(self, x, y, color):
        delta = 2
        pygame.draw.rect(self.screen,
                         color,
                         pygame.Rect(x * self.cell_size,
                                     y * self.cell_size,
                                     self.cell_size,
                                     self.cell_size)
        )

    def draw_water(self, x, y):
        # self.draw_square(x, y, self.COLOR_WATER)
        pass

    def draw_shark(self, x, y):
        self.draw_square(x, y, self.COLOR_SHARK)

    def draw_fish(self, x, y):
        self.draw_square(x, y, self.COLOR_FISH)

    def update_turn(self, current_turn):
        self.turn.set("Turns: " + str(current_turn))
        