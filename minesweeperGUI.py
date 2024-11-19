from tkinter import *
from table import Table

class Minesweeper:  
    def __init__(self, dimension, difficulty):
        self.main = Tk()
        self.dimension=dimension

        self.colors={
            '0':"white",
            '1':"blue2",
            '2':"green2",
            '3':"red",
            '4':"RoyalBlue4",
            '5':"brown4",
            '6':"cadet blue",
            '7':"purple",
            '8':"black",
            }
        
        self.main.title("Minesweeper")
        self.main.geometry("500x500")

        self.main_grid = Table(difficulty, self.dimension)
        self.main_grid_buttons = self.set_grid_buttons()
        self.main_grid_button_labels = self.set_grid_button_labels()

        self.set_display()
        self.main.mainloop()

    def set_grid_buttons(self):
        grid_to_return = []                
        for _ in range (self.dimension):
            row = []
            for _ in range (self.dimension): 
                row.append(None)
            grid_to_return.append(row)
        return grid_to_return
    
    def set_grid_button_labels(self):
        grid_to_return = []                
        for _ in range (self.dimension):
            row = []
            for _ in range (self.dimension): 
                row.append(StringVar())
            grid_to_return.append(row)
        return grid_to_return
    
    def update_game(self):
        size=self.main_grid.dimension
        for x in range(size):
            for y in range(size):
                if self.main_grid.grid[x][y].is_revealed:
                    if not self.main_grid.grid[x][y].is_mine:
                        self.main_grid_button_labels[x][y].set(self.main_grid.grid[x][y].number_of_nearby_mines)
                        self.main_grid_buttons[x][y].config(fg=self.colors[self.main_grid_button_labels[x][y].get()])
                    else:
                        self.main_grid_button_labels[x][y].set("🔴")

    def set_display(self):
        size=self.main_grid.dimension
        for x in range(size):
            self.main.grid_rowconfigure(x, weight=1)
            for y in range(size):
                self.main.grid_columnconfigure(y, weight=1)
                self.main_grid_buttons[x][y] = Button(
                    self.main,
                    fg='white',
                    bg="gray",
                    state=NORMAL,
                    textvariable=self.main_grid_button_labels[x][y], 
                    command=lambda x=x, y=y: self.clicked(x, y)
                )
                self.main_grid_buttons[x][y].bind(
                "<Button-3>", lambda event, x=x, y=y: self.right_clicked(x, y)
                )
                self.main_grid_buttons[x][y].grid(row=x, column=y, sticky="nsew")
        self.update_game()

    def clicked(self, x, y):
        if not self.main_grid.grid[x][y].is_mine:
            self.main_grid.chain_reveal(cord=(x, y))
        else:
            self.main_grid.reveal_all()
            self.disable_all() 
        self.update_game()

    def right_clicked(self, x, y):
        if self.main_grid_buttons[x][y]['state']==NORMAL:
            current_text = self.main_grid_button_labels[x][y].get()
            if current_text == "🚩":
                self.main_grid_button_labels[x][y].set("")
            else:
                self.main_grid_button_labels[x][y].set("🚩")

    def disable_all(self):
        for row in self.main_grid_buttons:
            for button in row:
                button.config(state=DISABLED)
                button.config(bg=self.colors['3'])