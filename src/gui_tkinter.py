from tkinter import *


class GuiTkinter():

    def __init__(self, window_width, window_height, cell_size, window_offset):
        # super().__init__
        self.cell_size = cell_size
        window_offset_string = ""
        if window_offset >= 0:
            window_offset_string += "+"
        window_offset_string += str(window_offset)



        self.window = Tk()
        self.window.geometry("" + str(window_width) + "x" + str(window_height) + window_offset_string + "+0")
        
        self.turn = StringVar()
        self.label_turn = Label(self.window, textvariable=self.turn, font=("Arial", 30))
        self.label_turn.pack()

        self.canvas = Canvas(self.window, width=window_width, height=window_height, bg="#202040") # border=self.cell_size
        self.canvas.pack()



    def draw_square(self, x, y, color):
        delta = 2
        a = (int(x * self.cell_size + delta), int(y * self.cell_size + delta), int(x * self.cell_size + self.cell_size + delta), int(y * self.cell_size + self.cell_size + delta))
        self.canvas.create_rectangle(int(x * self.cell_size),
                                int(y * self.cell_size),
                                int(x * self.cell_size + self.cell_size),
                                int(y * self.cell_size + self.cell_size),
                                fill=color,
                                outline="")

    def draw_water(self, x, y):
        # self.draw_square(x, y, "#202040")
        pass

    def draw_shark(self, x, y):
        self.draw_square(x, y, "#CD1818")

    def draw_fish(self, x, y):
        self.draw_square(x, y, "#fcda17")

    def update_turn(self, current_turn):
        self.turn.set("Turns: " + str(current_turn))
        