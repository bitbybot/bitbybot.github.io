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
box = Box(-150, 150)
box.draw()
tiles = []
c_index = 0
turn = 1
player_sequence = []
canClick = False

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
    global canClick
    if canClick:
        for tile in tiles:
            if tile.clicked(x, y) and tile.index not in player_sequence:
                player_sequence.append(tile.index)
                tile.draw()

### resets the colour of all the tiles on the screen ###
def clearTiles():
    for tile in tiles:
        tile.clear()

### checks if the player's sequence is equal to the actaul sequence ###
def matching():
    for i in range(len(player_sequence)):
        if player_sequence[i] != sequence[i]:
            return False
    return True

# makes the screen listen for when the player clicks the screen
screen.onclick(clicks)
screen.listen()

### this while loop will be the part where we continuously ask for the player's guess at the sequence ### 
while True:
    clearTiles()
    canClick = False
    time.sleep(0.5)

    for index in sequence[:turn]:
        tiles[index].draw()
        time.sleep(0.5)

    clearTiles()

    canClick = True

    player_sequence = []

    while len(player_sequence) < turn and matching():
        screen.update()  # Update the screen to allow for events to be processed
        pass

    time.sleep(0.5)
    clearTiles()

    if matching():
        if turn == 16:
            break  # Exit the loop if the player has memorized all 16 tiles
        turn += 1
    else:
        break

# clears the box from the screen and resets the pen to draw
clearTiles()
canClick = False
box.clear()
pu()
goto(0, 0)

### checks if the player won the game or lost and displays the corresponding message ###
if turn == 16:
    write("You Win!", align="center", font=("Ariel", 50))
else:
    write("Game Over", align="center", font=("Ariel", 50))

# writes the amount of tiles the player was able to memorize
goto(0, -50)
write("Tiles Memorized: " + str(len(player_sequence)), align="center", font=("Ariel", 30))
ht()
screen.mainloop() 