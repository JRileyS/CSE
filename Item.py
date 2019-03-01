class Item(object):
    def __init__(self):
        self.uses = 1


class Armor(Item):
    def __init__(self):
        self.uses = 999
        self.equipable = True


class Helmet(Armor):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.defense = 1


class Torso(Armor):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.defense = 1


class Boots(Armor):
    def __init__(self):
        self.uses = 999
        self.equipable = True
        self.defense = 1


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
        self.attack = 6
        self.name = "The Planet Buster"
        self.description = "A powerful sword you are lucky to brandish."


