from player import *
from map import *
from controls import *

spawn_x = Map.center_height
spawn_y = Map.center_width

Player.spawn(spawn_x, spawn_y)

while True:
    Map.findObject(1, 1)
    Controls.checkForUserKeyboardInput()