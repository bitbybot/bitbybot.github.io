from turtle import *

class Tile(Turtle):

    # this is done when a tile class is created, sets coordinates, size, colour, and index of the tile
    def __init__(self, c, x, y, size, c_index):
        super().__init__()
        self.c = c
        self.x = x
        self.y = y
        self.size = size
        self.index = c_index
        self.speed("fastest")
        self.ht()
        self.pu()
        self.goto(x, y)
        self.pd()
        self.color(c)

    # move turtle to the tile and fills in with the colour associated with the index
    def draw(self):
        self.pu()
        self.goto(self.x, self.y)
        self.pd()
        self.begin_fill()
        self.setheading(0)
        self.forward(self.size)
        self.setheading(270)
        self.forward(self.size)
        self.setheading(180)
        self.forward(self.size)
        self.setheading(90)
        self.forward(self.size)
        self.end_fill()

    # determines that this tile was clicked based on the location of the player's mouse click
    def clicked(self, x, y):
        if abs(x - (self.x + (self.size / 2))) < self.size / 2 and abs((self.y - (self.size / 2)) - y) < self.size / 2:
            return True
        return False