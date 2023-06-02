from tkinter import *


class GuiTkinter(Tk):


    def __init__(self, window_width, window_height, cell_size):
        super().__init__
        self.cell_size = cell_size
        self.geometry("" + str(window_width) + "x" + str(window_height))
        self.turn = StringVar()
        self.label_turn = Label(self.window, textvariable=self.turn, font=("Arial", 30))
        self.label_turn.pack()
        self.canvas = Canvas(self.window, width=window_width, height=window_height, bg="#116D6E") # border=self.cell_size
        self.canvas.pack()



    def draw_square(self, x, y, color):
        delta = self.cell_size / 2
        self.canvas.create_rectangle(
            x + delta,
            y + delta,
            x + self.cell_size + delta,
            y + self.cell_size + delta,
            fill=color,
            outline="")

    def draw_water(self, x, y):
        self.draw_square(x, y, "#116D6E")

    def draw_shark(self, x, y):
        self.draw_square(x, y, "#CD1818")

    def draw_fish(self, x, y):
        self.draw_square(x, y, "#08c73b")



    def update_turn(self, current_turn):
        self.turn.set("Turns: " + str(current_turn))
        