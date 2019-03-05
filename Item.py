class Item(object):
    def __init__(self, name, uses, value):
        self.uses = uses
        self.name = name
        self.value = value


class Armor(Item):
    def __init__(self):
        super(Armor, self).__init__("Armor", 999, 1)
        self.equipable = equipable
        self.durability = durability


class Helmet(Armor):
    def __init__(self):
        super(Helmet, self).__init__(True, 999)
        self.defense = defense


class Torso(Armor):
    def __init__(self):
        super(Torso, self).__init__(True, 999)
        self.defense = defense


class Boots(Armor):
    def __init__(self):
        super(Boots, self).__init__(True, 999)
        self.defense = defense


class Weapon(Item):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.attack = 1


class BaseballCap(Helmet):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.defense = 3
        self.name = "Lucky Baseball Cap"
        self.description = "A baseball cap that reminds you of a forgotten hero..."


class PlanetBuster(Weapon):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.attack = 24
        self.name = "The Planet Buster"
        self.description = "A powerful sword you are lucky to brandish."


class IdArmor(Torso):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.defense = 32
        self.name = "Armor of THE ID"
        self.description = "An armor based on the representation of your Id. It's slimy..."


class BottleRocket(Weapon):
    def __init__(self):
        self.equipable = True
        self.uses = 1
        self.attack = 64
        self.name = "Jeff's Bottle Rocket"
        self.description = "A very powerful bottle rocket by a young Mr. Andonuts. Can only be used once."


class BalletShoes(Boots):
    def __init__(self):
        self.uses = 999
        self.name = "Ballet Shoes"
        self.description = "These used shoes make you feel incredibly dangerous."
        self.equipable = True
        self.attack = 1


class DustyTutu(Torso):
    def __init__(self):
        self.uses = 999
        self.name = "Dusty Tutu"
        self.description = "Finally, a PROTECTIVE piece of armor."
        self.equipable = True
        self.defense = 3


class MysteryCloak(Torso):
    def __init__(self):
        self.uses = 999
        self.name = "Mystery Man's Cloak"
        self.description = "The cloak of someone known only as the 'Mystery Man.' It looks like it's made out of " \
                           "vantablack, or something..."
        self.equipable = True
        self.defense = 6


class SpadeOutfit(Torso):
    def __init__(self):
        self.uses = 999
        self.name = "Ace Outfit"
        self.description = "Not to call a spade a spade, but this is a spade."
        self.equipable = True
        self.defense = 1