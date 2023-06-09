from tkinter import Button, Label
import random
import settings


class Cell:
    all = []  # Class Attribute
    cell_count_label_obj: Label = None
    cell_count = settings.GRID_SIZE**2

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object: Button = None
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

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location,
                    text=f"Cells Left: {Cell.cell_count}",
                    bg="black",
                    fg="white",
                    width=12,
                    height=4,
                    font=("", 12))
        Cell.cell_count_label_obj = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surround_cells_mine_len == 0:
                for cell_obj in self.surround_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def right_click_action(self, event):
        print(event)
        print("RIGHT CLICK!")

    def show_mine(self):
        # A Logic to do the Game Over
        self.cell_btn_object.configure(bg="red")

    def show_cell(self):
        print(self.get_cell_by_axis(self.x, self.y), end="")
        print(" = ", end="")
        print(self.surround_cells)
        print(self.surround_cells_mine_len)
        Cell.cell_count -=1
        self.cell_btn_object.configure(text=self.surround_cells_mine_len)
        if Cell.cell_count_label_obj:
            Cell.cell_count_label_obj.configure(text=f"Cells Left: {Cell.cell_count}")

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surround_cells(self):
        cells = [self.get_cell_by_axis(self.x - 1, self.y - 1),
                 self.get_cell_by_axis(self.x - 1, self.y),
                 self.get_cell_by_axis(self.x - 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y),
                 self.get_cell_by_axis(self.x + 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y + 1)]

        cells = [c for c in cells if c is not None]
        return cells

    @property
    def surround_cells_mine_len(self):
        count = 0
        for c in self.surround_cells:
            if c.is_mine:
                count += 1
        return count

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        print("picked_cells = ", end="")
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y},T)" if self.is_mine else f"Cell({self.x},{self.y})"
