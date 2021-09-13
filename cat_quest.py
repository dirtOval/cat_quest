#libraries go here
import random


#classes

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
        global WPN_bonus
        if not equip["Weapon"] == None:
            inventory.append(equip["Weapon"])
        equip["Weapon"] = weapon
        inventory.remove(weapon)
        WPN_bonus = weapon.bonus
        update_attack()
        print("{} equipped! (+{})".format(weapon.id, weapon.bonus))

class Armor(Item):
    def __init__(self, id, value, bonus):
        super().__init__(id, value)
        self.bonus = bonus

    def equip_armor(self, armor):
        global equip
        global ARM
        if not equip["Armor"] == None:
            inventory.append(equip["Armor"])
        equip["Armor"] = armor
        inventory.remove(armor)
        ARM = armor.bonus
        print("{} equipped! (+{})".format(armor.id, armor.bonus))

class Accessory(Item):
    def __init__(self, id, value, bonus):
        super().__init__(id, value)
        self.bonus = bonus

    def effect(self):
        global HP_max
        global ATK_effect
        global ARM
        global STR
        global CON
        global SPD

        if self.bonus == "HP_boost":
            HP_max += 5

        if self.bonus == "ATK_up":
            ATK_effect = 3
            update_attack()

    def uneffect(self):
        global HP
        global HP_max
        global ATK_effect
        global ARM
        global STR
        global CON
        global SPD

        if self.bonus == "HP_boost":
            HP_max -= 5
            if HP > HP_max:
                HP = HP_max

        if self.bonus == "ATK_up":
            ATK_effect = 0
            update_attack()

    def equip_accessory(self, acc):
        global equip
        if not equip["Accessory"] == None:
            inventory.append(equip["Accessory"])
            equip["Accessory"].uneffect()
        equip["Accessory"] = acc
        inventory.remove(acc)
        acc.effect()
        print("{} equipped! (+{})".format(acc.id, acc.bonus))

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
        self.visited = visited
    def __repr__(self, roomID):
        return self.roomID

class Mob:
    def __init__(self, ID, HP, STR, CON, SPD, XP):
        self.ID = ID
        self.HP = HP
        self.STR = STR
        self.CON = CON
        self.SPD = SPD
        self.XP = XP
    def __repr__(self):
        return self.ID

#Functions
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
        #accessories
        elif id == "tough_collar":
            inventory.append(tough_collar)
            current_room.items.remove(tough_collar)
        elif id == "cute_collar":
            inventory.append(cute_collar)
            current_room.items.remove(cute_collar)
        
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
        
        #accessories
        elif id == "tough_collar":
            tough_collar.equip_accessory(tough_collar)
        elif id == "cute_collar":
            cute_collar.equip_accessory(cute_collar)
            
def update_attack():
    global ATK_bonus
    global WPN_bonus
    global ATK_effect
    global STR
    ATK_bonus = WPN_bonus + ATK_effect + STR

def update_HP_total():
    global HP_max
    HP_max = 1 + (3 * CON)

def random_encounter_check():
    global game_state
    chance = random.randint(1, 100)
    if chance >= 70:
        print("RANDOM ENCOUNTER! TIME TO FIGHT!")
        random_encounter()

def random_encounter():
    global floor
    global enemies
    global game_state
    if floor == 1:
        amount = random.randint(1, 3)
        for num in range(1, amount+1):
            enemies.append(dog)
        game_state = "combat"
        print("{} dogs appear, teeth bared!".format(amount))

def player_attack(target):
    global ATK_bonus
    global WPN_bonus
    global STR
    global XP
    roll = random.randint(1, 20) + ATK_bonus
    if roll >= 10 + target.SPD:
        damage = WPN_bonus + STR
        target.HP -= damage
        print("Did {} damage to {} ({} left)".format(damage, target, target.HP))
        if target.HP <= 0:
            print("{} died!".format(target))
            print("Gained {} XP".format(target.XP))
            XP += target.XP
            enemies.remove(target)
    else:
        print("You missed!")

def enemy_attack(attacker):
    global HP
    global SPD
    for enemy in enemies:
        roll = random.randint(1,20) + enemy.STR
        if roll >= 10 + SPD:
            damage = STR
            print("{} did {} damage to you!".format(enemy, damage))
            HP -= damage
            death_check()
        else:
            print("{} attacked, but missed!".format(enemy))

def death_check():
    global game_state
    if HP <= 0:
        game_state = "game_over"

def game_restart():
    global game_state
    global enemies
    global WPN_bonus
    global ATK_effect
    global ATK_bonus
    global ARM
    global STR
    global CON
    global SPD
    global LVL
    global XP
    global HP
    global HP_max
    global inventory
    global equip
    global current_room
    game_state = "playing"
    enemies = []
    player_coords = [3, 4]
    WPN_bonus = 1
    ATK_effect = 0
    ATK_bonus = 0
    ARM = 0
    STR = 3
    CON = 3
    SPD = 3
    LVL = 1
    XP = 0
    update_attack()
    update_HP_total()
    HP = HP_max
    inventory = []
    equip = {"Weapon": stick, "Armor": None, "Accessory": None}
    floor = 1
    current_room = None
    get_room(player_coords, floor)
    look()

#enemy objects go here
dog = Mob("dog", 5, 3, 3, 3, 25)

#item objects go here
potion = Item("potion", 50)
#weapons
sword = Weapon("sword", 100, 5)
stick = Weapon("stick", 5, 1)
#armor
cat_armor = Armor("cat_armor", 150, 5)
#accessories
tough_collar = Accessory("tough_collar", 200, "HP_boost")
cute_collar = Accessory("cute_collar", 200, "ATK_up")
# Room objects go here: (roomID, north, south, east, west, up, down, items)
#floor 1
bed = Room("bed", False, False, False, True, False, False, [potion])
dungeon = Room("dungeon", True, True, True, False, False, False)
bathroom = Room("bathroom", True, False, False, False, items=[cat_armor])
hallway1 = Room("hallway1", True, True, False, False, False, False)
hallway2 = Room("hallway2", True, True, False, True, False, False)
closet = Room("closet", False, False, True, True, False, False)
secret_chamber = Room("secret_chamber", False, False, True, False, items=[tough_collar])
hallway3 = Room("hallway3", True, True, True, False, False, False)
armory = Room("armory", False, False, False, True, False, False, [sword])
cat_tree1 = Room("cat_tree1", False, True, True, True, False, False)
shop1 = Room("shop1", False, False, False, True, items=[cute_collar])
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
enemies = []
player_coords = [3, 4]
WPN_bonus = 1
ATK_effect = 0
ATK_bonus = 0
ARM = 0
STR = 3
CON = 3
SPD = 3
LVL = 1
XP = 0
update_attack()
update_HP_total()
HP = HP_max
inventory = []
equip = {"Weapon": stick, "Armor": None, "Accessory": None}
floor = 1
current_room = None
get_room(player_coords, floor)
look()
game_running = True

while game_running:

# while loops go here
    while game_state == "playing":
    
        if XP >= 100 * LVL:
            game_state = "level_up"
    
        doing = input(" HP {}/{}:".format(HP,HP_max))    
        #control commands
        if doing == "north" or doing == "n":
            if current_room.can_north == True:
                player_coords[1] -= 1
                get_room(player_coords, floor)
                print("new coords: {}".format(player_coords))
                look()
                random_encounter_check()
            else:
                print("Can't go that way.")

        elif doing == "south" or doing == "s":
            if current_room.can_south == True:
                player_coords[1] += 1
                get_room(player_coords, floor)
                print("new coords: {}".format(player_coords))
                look()
                random_encounter_check()
            else:
                print("Can't go that way.")

        elif doing == "west" or doing == "w":
            if current_room.can_west == True:
                player_coords[0] -= 1
                get_room(player_coords, floor)
                print("new coords: {}".format(player_coords))
                look()
                random_encounter_check()
            else:
                print("Can't go that way.")

        elif doing == "east" or doing == "e":
            if current_room.can_east == True:
                player_coords[0] += 1
                get_room(player_coords, floor)
                print("new coords: {}".format(player_coords))
                look()
                random_encounter_check()
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
                acc = " Accessory: " + str(equip["Accessory"]) + " (+{})".format(equip["Accessory"].bonus)

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
        #TEST COMMANDS: REMOVE THESE LATER!!
        elif "OP_giveXP" in doing:
            tag = doing.split()
            if len(tag) == 1:
                print("how much xp?")
            else:
                XP += int(tag[1])
        elif doing == "OP_fight":
            random_encounter()

    while game_state == "level_up":
        congrats = False
        if congrats == False:
            print("|~|LEVEL UP|~|")
            print("Select Stat to upgrade:")
            print("1. STR")
            print("2. CON")
            print("3. SPD")

        XP -= 100 * LVL
        LVL += 1
        choice = input(" HP {}/{}:".format(HP,HP_max))
        if choice == "1":
            STR += 1
            print("STR Boosted!")
            print("New STR: {}".format(STR))
            update_attack()
            game_state = "playing"
        elif choice == "2":
            CON += 1
            print("CON Boosted!")
            print("New CON: {}".format(CON))
            update_HP_total()
            game_state = "playing"
        elif choice == "3":
            SPD += 1
            print("SPD Boosted!")
            print("New SPD: {}".format(SPD))
            game_state = "playing"
    
    while game_state == "combat":
        #generate enemies for player (do in random_encounter())
        #lay out combat (e.g. player vs how many enemies of what kind)
        #give the player numbered options
        while len(enemies) > 0 and HP > 0:
            print(enemies)
            print("1. Attack")
            print("2. Use Item")
            print("3. Run Away")
            choice = input(" HP {}/{}:".format(HP,HP_max))
            if choice == "1":
                for num in range(len(enemies)):
                    print(str(num+1) + ".", enemies[num-1])
                target = int(input("Which enemy?"))
                for num in range(len(enemies)):
                    if target-1 == num:
                        player_attack(enemies[num])
                        enemy_attack(enemies)
        if HP > 0:
            game_state = "playing"
            look()
        else:
            game_state = "game_over"


    while game_state == "game_over":
        print("YOU HAVE DIED! GAME OVER")
        print("1. Restart")
        print("2. Quit")
        choice = (input("What would you like to do?"))
        if choice == "1":
            game_restart()
        elif choice == "2":
            print("Goodbye!")
            game_running == False
            exit()
        else:
            print("Huh?")


    