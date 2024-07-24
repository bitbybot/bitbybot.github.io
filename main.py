# import libraries 
from turtle import *
from box import *
from tile import *
from random import *
import time

# create screan and set colour mode to rgb
screen = Screen()
screen.colormode(255)  

# grid colour stored in list
colors = [
    (255, 0, 0), (201, 46, 40), (153, 65, 61), (173, 114, 111),
    (255, 230, 0), (219, 202, 44), (191, 180, 78), (230, 224, 172),
    (10, 87, 6), (29, 201, 20), (55, 230, 46), (151, 255, 145),
    (21, 108, 158), (60, 168, 230), (115, 204, 255), (153, 210, 242)
]

### Define varibles ###


# get the coordinates for each tile and create a tile object for each of the 16 squares 
for row in range(4):
    for col in range(4):
        c = colors[c_index]
        x = -150 + (col * 75)
        y = 150 - (row * 75)
        t = Tile(c, x, y, 75, c_index)
        c_index += 1
        tiles.append(t)

# this creates a list called sequence with the numbers 0-15 in any order
sequence = [num for num in range(16)]
for i in range(len(sequence) - 1, 0, -1):
    r = randint(0, i)
    sequence[r], sequence[i] = sequence[i], sequence[r]

### if the user is allowed to click, then add their next click to the player's sequence ###
def clicks(x, y):


### resets the colour of all the tiles on the screen ###
def clearTiles():


### checks if the player's sequence is equal to the actaul sequence ###
def matching():


# makes the screen listen for when the player clicks the screen
screen.onclick(clicks)
screen.listen()

### this while loop will be the part where we continuously ask for the player's guess at the sequence ### 
while True:
    

# clears the box from the screen and resets the pen to draw
clearTiles()
canClick = False
box.clear()
pu()
goto(0, 0)

### checks if the player won the game or lost and displays the corresponding message ###

# writes the amount of tiles the player was able to memorize
goto(0, -50)
write("Tiles Memorized: " + str(len(player_sequence)), align="center", font=("Ariel", 30))
ht()
screen.mainloop() 