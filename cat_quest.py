#libraries go here



#class & function defs go here
def get_room(coords, level):
    global can_north
    global can_south
    global can_east
    global can_west
    global can_up
    global can_down
    global roomID
    if level == 1:
        if coords == [3, 4]:
            roomID = "bed"
            can_north = False
            can_south = False
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [2, 4]:
            roomID = "dungeon"
            can_north = True
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2, 5]:
            roomID = "bathroom"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2, 3]:
            roomID = "hallway1"
            can_north = True
            can_south = True
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2, 2]:
            roomID = "hallway2"
            can_north = True
            can_south = True
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [1, 2]:
            roomID = "closet"
            can_north = False
            can_south = False
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [0, 2]:
            roomID = "secret_chamber"
            can_north = False
            can_south = False
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2, 1]:
            roomID = "hallway3"
            can_north = True
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3, 1]:
            roomID = "armory"
            can_north = False
            can_south = False
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [2, 0]:
            roomID = "cat_tree1"
            can_north = False
            can_south = True
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [3, 0]:
            roomID = "shop1"
            can_north = False
            can_south = False
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [1, 0]:
            roomID = "stairs1"
            can_north = False
            can_south = False
            can_east = True
            can_west = False
            can_up = True
            can_down = False

    elif level == 2:
        if coords == [1,0]:
            roomID = "stairs2"
            can_north = False
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = True
        elif coords == [2,0]:
            roomID = "maze1"
            can_north = False
            can_south = True
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [3,0]:
            roomID = "maze3"
            can_north = False
            can_south = True
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [1,1]:
            roomID = "maze2"
            can_north = True
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2,1]:
            roomID = "owl_room1"
            can_north = True
            can_south = True
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [3,1]:
            roomID = "maze4"
            can_north = True
            can_south = True
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [4,1]:
            roomID = "trap_room"
            can_north = False
            can_south = True
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [1,2]:
            roomID = "maze5"
            can_north = True
            can_south = False
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2,2]:
            roomID = "maze6"
            can_north = True
            can_south = True
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [3,2]:
            roomID = "scratch_post"
            can_north = True
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [4,2]:
            roomID = "maze7"
            can_north = True
            can_south = True
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [2,3]:
            roomID = "maze8"
            can_north = True
            can_south = True
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,3]:
            roomID = "maze9"
            can_north = True
            can_south = True
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [4,3]:
            roomID = "maze"
            can_north = True
            can_south = True
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [1,4]:
            roomID = "shop2"
            can_north = False
            can_south = False
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [2,4]:
            roomID = "cat_tree2"
            can_north = True
            can_south = False
            can_east = True
            can_west = True
            can_up = False
            can_down = False
        elif coords == [3,4]:
            roomID = "key_room1"
            can_north = True
            can_south = False
            can_east = False
            can_west = True
            can_up = False
            can_down = False
        elif coords == [4,4]:
            roomID = "cactus_room1"
            can_north = True
            can_south = True
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3, 5]:
            roomID = "stairs3"
            can_north = False
            can_south = False
            can_east = True
            can_west = False
            can_up = True
            can_down = False
        elif coords == [4, 5]:
            roomID = "cactus2"
            can_north = True
            can_south = False
            can_east = False
            can_west = True
            can_up = False
            can_down = False

    elif level == 3:
        if coords == [3,5]:
            roomID = "stairs4"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = True
        elif coords == [3,4]:
            roomID = "owl_room2"
            can_north = True
            can_south = True
            can_east = True
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,3]:
            roomID = "trial1"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,2]:
            roomID = "trial2"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,1]:
            roomID = "trial3"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,0]:
            roomID = "boss"
            can_north = True
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [3,-1]:
            roomID = "food"
            can_north = False
            can_south = False
            can_east = False
            can_west = False
            can_up = False
            can_down = False
        elif coords == [4,4]:
            roomID = "shop3"
            can_north = False
            can_south = False
            can_east = False
            can_west = True

def look():
    global roomID
    if roomID == "bed":
        print("It's your bedroom. Cat bed, water dish, toy mouse.")
    elif roomID == "dungeon":
        print("It's the dungeon outside your bedroom.")
    elif roomID == "bathroom":
        print("Just the bathroom.")
    elif roomID == "hallway1":
        print("The hallway leading out of the dungeon. Suits of armor line the walls.")
    elif roomID == "hallway2":
        print("The middle of the long hallway in CAT CASTLE.")
    elif roomID == "closet":
        print("It's a closet. It's just full of cleaning supplies but something about it seems fishy.")
    elif roomID == "secret_chamber":
        print("Of course there was a secret chamber behind the closet.")
    elif roomID == "hallway3":
        print("The north end of the long hallway in CAT CASTLE. There's a big spooky cat banner on the wall.")
    elif roomID == "armory":
        print("It's the armory! Big piles of swords and armor everywhere. Rad.")
    elif roomID == "cat_tree1":
        print("It's the castle cat tree! Seems like a good place to take a nap.")
    elif roomID == "shop1":
        print("It's the shop. Why does CAT CASTLE have a shop?")
    elif roomID == "stairs1":
        print("The stairs leading up to the LABYRINTH OF MISERY.")
    #second floor
    elif roomID == "stairs2":
        print("These stairs lead back down to CAT CASTLE")
    elif roomID == "maze":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze1":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze2":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze3":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze4":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze5":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze6":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze7":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze8":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "maze9":
        print("It's the labyrinth of misery. It feels endless.")
    elif roomID == "owl_room1":
        print("There's a giant owl here. It looks like it has a lot to say.")
    elif roomID == "trap_room":
        print("This room looks really suspicious.")
    elif roomID == "scratch_post":
        print("There's a giant scratching post here. It looks so inviting.")
    elif roomID == "shop2":
        print("There's a shop here. Why is there a shop in the LABYRINTH OF MISERY?")
    elif roomID == "cat_tree2":
        print("There's another cat tree here. Looks comfy, if a little damp.")
    elif roomID == "key_room":
        print("There's a big chest here.")
    elif roomID == "cactus_room1":
        print("This room is full of cacti. They look dangerous.")
    elif roomID == "cactus2":
        print("More cacti here.")
    elif roomID == "stairs3":
        print("These stairs lead to HELL KITCHEN, where your food bowl awaits.")
    #third floor
    elif roomID == "stairs4":
        print("These stairs lead down to the LABYRINTH OF MISERY. blegh")
    elif roomID == "owl_room2":
        print("There's another giant owl here.")
    elif roomID == "shop3":
        print("It's another shop. Why is there a shop in HELL KITCHEN?")
    elif roomID == "trial1":
        print("There's a sphinx here. It looks hungry.")
    elif roomID == "trial2":
        print("There's a bunch of bones lying around.")
    elif roomID == "trial3":
        print("There's some other kind of trial here (lol)")
    elif roomID == "boss":
        print("There's a human here ready to do battle.")
    elif roomID == "food":
        print("It's your dinner! You win!")
   

#start up scripts go here, e.g. title graphic, game_state = "new_game"
game_state = "playing"
player_coords = [3, 4]
level = 1
roomID = ""
can_north = False
can_south = False
can_east = False
can_west = False
can_up = False
can_down = False
get_room(player_coords, level)

# while loops go here
while game_state == "playing":
    doing = input(":")

    if doing == "north" or doing == "n":
        if can_north == True:
            player_coords[1] -= 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "south" or doing == "s":
        if can_south == True:
            player_coords[1] += 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "west" or doing == "w":
        if can_west == True:
            player_coords[0] -= 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "east" or doing == "e":
        if can_east == True:
            player_coords[0] += 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")
    
    elif doing == "up" or doing == "u":
        if can_up == True:
            level += 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")
    
    elif doing == "down" or doing == "d":
        if can_down == True:
            level -= 1
            get_room(player_coords, level)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")