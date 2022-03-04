import time, keyboard, os
from map import *
from inventory import *

global player_costume
global player_x # Current map column the player is in
global player_y # Current map row the player is in
global player_direction

class Player:
    global player_costume

    # Define what the player looks like
    player_costume = "@" 

    def spawn(x, y): # Create where the player will spawn when loading into the world
        global player_x
        global player_y

        Map.generate() # The spawn function automatically generates a map first

        player_x = x # Set player x position
        player_y = y # Set player y position
        x_row_info = list(Map.map[player_x]) # Get information about the row the player is in
        x_row_info[player_y] = player_costume
        x_row_info = ''.join(x_row_info)
        Map.map[player_x] = x_row_info

        os.system("cls||clear")
        Map.display()
    
    def checkAround(current_x, current_y): # x is vertical, y is horizontal
        # NOTE ORDER IS ALWAYS UP, RIGHT, DOWN AND THEN LEFT
        # TODO: Fix left collision problem and left and right world clipping
        up = False
        right = False
        down = False
        left = False
        orig_x = current_x
        orig_y = current_y

        if player_x > 0:
            x_row_info = Map.map[orig_x - 1]
            if x_row_info[orig_y] != "█":
                up = True
            else:
                up = False
        else:
            up = False
        
        if player_y < (Map.full_width - 1):
            x_row_info = Map.map[orig_x]
            if x_row_info[orig_y + 1] != "█":
                right = True
            else:
                right = False
        else:
            right = False
        
        if player_x < (Map.full_height - 1):
            x_row_info = Map.map[orig_x + 1]
            if x_row_info[orig_y] != "█":
                down = True
            else:
                down = False
        else:
            down = False
        
        if player_y > 0:
            x_row_info = Map.map[orig_x]
            if x_row_info[orig_y - 1] != "█":
                left = True
            else:
                left = False
        else:
            left = False

        return up, right, down, left

    def move(increase_x, increase_y):
        global player_x
        global player_y

        Map.reset()
        if increase_x != None:
            player_y += increase_x
        if increase_y != None:
            player_x -= increase_y
        
        row_info = list(Map.map[player_x])
        row_info[player_y] = player_costume
        row_info = ''.join(row_info)
        Map.map[player_x] = row_info

        os.system("cls||clear")
        Map.display()
        time.sleep(0.13) # TODO Use a different way to stop player from moving infinitly, this way is not efficient

    def checkInput():
        global player_direction
        up, right, down, left = Player.checkAround(player_x, player_y)

        # Check keyboard player movement
        if up != False:
            if keyboard.is_pressed("up") or keyboard.is_pressed("w"):
                Player.move(None, 1)
                player_direction = "up"
        if right != False:
            if keyboard.is_pressed("right") or keyboard.is_pressed("d"):
                Player.move(1, None)
                player_direction = "right"
        if down != False:
            if keyboard.is_pressed("down") or keyboard.is_pressed("s"):
                Player.move(None, -1)
                player_direction = "down"
        if left != False:
            if keyboard.is_pressed("left") or keyboard.is_pressed("a"):
                Player.move(-1, None)
                player_direction = "left"
        if keyboard.is_pressed('f'):
            Player.tryCollectItem(player_direction, player_x, player_y)
    
    def tryCollectItem(direction, current_x, current_y):
        orig_x = current_x
        orig_y = current_y
        if direction == "up":
            x_row_info = Map.map[orig_x - 1]
            if x_row_info[orig_y] == "F":
                Inventory.addItem("Regular Flower", 1)
        elif direction == "right":
            x_row_info = Map.map[orig_x]
            if x_row_info[orig_y + 1] == "F":
                Inventory.addItem("Regular Flower", 1)
        elif direction == "down":
            x_row_info = Map.map[orig_x + 1]
            if x_row_info[orig_y] == "F":
                Inventory.addItem("Regular Flower", 1)
        elif direction == "left":
            x_row_info = Map.map[orig_x]
            if x_row_info[orig_y - 1] == "F":
                Inventory.addItem("Regular Flower", 1)