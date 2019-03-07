class Item(object):
    def __init__(self, name, uses, value):
        self.uses = uses
        self.name = name
        self.value = value


class Armor(Item):
    def __init__(self, equipable, durability):
        super(Armor, self).__init__("Armor", 999, 1)
        self.equipable = equipable
        self.durability = durability


class Helmet(Armor):
    def __init__(self, defense):
        super(Helmet, self).__init__(True, 999)
        self.defense = defense


class Torso(Armor):
    def __init__(self, defense):
        super(Torso, self).__init__(True, 999)
        self.defense = defense


class Boots(Armor):
    def __init__(self, defense):
        super(Boots, self).__init__(True, 999)
        self.defense = defense


class Weapon(Item):
    def __init__(self):
        super(Weapon, self).__init__(True, 999, 1)
        self.uses = 999
        self.equipable = True
        self.attack = 1


class Food(Item):
    def __init__(self, taste, size):
        super(Food, self).__init__("Food", 1, 1)
        self.taste = taste
        self.size = size


class Consumable(Item):
    def __init__(self, size, effect):
        super(Consumable, self).__init__("Consumable", 1, 1)
        self.size = size
        self.effect = effect


class BaseballCap(Helmet):
    def __init__(self):
        super(BaseballCap, self).__init__(3)
        self.uses = 999
        self.equipable = True
        self.defense = 3
        self.name = "Lucky Baseball Cap"
        self.description = "A baseball cap that reminds you of a forgotten hero..."


class PlanetBuster(Weapon):
    def __init__(self):
        super(PlanetBuster, self).__init__()
        self.uses = 999
        self.equipable = True
        self.attack = 24
        self.name = "The Planet Buster"
        self.description = "A powerful sword you are lucky to brandish."


class IdArmor(Torso):
    def __init__(self):
        super(IdArmor, self).__init__(32)
        self.uses = 999
        self.equipable = True
        self.defense = 32
        self.name = "Armor of THE ID"
        self.description = "An armor based on the representation of your Id. It's slimy..."


class BottleRocket(Weapon):
    def __init__(self):
        super(BottleRocket, self).__init__()
        self.equipable = True
        self.uses = 1
        self.attack = 64
        self.name = "Jeff's Bottle Rocket"
        self.description = "A very powerful bottle rocket by a young Mr. Andonuts. Can only be used once."


class BalletShoes(Weapon):
    def __init__(self):
        super(BalletShoes, self).__init__()
        self.uses = 999
        self.name = "Ballet Shoes"
        self.description = "These used shoes make you feel incredibly dangerous."
        self.equipable = True
        self.attack = 1


class DustyTutu(Torso):
    def __init__(self):
        super(DustyTutu, self).__init__(3)
        self.uses = 999
        self.name = "Dusty Tutu"
        self.description = "Finally, a PROTECTIVE piece of armor."
        self.equipable = True
        self.defense = 3


class MysteryCloak(Torso):
    def __init__(self):
        super(MysteryCloak, self).__init__(6)
        self.uses = 999
        self.name = "Mystery Man's Cloak"
        self.description = "The cloak of someone known only as the 'Mystery Man.' It looks like it's made out of " \
                           "vantablack, or something..."
        self.equipable = True
        self.defense = 6


class SpadeOutfit(Torso):
    def __init__(self):
        super(SpadeOutfit, self).__init__(1)
        self.uses = 999
        self.name = "Ace Outfit (Spade Variation)"
        self.description = "Not to call a spade a spade, but this is a spade."
        self.equipable = True
        self.defense = 1


class JammyDodger(Food):
    def __init__(self):
        super(JammyDodger, self).__init__("Sweet", "Small")
        self.hp_heal = 2
        self.name = "Jammy Dodger"
        self.description = "A cookie with jam in the middle. Popular in Britain. Heals 2 HP."


class Steak(Food):
    def __init__(self):
        super(Steak, self).__init__("Savory", "Big")
        self.hp_heal = 15
        self.name = "Steak"
        self.description = "A large, medium-well steak. It's really salty. Heals 15 HP."


class Grasshopper(Food):
    def __init__(self):
        super(Grasshopper, self).__init__("Savory", "Small")
        self.hp_heal = 1
        self.name = "Grasshopper"
        self.description = "A chocolate-covered grasshopper. It's not too tasty, but it'll have to do."


class Inhaler(Consumable):
    def __init__(self):
        super(Inhaler, self).__init__("Small", "Status Heal")
        self.name = "Asthma Inhaler"
        self.description = "An inhaler for asthma. If you have an asthma attack, it'll be pretty handy."


class SmokeBomb(Consumable):
    def __init__(self):
        super(SmokeBomb, self).__init__("Small", "Battle Effect")
        self.name = "Smoke Bomb"
        self.description = "A small smoke bomb. It'll make smoke appear wherever you use it."


class WarHorn(Weapon):
    def __init__(self):
        super(WarHorn, self).__init__()
        self.equipable = True
        self.uses = 999
        self.attack = 20
        self.name = "War Horn"
        self.description = "You can blast away your opponents with these harsh sounds!"


class WaterGun(Weapon):
    def __init__(self):
        super(WaterGun, self).__init__()
        self.equipable = True
        self.uses = 999
        self.attack = 2
        self.name = "Water Gun"
        self.description = "A small water gun. It's extremely effective against things made of fire, unsurprisingly."


class PencilBlade(Weapon):
    def __init__(self):
        super(PencilBlade, self).__init__()
        self.equipable = True
        self.uses = 999
        self.attack = 7
        self.name = "Pencil Blade"
        self.description = "A wooden blade with a carbon-reinforced core."


class Jevilstail(Torso):
    def __init__(self):
        super(Jevilstail, self).__init__(5)
        self.name = "Jevilstail"
        self.description = "You didn't know you'd grow a tail. It's pretty chaotic, honestly."
