
from tkinter import Canvas, Label, StringVar, Tk




window_width = 800
window_height = 600
cell_size = 8





def draw_square(x, y, size, color):
    delta = cell_size / 2
    canvas.create_rectangle(x + delta,
                            y + delta,
                            x + size + delta,
                            y + size + delta,
                            fill=color,
                            outline=""
    )

def draw_water(x, y):
    draw_square(x * cell_size, y * cell_size, cell_size, "#116D6E")

def draw_shark(x, y):
    draw_square(x * cell_size, y * cell_size, cell_size, "#CD1818")

def draw_fish(x, y):
    draw_square(x * cell_size, y * cell_size, cell_size, "#08c73b")

def update_turn(current_turn):
    turn.set("Turns: " + str(current_turn))




tk = Tk()
tk.geometry("" + str(window_width) + "x" + str(window_height))

turn = StringVar()
label_turn = Label(tk, textvariable=turn, font=("Arial", 30))
label_turn.pack()

canvas = Canvas(tk, width=window_width, height=window_height, bg="#116D6E") # border=self.cell_size
canvas.pack()

draw_shark(6, 10)
draw_fish(1, 1)
draw_shark(0, 0)

# canvas.update()
canvas.mainloop()



