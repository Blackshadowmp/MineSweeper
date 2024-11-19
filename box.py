class Box:
    def __init__(self, xcord, ycord):
        self.number_of_nearby_mines=0
        self.is_mine=False
        self.is_revealed=False
        self.has_flag=False
        self.cord=(xcord, ycord)
    def print(self):
        if self.is_revealed and not self.is_mine:
            return self.number_of_nearby_mines
        return "X"
    def reveal_box_on_click(self):
        self.is_revealed=True
        if self.is_mine:
            return False
        return True