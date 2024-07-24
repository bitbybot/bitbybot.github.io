from turtle import *

class Box(Turtle):

    # this is done when a box class is created, sets coordinates 
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed("fastest")
        self.pu()
        self.ht()
        self.goto(x, y)
        self.pd()
        
    # draws the verticle and horizontal lines
    def draw(self):
        self.forward(300)
        self.setheading(270)
        self.forward(300)
        self.setheading(180)
        self.forward(300)
        self.setheading(90)
        self.forward(300)
        self.setheading(0)

        for i in range(1, 4):
            x = -150 + (i * 75)
            self.goto(x, 150)
            self.pd()
            self.goto(x, -150)
            self.pu()
            y = 150 + (i * -75)
            self.goto(-150, y)
            self.pd()
            self.goto(150, y)
            self.pu()