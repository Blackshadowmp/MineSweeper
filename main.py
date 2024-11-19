from tkinter import *
from minesweeperGUI import Minesweeper

root = Tk()
root.title("Minesweeper Configuration")
root.geometry("600x400")
dimension = tuple()

def start_game():
    root.destroy()
    dimension=(size.get())
    game=Minesweeper(dimension, difficulty[difficulty_input_text.get()])

difficulty = {
    "easy": 0.1,
    "medium": 0.2,
    "hard": 0.4,
    "unfair": 0.6
}

difficulty_input_text = StringVar()
difficulty_input_text.set("medium")

difficulty_dropdown = OptionMenu(root, difficulty_input_text, *difficulty)

button = Button(root, text="Start Game", command=start_game)

size_label = Label(root, text="size")
size = IntVar()
size.set(10)
size_input = Entry(root, textvariable=size, font=("calibre", 10, "normal"))

difficulty_label = Label(root, text="Difficulty: ")

size_label.grid(row=1, column=1)
size_input.grid(row=1, column=2)
difficulty_label.grid(row=2, column=1)
difficulty_dropdown.grid(row=2, column=2)
button.grid(row=1, column=3)

root.mainloop()