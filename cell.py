from tkinter import Button
import random
import settings


class Cell:
    all = []  # Class Attribute

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)  # Append to the Class Attribute

    def create_btn_object(self, location):
        btn = Button(location,
                     width=6,
                     height=2)
        # Binding the events
        btn.bind("<Button-1>", self.left_click_action)  # Left Click
        btn.bind("<Button-3>", self.right_click_action)  # Right Click
        self.cell_btn_object = btn

    def left_click_action(self, event):
        print(event)
        print("LEFT CLICK!")

    def right_click_action(self, event):
        print(event)
        print("RIGHT CLICK!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        print("picked_cells = ", end="")
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
