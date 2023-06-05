
import random
import time
from tkinter import Canvas, Label, StringVar, Tk




window_width = 800
window_height = 600
cell_size = 20





def draw_square(x, y, color):
    delta = 2
    a = (int(x * cell_size + delta), int(y * cell_size + delta), int(x * cell_size + cell_size + delta), int(y * cell_size + cell_size + delta))
    canvas.create_rectangle(int(x * cell_size),
                            int(y * cell_size),
                            int(x * cell_size + cell_size),
                            int(y * cell_size + cell_size),
                            fill=color,
                            outline="")
    canvas.pack()

def draw_water(x, y):
    draw_square(x, y, "#116D6E")

def draw_shark(x, y):
    draw_square(x, y, "#CD1818")

def draw_fish(x, y):
    draw_square(x, y, "#08c73b")

def update_turn(current_turn):
    turn.set("Turns: " + str(current_turn))


# ====================================


tk = Tk()
tk.geometry("" + str(window_width) + "x" + str(window_height))

turn = StringVar()
label_turn = Label(tk, textvariable=turn, font=("Arial", 30))
label_turn.pack()

canvas = Canvas(tk, width=window_width, height=window_height, bg="#116D6E") # border=cell_size
canvas.pack()

# draw_shark(6, 10)
# draw_fish(1, 1)
draw_shark(0, 0)

# tk.after(2000, )



def loop():
    # draw_shark(random.randint(0, 30), random.randint(0, 30))
    tk.after(500, loop)








while True:
    tk.after(500, loop)
    tk.mainloop()

