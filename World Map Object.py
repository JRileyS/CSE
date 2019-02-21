class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# Option 1 - Define as we go
StartRoom = Room("Starting Room", "You're suddenly in a strange forest, in the middle of an island. How'd you get "
                                  "here? There's paths to each cardinal direction.")
northern_path = Room("Northern Path", "There's a path to your north, a path to your east, and a path back to your "
                                      "starting point, to the south.", None, StartRoom, None, None)
southern_path = Room("Southern Path", "You find three paths to go to: one to the south, one to the west, and one to "
                                      "the north, back to your starting point.", StartRoom, None, None, None)
eastern_path = Room("Eastern Path", "You can see paths to the east and north, along with a path west, back to where "
                                    "you started.", None, None, None, StartRoom)
western_path = Room("Western Path", "You can see a path to your west, a path south, and a path back east to your "
                                    "starting point.", None, None, StartRoom, None)
northern_dog = Room("Dog Room (North)", "There's a pomeranian here, just sitting down and drawing a picture. Maybe, "
                                        "just maybe, you can befriend it...? There are also paths north and south.",
                    None, northern_path, None, None)
southern_dog = Room("Dog Room (South)", "There's a small dog jumping up and down. It seems to just be recording an "
                                        "animation. Maybe you could befriend it...?", southern_path, None, None, None)
eastern_dog = Room("Dog Room (East)", "You observe the dog that's in here. It seems to be writing code on a laptop."
                                      "It's coding a game...? And can you really befriend a dog that's so"
                                      "distracted?", None, None, None, eastern_path)
western_dog = Room("Dog Room (West)", "Are you seeing double? There are TWO dogs here. One has a scarf, and the other"
                                      "has a pilot's cap. Where do dogs even get clothes? Anyways, you should probably"
                                      "find a way to get around them.", None, None, western_path, None)
nnn_path = Room("Far Northern Path", "You're past the Dog Room, and there's a broken boat here. If you found some"
                                     "wood, you could fix it, but right now, you can't sail.", None, northern_dog, None,
                None)
sss_path = Room("Far Southern Path", "You're past the Southern Dog Room. There's a dead end here, but you can still "
                                     "go back.", southern_dog, None, None, None)
eee_path = Room("Far Eastern Path", "There's a dead end past the Eastern Dog Room, but there is some wood here you "
                                    "can take.", None, None, None, eastern_dog)
www_path = Room("Far Western Path", "There's a beach here. It might be a dead end, but you're at least past the dogs.",
                None, None, western_dog, None)
water = Room("The Ocean", "You're riding a boat on the ocean. You're escaping the island!", None, None, www_path, None)
win = Room("You Win!", "You successfully escaped the island of dogs, and you can restart by running the program "
                       "again.", None, None, None, None)

StartRoom.north = northern_path
StartRoom.south = southern_path
StartRoom.east = eastern_path
StartRoom.west = western_path
northern_path.north = northern_dog
southern_path.south = southern_dog
eastern_path.east = eastern_dog
western_path.west = western_dog
northern_dog.north = nnn_path
southern_dog.south = sss_path
eastern_dog.east = eee_path
western_dog.west = www_path
www_path.west = water
water.west = win

# Sonnet I #

# From fairest creatures we desire increase,
# That thereby beauty's rose might never die,
# But as the riper should by time decease,
# His tender heir might bear his memory:
# But thou contracted to thine own bright eyes,
# Feed'st thy light's flame with self-substantial fuel,
# Making a famine where abundance lies,
# Thy self thy foe, to thy sweet self too cruel:
# Thou that art now the world's fresh ornament,
# And only herald to the gaudy spring,
# Within thine own bud buriest thy content,
# And, tender churl, mak'st waste in niggarding:
# Pity the world, or else this glutton be,
# To eat the world's due, by the grave and thee.
