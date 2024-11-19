from box import Box
import math
import random
class Table:

    def __init__(self, difficulty, dimension):
        self.dimension=dimension
        self.grid=self.set_grid()
        self.number_of_mines=int(math.floor(difficulty*self.dimension*self.dimension))
        
        self.set_random_mines()
        self.set_nearby_mine_count()
        self.start_grid_revealed()

    def set_grid(self):
        grid_to_return = []                
        for i in range (self.dimension):
            row = []
            for j in range (self.dimension): 
                box_to_add=Box(i, j)
                row.append(box_to_add)
            grid_to_return.append(row)
        return grid_to_return

    def get_random_cords_exclusive(self):
        exclusive_cords=set()
        while len(exclusive_cords) != self.number_of_mines:
            randomized_cord=(random.randint(0,self.dimension-1), random.randint(0, self.dimension-1))
            if randomized_cord not in exclusive_cords:
                exclusive_cords.add(randomized_cord)
        return exclusive_cords
    
    def start_grid_revealed(self):
        starting_box=self.get_no_nearby_box_random()
        if starting_box:
            self.chain_reveal(starting_box.cord)
        else:
            starting_box=self.get_random_not_mine()
            self.grid[starting_box.cord[0]][starting_box.cord[1]].is_revealed=True

    def print_mines(self):
        for row in self.grid:
            for box in row:
                if box.is_mine:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()
    def get_no_nearby_box_random(self):
        no_nearby_cords = set()
        for row in self.grid:
            for box in row:
                if box.number_of_nearby_mines == 0 and not box.is_mine:
                    no_nearby_cords.add(box.cord)                
        if len(no_nearby_cords) != 0:
            no_nearby_cords = list(no_nearby_cords)
            random_index = random.randint(0, len(no_nearby_cords) - 1)
            random_box_xcord, random_box_ycord = no_nearby_cords[random_index]
            return self.grid[random_box_xcord][random_box_ycord]
        return None
    
    def get_random_not_mine(self):
        for row in self.grid:
            for box in row:
                if not box.is_mine:
                    return box
                
    def set_random_mines(self):
        mine_cords=self.get_random_cords_exclusive()
        for cord in mine_cords:
            self.grid[cord[0]][cord[1]].is_mine=True

    def get_nearby_mines(self, cord=tuple()):
        number_of_nearby_mines = 0
        x, y = cord
        neighbors = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1), (1, 0), (1, 1)]
        for i, j in neighbors:
            new_x, new_y = x + i, y + j
            if 0 <= new_x < self.dimension and 0 <= new_y < self.dimension and self.grid[new_x][new_y].is_mine:
                number_of_nearby_mines += 1
        
        return number_of_nearby_mines


    def set_nearby_mine_count(self):
        for row in self.grid:
            for box in row:
                box.number_of_nearby_mines=self.get_nearby_mines(box.cord)

    def print_grid(self):
        for row in self.grid:
            for box in row:
                print(box.print(), end=" ")
            print()

    def chain_reveal(self, cord=tuple()):
        x, y = cord
        if 0 <= x < self.dimension and 0 <= y < self.dimension and not self.grid[x][y].is_revealed and not self.grid[x][y].is_mine:
            self.grid[x][y].is_revealed = True
            if self.grid[x][y].number_of_nearby_mines == 0:
                neighbors = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),          (0, 1),
                            (1, -1), (1, 0), (1, 1)]
                for dx, dy in neighbors:
                    self.chain_reveal(cord=(x + dx, y + dy))

    
    def on_click_chain_reveal(self, cord=tuple()):
        if self.grid[cord[0]][cord[1]].is_mine:
            self.grid[cord[0]][cord[1]].is_revealed=True
            return False
        self.chain_reveal(cord=cord)
        return True
    
    def reveal_all(self):
        for row in self.grid:
            for box in row:
                box.is_revealed=True    