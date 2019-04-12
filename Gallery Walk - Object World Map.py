from typing import List, Any

Inventory: List[Any] = []
whatever = []


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.characters = []
        self.items = items


class Item(object):
    def __init__(self, name, uses, value):
        self.uses = uses
        self.name = name
        self.value = value


armor_amt = 0


class Character(object):
    def __init__(self, name, health: int, armor, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon

    def take_damage(self, damage: int):
        if self.health - (damage - self.armor.armor_amt) <= 0:
            print("The %s became tame!" % self.name)
        else:
            if self.armor.armor_amt > damage:
                print("The armor blocked the attack!")
            else:
                self.health -= damage - self.armor.armor_amt
            print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s with %s for %d damage!" % (self.name, target.name, self.weapon.name,
                                                        (self.weapon.attack - target.armor.armor_amt)))
        target.take_damage(self.weapon.attack)


class Armor(Item):
    def __init__(self, equipable, durability, armor_amt_equip: int):
        super(Armor, self).__init__("Armor", 999, 1)
        self.equipable = equipable
        self.durability = durability
        self.armor_amt = armor_amt_equip


class Helmet(Armor):
    def __init__(self, uses, defense, name, description):
        super(Helmet, self).__init__(True, 999, armor_amt, )
        self.uses = uses
        self.equipable = True
        self.defense = defense
        self.name = name
        self.description = description


class Torso(Armor):
    def __init__(self, uses, defense, name, description):
        super(Torso, self).__init__(True, 999, armor_amt, )
        self.uses = uses
        self.equipable = True
        self.defense = defense
        self.name = name
        self.description = description


class Boots(Armor):
    def __init__(self, uses, defense, name, description):
        super(Boots, self).__init__(True, 999, armor_amt, )
        self.uses = uses
        self.equipable = True
        self.defense = defense
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, uses, attack: int, name, description):
        super(Weapon, self).__init__(True, 999, 1)
        self.uses = uses
        self.equipable = True
        self.attack = attack
        self.name = name
        self.description = description


class Food(Item):
    def __init__(self, hp_heal, taste, size, name, description):
        super(Food, self).__init__("Food", 1, 1)
        self.hp_heal = hp_heal
        self.taste = taste
        self.size = size
        self.name = name
        self.description = description


class Consumable(Item):
    def __init__(self, size, effect, name, description):
        super(Consumable, self).__init__("Consumable", 1, 1)
        self.size = size
        self.effect = effect
        self.name = name
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.armor_head = []
        self.armor_torso = []
        self.armor_legs = []
        self.flavor = "salty"
        self.name = "You"

    def move(self, new_location):
        """This moves the player to a new room.

        :param new_location: The room object of which you are going to move to.
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction.

        :param direction: The direction you want to move to.
        :return: The Room object if it exists, or None if not.
        """
        return getattr(self.current_location, direction)


# Items, Weapons, and Armor
PencilBlade = Weapon(999, 7, "Pencil Blade", "A wooden practice blade with a carbon-reinforced core.")
BottleRocket = Weapon(1, 24, "Bottle Rocket", "A powerful bottle rocket weapon. Can only be used once.")
BalletShoes = Weapon(999, 10, "Ballet Shoes", "These used shoes make you feel incredibly dangerous.")
WaterGun = Weapon(999, 2, "Water Gun", "A small water gun that's unsurprisingly effective against fire.")
WarHorn = Weapon(999, 20, "War Horn", "Blow away your foes with these harsh sounds!")
OldTutu = Torso(999, 10, "Old Tutu", "Finally, a PROTECTIVE piece of armor.")
Jevilstail = Boots(999, 5, "Jevilstail", "A J-shaped tail that gives you chaotic energy.")
BaseballCap = Helmet(999, 2, "Baseball Cap", "A baseball cap that belonged to a fallen hero...")
SpadeOutfit = Torso(999, 1, "Ace Outfit", "Not to call a spade a spade, but this is a spade.")
MysteryCloak = Torso(999, 6, "Mystery Man's Cloak", "A cloak belonging to the Mystery Man.")
Inhaler = Consumable("Small", "Status Heal", "Asthma Inhaler", "An inhaler for asthma attacks.")
SmokeBomb = Consumable("Small", "Battle Effect", "Smoke Bomb", "A small smoke bomb that makes smoke appear whenever "
                                                               "you use it.")
Steak = Food(15, "Salty", "Big", "Steak", "A medium-rare steak. It's pretty salty, but still tastes good. Heals 15 HP.")
JammyDodger = Food(2, "Sweet", "Small", "Jammy Dodger", "A cookie with jam in it. Popular in Britain. Heals 2 HP.")
Grasshopper = Food(1, "Savory", "Small", "Grasshopper", "A chocolate-covered grasshopper. Not too good, but it'll "
                                                        "have to do. Heals 1 HP.")
IdArmor = Torso(999, 32, "ID Armor", "An armor based on your Id. It's really slimy...")

# Option 1 - Define as we go
StartRoom = Room("Starting Room", "You're suddenly in a strange forest, in the middle of an island. How'd you get "
                                  "here? There's paths to each cardinal direction.")
northern_path = Room("Northern Path", "There's a path to your north, a path to your east, and a path back to your "
                                      "starting point, to the south.", None, StartRoom, None, None, None)
southern_path = Room("Southern Path", "You find three paths to go to: one to the south, one to the west, and one to "
                                      "the north, back to your starting point.", StartRoom, None, None, None, None)
eastern_path = Room("Eastern Path", "You can see paths to the east and north, along with a path west, back to where "
                                    "you started.", None, None, None, StartRoom, None)
western_path = Room("Western Path", "You can see a path to your west, a path south, and a path back east to your "
                                    "starting point.", None, None, StartRoom, None, None)
ne_path = Room("Armory", "You find some abandoned armor here, along with a large number of steaks. Maybe someone was"
                         " here before you? There are also paths south and "
                         "west.", None, eastern_path, None, northern_path, PencilBlade)
nw_path = Room("Northwest Path", "You can barely see anything except the paths to the south and "
                                 "east.", None, western_path, northern_path, None, None)
se_path = Room("Southeast Path", "You can only see paths to the north and "
                                 "west.", eastern_path, None, None, southern_path, None)
sw_path = Room("Southwest Path", "You're surrounded by trees, but there are paths to the north and "
                                 "east.", western_path, None, southern_path, None, None)
northern_dog = Room("Dog Room (North)", "There's a pomeranian here, just sitting down and drawing a picture. Maybe, "
                                        "just maybe, you can befriend it...? There are also paths north and "
                                        "south.", None, northern_path, None, None, None)
southern_dog = Room("Dog Room (South)", "There's a small dog jumping up and down. It seems to just be recording an "
                                        "animation. Maybe you could befriend it...?", southern_path, None, None, None,
                    None)
eastern_dog = Room("Dog Room (East)", "You observe the dog that's in here. It seems to be writing code on a laptop."
                                      "It's coding a game...? And can you really befriend a dog that's so"
                                      "distracted?", None, None, None, eastern_path, None)
western_dog = Room("Dog Room (West)", "Are you seeing double? There are TWO dogs here. One has a scarf, and the other"
                                      "has a pilot's cap. Where do dogs even get clothes? Anyways, you should probably"
                                      "find a way to get around them.", None, None, western_path, None, None)
nnn_path = Room("Far Northern Path", "You're past the Dog Room, and there's a broken boat here. If you found some "
                                     "wood, you could fix it, but right now, you can't "
                                     "sail.", None, northern_dog, None, None, None)
sss_path = Room("Far Southern Path", "You're past the Southern Dog Room. There's a dead end here, but you can still "
                                     "go back.", southern_dog, None, None, None, None)
eee_path = Room("Far Eastern Path", "There's a dead end past the Eastern Dog Room, but there is some wood here you "
                                    "can take.", None, None, None, eastern_dog, None)
www_path = Room("Far Western Path", "There's a beach here. It might be a dead end, but you're at least past the "
                                    "dogs.", None, None, western_dog, None, None)
water = Room("The Ocean", "You're riding a boat on the ocean. You're escaping the "
                          "island!", None, None, www_path, None, None)
win = Room("You Win!", "You successfully escaped the island of dogs, and you can restart by running the program "
                       "again.", None, None, None, None, None)


StartRoom.north = northern_path
StartRoom.south = southern_path
StartRoom.east = eastern_path
StartRoom.west = western_path
northern_path.north = northern_dog
northern_path.east = ne_path
northern_path.west = nw_path
southern_path.east = se_path
southern_path.west = sw_path
eastern_path.north = ne_path
eastern_path.south = se_path
western_path.north = nw_path
western_path.south = sw_path
southern_path.south = southern_dog
eastern_path.east = eastern_dog
western_path.west = western_dog
northern_dog.north = nnn_path
southern_dog.south = sss_path
eastern_dog.east = eee_path
western_dog.west = www_path
www_path.west = water
water.west = win


player = Player(StartRoom)
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in ['restart']:
        player.current_location = StartRoom
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            if next_room is None:
                raise AttributeError
            player.move(next_room)
        except KeyError:
            print("You can't go that way.")
        except AttributeError:
            print("This path doesn't exist.")
    elif command.lower() in ['zork']:
        print("This isn't The Great Underground Empire.")
    elif command.lower() in ['take']:
        if player.current_location.items is not []:
            print("You took the " + str(player.current_location.items.name) + ".")
            Inventory += str(player.current_location.items.name)
        else:
            print("But there was nothing to take.")
    elif command.lower() in ['pick up']:
        if player.current_location.items is not []:
            print("You picked up the " + str(player.current_location.items.name) + ".")
            Inventory += str(player.current_location.items.name)
            player.current_location.items -= player.current_location.items
        else:
            print("But there was nothing to pick up.")
    elif command.lower() in ['inventory']:
        for Inventory in range(player.current_location.items):
            print(str(Inventory))
    else:
        print("I don't know that command.")
