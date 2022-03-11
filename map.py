import random, math, os

class Map():
    width = 72
    height = 29
    map = []
    code = []
    center_width = width / 2
    center_height = height / 2
    old_obj = ""
    to_generate = []
    flowers = ["D", "F"]

    if isinstance(center_width, float):
        center_width = math.ceil(center_width)
    if isinstance(center_height, float):
        center_height = math.ceil(center_height)

    def generate():
        for row in range(Map.height): # Variable row is not used
            single_row_code = [] # Used to store one line of code
            single_map_row = []
            for item in range(Map.width): # Variable item is not used
                current_tile = random.randrange(1, 500)
                if current_tile <= 420:
                    current_tile = "G"
                    single_row_code.append("2")
                elif current_tile > 420 and current_tile <= 475:
                    current_tile = "█"
                    single_row_code.append("3")
                elif current_tile > 475 and current_tile < 485: 
                    current_tile = "F"
                    single_row_code.append("4")
                elif current_tile >= 485:
                    current_tile = "D"
                    single_row_code.append("5")
                single_map_row.append(current_tile)
            single_map_row = ''.join(single_map_row) # Join entire row list together into one string
            single_row_code = ''.join(single_row_code) # Join all the numbers together into one string for one row of code
            Map.code.append(single_row_code)
            Map.map.append(single_map_row)
    
    def display():
        for row in Map.map:
            print(row)
    
    def update_map():
        costume_code = []
        for row in range(len(Map.code)):
            current_sector_info = list(Map.code[row])
            for item in range(len(current_sector_info)):
                if current_sector_info[item] == "1":
                    current_sector_info[item] = "@"
                elif current_sector_info[item] == "2":
                    current_sector_info[item] = "G"
                elif current_sector_info[item] == "3":
                    current_sector_info[item] = "█"
                elif current_sector_info[item] == "4":
                    current_sector_info[item] = "F"
                elif current_sector_info[item] == "5":
                    current_sector_info[item] = "D"
            costume_code.append(''.join(current_sector_info))
        Map.map.clear()
        for row in costume_code:
            Map.map.append(row)
        os.system('cls||clear')
        Map.display()
    
    def replaceObject(pos_x, pos_y, obj, store_old_obj):
        if obj == "@":
            obj = "1"
        elif obj == "G":
            obj = "2"
        elif obj == "█":
            obj = "3"
        elif obj == "F":
            obj = "4"
        elif obj == "D":
            obj = "5"
        code = list(Map.code[pos_x])
        if store_old_obj:
            Map.old_obj = code[pos_y]
        code[pos_y] = obj
        Map.code[pos_x] = ''.join(code)
        Map.update_map()
    
    def findObject(pos_x, pos_y):
        row = Map.map[pos_x]
        return row[pos_y]
    