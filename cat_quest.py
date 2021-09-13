#libraries go here



#class & function defs go here

class Item:
    def __init__(self, id, value,):
        self.id = id
        self.value = value
    def __repr__(self):
        return self.id
    
    def heal(self, amount):
        global HP
        global HP_max
        HP += amount
        if HP > HP_max:
            HP = HP_max
            print("Full health!")
        else:
            print ("Healed {} HP".format(amount))
    
    

class Weapon(Item):
    def __init__(self, id, value, bonus):
        super().__init__(id, value)
        self.bonus = bonus

    def equip_weapon(self, weapon):
        global equip
        global ATK_bonus
        if not equip["Weapon"] == None:
            inventory.append(equip["Weapon"])
        equip["Weapon"] = weapon
        inventory.remove(weapon)
        ATK_bonus = weapon.bonus
        print("{} equipped! (+{})".format(weapon.id, weapon.bonus))

class Armor(Item):
    def __init__(self, id, value, bonus):
        super().__init__(id, value)
        self.bonus = bonus

    def equip_armor(self, armor):
        global equip
        if not equip["Armor"] == None:
            inventory.append(equip["Armor"])
        equip["Armor"] = armor
        inventory.remove(armor)
        print("{} equipped! (+{})".format(armor.id, armor.bonus))

class Accessory(Item):
    def __init__(self, id, value):
        super().__init__(id, value)

class Room:
    def __init__(self, roomID, can_north, can_south, can_east, can_west, can_up=False, can_down=False, items=[], visited = False):
        self.roomID = roomID
        self.items = items
        self.can_north = can_north
        self.can_south = can_south
        self.can_east = can_east
        self.can_west = can_west
        self.can_up = can_up
        self.can_down = can_down
        self.visited = False
    def __repr__(self, roomID):
        return self.roomID

def get_room(coords, floor):
    global current_room
    if floor == 1:
        if coords == [3, 4]:
            current_room = bed

        elif coords == [2, 4]:
            current_room = dungeon

        elif coords == [2, 5]:
            current_room = bathroom

        elif coords == [2, 3]:
            current_room = hallway1
            
        elif coords == [2, 2]:
            current_room = hallway2
            
        elif coords == [1, 2]:
            current_room = closet
            
        elif coords == [0, 2]:
            current_room = secret_chamber
            
        elif coords == [2, 1]:
            current_room = hallway3
            
        elif coords == [3, 1]:
            current_room = armory
            
        elif coords == [2, 0]:
            current_room = cat_tree1
            
        elif coords == [3, 0]:
            current_room = shop1
            
        elif coords == [1, 0]:
            current_room = stairs1

    elif floor == 2:
        if coords == [1,0]:
            current_room = stairs2

        elif coords == [2,0]:
            current_room = maze1
            
        elif coords == [3,0]:
            current_room = maze3
            
        elif coords == [1,1]:
            current_room = maze2
            
        elif coords == [2,1]:
            current_room = owl_room1
            
        elif coords == [3,1]:
            current_room = maze4
            
        elif coords == [4,1]:
            current_room = trap_room
            
        elif coords == [1,2]:
            current_room = maze5
            
        elif coords == [2,2]:
            current_room = maze6
            
        elif coords == [3,2]:
            current_room = scratch_post
            
        elif coords == [4,2]:
            current_room = maze7
            
        elif coords == [2,3]:
            current_room = maze8
            
        elif coords == [3,3]:
            current_room = maze9
            
        elif coords == [4,3]:
            current_room = maze
            
        elif coords == [1,4]:
            current_room = shop2
            
        elif coords == [2,4]:
            current_room = cat_tree2
            
        elif coords == [3,4]:
            current_room = key_room1
            
        elif coords == [4,4]:
            current_room = cactus_room1
            
        elif coords == [3, 5]:
            current_room = stairs3
            
        elif coords == [4, 5]:
            current_room = cactus2

    elif floor == 3:
        if coords == [3,5]:
            current_room = stairs4
            
        elif coords == [3,4]:
            current_room = owl_room2
            
        elif coords == [3,3]:
            current_room = trial1
            
        elif coords == [3,2]:
            current_room = trial2
            
        elif coords == [3,1]:
            current_room = trial3

        elif coords == [3,0]:
            current_room = boss
            
        elif coords == [3,-1]:
            current_room = food
            
        elif coords == [4,4]:
            current_room = shop3

def look():
    global roomID
    global room_item
    if current_room.roomID == "bed":
        print("It's your bedroom. Cat bed, water dish, toy mouse.")
    elif current_room.roomID == "dungeon":
        print("It's the dungeon outside your bedroom.")
    elif current_room.roomID == "bathroom":
        print("Just the bathroom.")
    elif current_room.roomID == "hallway1":
        print("The hallway leading out of the dungeon. Suits of armor line the walls.")
    elif current_room.roomID == "hallway2":
        print("The middle of the long hallway in CAT CASTLE.")
    elif current_room.roomID == "closet":
        print("It's a closet. It's just full of cleaning supplies but something about it seems fishy.")
    elif current_room.roomID == "secret_chamber":
        print("Of course there was a secret chamber behind the closet.")
    elif current_room.roomID == "hallway3":
        print("The north end of the long hallway in CAT CASTLE. There's a big spooky cat banner on the wall.")
    elif current_room.roomID == "armory":
        print("It's the armory! Big piles of swords and armor everywhere. Rad.")
    elif current_room.roomID == "cat_tree1":
        print("It's the castle cat tree! Seems like a good place to take a nap.")
    elif current_room.roomID == "shop1":
        print("It's the shop. Why does CAT CASTLE have a shop?")
    elif current_room.roomID == "stairs1":
        print("The stairs leading up to the LABYRINTH OF MISERY.")
    #second floor
    elif current_room.roomID == "stairs2":
        print("These stairs lead back down to CAT CASTLE")
    elif current_room.roomID == "maze":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze1":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze2":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze3":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze4":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze5":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze6":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze7":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze8":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "maze9":
        print("It's the labyrinth of misery. It feels endless.")
    elif current_room.roomID == "owl_room1":
        print("There's a giant owl here. It looks like it has a lot to say.")
    elif current_room.roomID == "trap_room":
        print("This room looks really suspicious.")
    elif current_room.roomID == "scratch_post":
        print("There's a giant scratching post here. It looks so inviting.")
    elif current_room.roomID == "shop2":
        print("There's a shop here. Why is there a shop in the LABYRINTH OF MISERY?")
    elif current_room.roomID == "cat_tree2":
        print("There's another cat tree here. Looks comfy, if a little damp.")
    elif current_room.roomID == "key_room":
        print("There's a big chest here.")
    elif current_room.roomID == "cactus_room1":
        print("This room is full of cacti. They look dangerous.")
    elif current_room.roomID == "cactus2":
        print("More cacti here.")
    elif current_room.roomID == "stairs3":
        print("These stairs lead to HELL KITCHEN, where your food bowl awaits.")
    #third floor
    elif current_room.roomID == "stairs4":
        print("These stairs lead down to the LABYRINTH OF MISERY. blegh")
    elif current_room.roomID == "owl_room2":
        print("There's another giant owl here.")
    elif current_room.roomID == "shop3":
        print("It's another shop. Why is there a shop in HELL KITCHEN?")
    elif current_room.roomID == "trial1":
        print("There's a sphinx here. It looks hungry.")
    elif current_room.roomID == "trial2":
        print("There's a bunch of bones lying around.")
    elif current_room.roomID == "trial3":
        print("There's some other kind of trial here (lol)")
    elif current_room.roomID == "boss":
        print("There's a human here ready to do battle.")
    elif current_room.roomID == "food":
        print("It's your dinner! You win!")
    #say what items are here
    if len(current_room.items) != 0:
        print("Items: {}".format(current_room.items))
    #tell players where they can go
    dir = ""
    if current_room.can_north:
        dir += " N"
    if current_room.can_south:
        dir += " S"
    if current_room.can_east:
        dir += " E"
    if current_room.can_west:
        dir += " W"
    if current_room.can_up:
        dir += " U"
    if current_room.can_down:
        dir += " D"
    print("You can go:" + dir)
    
def get_item(id):
    global inventory
    if not id in str(current_room.items):
        print("There's no {} here.".format(id))
    else:
        #items
        if id == "potion":
            inventory.append(potion)
            current_room.items.remove(potion)
        #weapons
        elif id == "sword":
            inventory.append(sword)
            current_room.items.remove(sword)
        #armors
        elif id == "cat_armor":
            inventory.append(cat_armor)
            current_room.items.remove(cat_armor)
        
        print("got {}!".format(id))

def use_item(id):
    global inventory
    if not id in str(inventory):
        print("You don't have {}".format(id))
    else:
        #items
        if id == "potion":
            potion.heal(10)
            inventory.remove(potion)

        #weapons
        elif id == "sword":
            sword.equip_weapon(sword)
            
        elif id == "stick":
            stick.equip_weapon(stick)
        
        #armors
        elif id == "cat_armor":
            cat_armor.equip_armor(cat_armor)

            



#item objects go here
potion = Item("potion", 50)
#weapons
sword = Weapon("sword", 100, 5)
stick = Weapon("stick", 5, 1)
#armor
cat_armor = Armor("cat_armor", 150, 5)
#accessories

# Room objects go here: (roomID, north, south, east, west, up, down, items)
#floor 1
bed = Room("bed", False, False, False, True, False, False, [potion])
dungeon = Room("dungeon", True, True, True, False, False, False)
bathroom = Room("bathroom", True, False, False, False, items=[cat_armor])
hallway1 = Room("hallway1", True, True, False, False, False, False)
hallway2 = Room("hallway2", True, True, False, False, False, False)
closet = Room("closet", False, False, True, True, False, False)
secret_chamber = Room("secret_chamber", False, False, True, False, False, False)
hallway3 = Room("hallway3", True, True, True, False, False, False)
armory = Room("armory", False, False, False, True, False, False, [sword])
cat_tree1 = Room("cat_tree1", False, True, True, True, False, False)
shop1 = Room("shop1", False, False, False, True, False, False)
stairs1 = Room("stairs1", False, False, True, False, True, False)

#floor2
stairs2 = Room("stairs2", False, True, True, False, False, True)
maze1 = Room("maze1", False, True, True, True)
maze3 = Room("maze3", False, True, False, True)
maze2 = Room("maze2", True, True, True, False)
owl_room1 = Room("owl_room1", True, True, True, True)
maze4 = Room("maze4", True, True, True, True)
trap_room = Room("trap_room", False, True, False, True)
maze5 = Room("maze5", True, False, True, False)
maze6 = Room("maze6", True, True, False, True)
scratch_post = Room("scratch_post", True, True, True, False)
maze7 = Room("maze7", True, True, False, True)
maze8 = Room("maze8", True, True, False, False)
maze9 = Room("maze9", True, True, False, False)
maze = Room("maze", True, True, False, False)
shop2 = Room("shop2", False, False, True, False)
cat_tree2 = Room("cat_tree2", True, False, True, True)
key_room1 = Room("key_room1", True, False, False, True)
cactus_room1 = Room("cactus_room1", True, True, False, False)
stairs3 = Room("stairs3", False, False, True, False, True, False)
cactus2 = Room("cactus2", True, False, False, True)

#floor3
stairs4 = Room("stairs4", True, False, False, False, False, True)
owl_room2 = Room("owl_room2", True, True, True, False)
trial1 = Room("trial1", True, False, False, False)
trial2 = Room("trial2", True, False, False, False)
trial3 = Room("trial3", True, False, False, False)
boss = Room("boss", True, False, False, False)
food = Room("food", False, False, False, False)
shop3 = Room("shop3", False, False, False, True)


#start up scripts go here, e.g. title graphic, game_state = "new_game"
game_state = "playing"
player_coords = [3, 4]
HP = 10
HP_max = 10
ATK_bonus = 1
ARM = 0
STR = 3
CON = 3
SPD = 3
LVL = 1
XP = 0
inventory = [potion]
equip = {"Weapon": stick, "Armor": None, "Accessory": None}
floor = 1
current_room = None
get_room(player_coords, floor)
look()
# while loops go here
while game_state == "playing":
    doing = input(" HP {}/{}:".format(HP,HP_max))

    if doing == "north" or doing == "n":
        if current_room.can_north == True:
            player_coords[1] -= 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "south" or doing == "s":
        if current_room.can_south == True:
            player_coords[1] += 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "west" or doing == "w":
        if current_room.can_west == True:
            player_coords[0] -= 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "east" or doing == "e":
        if current_room.can_east == True:
            player_coords[0] += 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")
    
    elif doing == "up" or doing == "u":
        if current_room.can_up == True:
            floor += 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")
    
    elif doing == "down" or doing == "d":
        if current_room.can_down == True:
            floor -= 1
            get_room(player_coords, floor)
            print("new coords: {}".format(player_coords))
            look()
        else:
            print("Can't go that way.")

    elif doing == "inventory" or doing == "inv":
        print(inventory)
        if equip["Weapon"] == None:
            wpn = "Weapon: None |"
        else:
            wpn = "Weapon: " + str(equip["Weapon"]) + " (+{})".format(equip["Weapon"].bonus) + " |"
        if equip["Armor"] == None:
            armr = " Armor: None |"
        else:
            armr = " Armor: " + str(equip["Armor"]) + " (+{})".format(equip["Armor"].bonus) + " |"
        if equip["Accessory"] == None:
            acc = " Accessory: None"
        else:
            acc = " Accessory: " + str(equip["Accessory"])

        print(wpn + armr + acc)
    
    elif doing == "character" or doing == "cha":
        print("STR:", STR, "| CON:", CON, "| SPD:", SPD, "| ATK Bonus:", ATK_bonus, "| ARM:", ARM, "| LVL:", LVL, "| XP:", XP)


    elif doing == "look" or doing == "l":
        look()

    elif "get" in doing:
        tag = doing.split()
        if len(tag) == 1:
            print("Get what?")
        else:
            get_item(tag[1])
    
    elif "use" in doing:
        tag = doing.split()
        if len(tag) == 1:
            print("Use what?")
        else:
            use_item(tag[1])