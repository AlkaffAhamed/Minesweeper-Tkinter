from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(location,
                     text="TEXT")
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
