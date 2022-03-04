from controls import *
from map import *
from inventory import *


running = False

spawn_x = Map.center_height
spawn_y = Map.center_width

Player.spawn(spawn_x, spawn_y)

running = True # TODO: Remove this when we have a title / menu screen

while running:
    checkKeyboardInput()
