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
        print("WIP")
    
    def checkForKeyboardInput():
        if keyboard.is_pressed("up"):
            Player.move(None, 1)
        if keyboard.is_pressed("right"):
            Player.move(1, None)
        if keyboard.is_pressed("down"):
            Player.move(None, -1)
        if keyboard.is_pressed("left"):
            Player.move(-1, None)