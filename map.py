import random, math, os

class Map:
    full_width = 48 # Used for generation
    full_height = 25 # Used for generation
    shown_width = 48 # NOTE: This is so far unused, this will be used when map scrolling is made
    shown_height = 16 # NOTE: This is so far unused, this will be used when map scrolling is made
    code = []
    center_width = full_width / 2
    center_height = full_height / 2
    
    # Declare the map list
    map = []

    # Round up center of map variables if they are floats
    if isinstance(center_width, float):
        center_width = math.ceil(center_width)
    if isinstance(center_height, float):
        center_height = math.ceil(center_height)
    
    def generate():
        for row in range(Map.full_height): # Variable row is not used
            single_row_code = [] # Used to store one line of code
            single_map_row = []
            for item in range(Map.full_width): # Variable item is not used
                current_tile = random.randrange(1, 200)
                if current_tile <= 170:
                    current_tile = "G"
                    single_row_code.append("1")
                elif current_tile > 170 and current_tile < 197:
                    current_tile = "█"
                    single_row_code.append("2")
                elif current_tile >= 197: 
                    current_tile = "F"
                    single_row_code.append("3")
                single_map_row.append(current_tile)
            single_map_row = ''.join(single_map_row) # Join entire row list together into one string
            single_row_code = ''.join(single_row_code) # Join all the numbers together into one string for one row of code
            Map.code.append(single_row_code)
            Map.map.append(single_map_row)

    def display():
        if len(Map.map) < 1:
            print("Please generate map first!")
            exit(1)
        for row in Map.map:
            print(row)
    
    
    def reset():
        costume_code = []
        for row in range(len(Map.map)):
            current_sector_info = list(Map.code[row])
            for item in range(len(current_sector_info)):
                if current_sector_info[item] == "1":
                    current_sector_info[item] = "G"
                elif current_sector_info[item] == "2":
                    current_sector_info[item] = "█"
                elif current_sector_info[item] == "3":
                    current_sector_info[item] = "F"
            current_sector_info  = ''.join(current_sector_info)
            costume_code.append(current_sector_info)
        Map.map.clear()
        for row in costume_code:
            Map.map.append(row)           

    def replaceObject(pos_x, pos_y, obj):
        # Turn object into number
        if obj == "G":
            obj = "1"
        elif obj == "█":
            obj = "2"
        elif obj == "F":
            obj = "3"
        current_row_of_code = list(Map.code[pos_x])
        current_row_of_code[pos_y] = obj
        Map.code[pos_x] = ''.join(current_row_of_code)
        Map.reset()
        os.system('cls||clear')
        Map.display()