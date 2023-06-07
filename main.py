from tkinter import *

root = Tk()

# Setup Window
root.configure(bg="black")
root.geometry("720x360")
root.title("Minesweeper Tutorial")
root.resizable(False, False)

# Title Frame
top_frame = Frame(root,
                  bg="red",
                  width=720,
                  height=90)
top_frame.place(x=0, y=0)

# Sidebar Frame
left_frame = Frame(root,
                   bg="red",
                   width=720,
                   height=90)
left_frame.place(x=0, y=90)

# Run Window
root.mainloop()
