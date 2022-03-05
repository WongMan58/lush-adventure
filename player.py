import keyboard, time, os

from map import *

class Player():
    x = 0
    y = 0
    direction = "UP"
    costume = "@"

    def spawn(pos_x, pos_y):
        Map.generate()
        Player.x = pos_x
        Player.y = pos_y
        Map.replace(Player.x, Player.y, Player.costume)
    
    def move(change_x, change_y):
        Map.replace(Player.x, Player.y, Map.old_obj)
        if change_x != None:
            Player.y += change_x
            Map.replace(Player.x, Player.y, Player.costume)
        if change_y != None:
            Player.x -= change_y
            Map.replace(Player.x, Player.y, Player.costume)
        time.sleep(0.12)
    
    def checksides():
        up = False
        right = False
        down = False
        left = False

        stone = "█"

        if Player.x > 0:
            x_row_info = Map.map[Player.x - 1]
            if x_row_info[Player.y] != stone:
                up = True
        
        if Player.y < (Map.width - 1):
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y + 1] != stone:
                right = True

        if Player.x < (Map.height - 1):
            x_row_info = Map.map[Player.x + 1]
            if x_row_info[Player.y] != stone:
                down = True

        if Player.y > 0:
            x_row_info = Map.map[Player.x]
            if x_row_info[Player.y - 1] != stone:
                left = True

        return up, right, down, left
    
    def checkForKeyboardInput():
        can_go_up, can_go_right, can_go_down, can_go_left = Player.checksides()

        if keyboard.is_pressed("up") and can_go_up:
            Player.move(None, 1)
        if keyboard.is_pressed("right") and can_go_right:
            Player.move(1, None)
        if keyboard.is_pressed("down") and can_go_down:
            Player.move(None, -1)
        if keyboard.is_pressed("left") and can_go_left:
            Player.move(-1, None)