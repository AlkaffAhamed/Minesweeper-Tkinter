from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Setup Window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Tutorial")
root.resizable(False, False)

# Title Frame
top_frame = Frame(root,
                  bg="black",
                  width=settings.WIDTH,
                  height=utils.height_prct(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame,
                   bg="black",
                   fg="white",
                   text="Minesweeper Python",
                   font=("", 32))
game_title.place(x=utils.width_prct(25), y=15)

# Sidebar Frame
left_frame = Frame(root,
                   bg="black",
                   width=utils.width_prct(25),
                   height=utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

# Center Frame
center_frame = Frame(root,
                     bg="black",
                     width=utils.width_prct(75),
                     height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# Generate the cells
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        #c.cell_btn_object.grid(column=x, row=y)
        c.cell_btn_object.place(relx=x/settings.GRID_SIZE,
                                rely=y/settings.GRID_SIZE,
                                relwidth=1/settings.GRID_SIZE,
                                relheight=1/settings.GRID_SIZE)

Cell.randomize_mines()
print("Cell.all = ", end="")
print(Cell.all)

# Call the label from Cell() class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

# Run Window
root.mainloop()
