# # # An Experiment # # #
world_map = {
    'START_ROOM': {
        'NAME': "Starting Room",
        'DESCRIPTION': "You're suddenly in a strange forest, in the "
                       "middle of an island. How'd you get here? "
                       "There's paths to each cardinal direction.",
        'PATHS': {
            'EAST': "EAST_PATH",
            'WEST': "WEST_PATH",
            'NORTH': "NORTH_PATH",
            'SOUTH': "SOUTH_PATH"
        }
    },
    'EAST_PATH': {
        'NAME': "Eastern Path",
        'DESCRIPTION': "You can see paths to the east and north, "
                       "along with a path west, back to where you started.",
        'PATHS': {
            'EAST': 'EAST_DOG',
            'NORTH': 'ARMORY',
            'SOUTH': 'SE_PATH',
            'WEST': 'START_ROOM'
        }
    },
    'WEST_PATH': {
        'NAME': "Western Path",
        'DESCRIPTION': "You can see a path to your west, along with "
                       "a path to the east back to your starting point.",
        'PATHS': {
            'WEST': 'WEST_DOG',
            'EAST': 'START_ROOM',
            'SOUTH': 'SW_PATH'
        }
    },
    'NORTH_PATH': {
        'NAME': "Northern Path",
        'DESCRIPTION': "There's a path to your north, a path "
                       "to your east, and a path back to your "
                       "starting point, to the south.",
        'PATHS': {
            'NORTH': 'NORTH_DOG',
            'SOUTH': 'START_ROOM',
            'EAST': 'ARMORY',
            'WEST': 'NW_PATH'
        }
    },
    'SOUTH_PATH': {
        'NAME': "Southern Path",
        'DESCRIPTION': "You find only two paths to go: one to the "
                       "south, and one to the north, back to your "
                       "starting point.",
        'PATHS': {
            'NORTH': 'START_ROOM',
            'SOUTH': 'SOUTH_DOG',
            'EAST': 'SE_PATH',
            'WEST': 'SW_PATH'
        }
    },
    'EAST_DOG': {
        'NAME': "Eastern Dog Room",
        'DESCRIPTION': "You see a dog in this area, coding a "
                       "game. Maybe you should leave it be. "
                       "Or, maybe you can befriend it?",
        'PATHS': {
            'WEST': 'EAST_PATH',
            'EAST': 'EEE_PATH'
        }
    },
    'WEST_DOG': {
        'NAME': "Western Dog Room",
        'DESCRIPTION': "You see a pair of dogs; one has a scarf, "
                       "the other a pilot's cap. You don't know "
                       "why these dogs have clothes on... but "
                       "you could befriend them if you tried.",
        'PATHS': {
            'EAST': 'WEST_PATH'
        }
    },
    'NORTH_DOG': {
        'NAME': "Northern Dog Room",
        'DESCRIPTION': "You see a pomeranian here, just sitting "
                       "down and drawing a picture. Maybe, just "
                       "maybe, you can befriend it...? "
                       "There's also a path north and a path south.",
        'PATHS': {
            'SOUTH': 'NORTH_PATH',
            'NORTH': 'NNN_PATH'
        }
    },
    'SOUTH_DOG': {
        'NAME': "Southern Dog Room",
        'DESCRIPTION': "You see a small dog jumping up and "
                       "down. It seems to be making an animation. "
                       "Maybe you can befriend it...?",
        'PATHS': {
            'NORTH': 'SOUTH_PATH'
        }
    },
    'ARMORY': {
        'NAME': "Armory",
        'DESCRIPTION': "You find some abandoned armor and a steak here. Maybe "
                       "another person came here before you? "
                       "The steak seems to be infinitely usable to befriend dogs. "
                       "There's also a path south and a path west.",
        'PATHS': {
            'WEST': 'NORTH_PATH',
            'SOUTH': 'EAST_PATH'
        }
    },
    'SW_PATH': {
        'NAME': "Armory",
        'DESCRIPTION': "You find some abandoned armor here. Maybe "
                       "another person came here before you? "
                       "There's also a path north and a path east.",
        'PATHS': {
            'NORTH': 'WEST_PATH',
            'EAST': 'SOUTH_PATH'
        }
    },
    'SE_PATH': {
        'NAME': "Armory",
        'DESCRIPTION': "You find some abandoned armor here. Maybe "
                       "another person came here before you? "
                       "There's also a path north and a path west.",
        'PATHS': {
            'WEST': 'SOUTH_PATH',
            'NORTH': 'EAST_PATH'
        }
    },
    'NW_PATH': {
        'NAME': "Armory",
        'DESCRIPTION': "You find some abandoned armor here. Maybe "
                       "another person came here before you? "
                       "There's also a path south and a path east.",
        'PATHS': {
            'EAST': 'NORTH_PATH',
            'SOUTH': 'WEST_PATH'
        }
    },
    'NNN_PATH': {
        'NAME': "Far North Path",
        'DESCRIPTION': "There's a broken-down boat here. If you "
                       "could fix it, you might be able to escape "
                       "this island.",
        'PATHS': {
            'SOUTH': 'NORTH_DOG',
            'NORTH': 'WIN'
        }
    },
    'EEE_PATH': {
        'NAME': "Far Eastern Path",
        'DESCRIPTION': "You're at the most far east point at the island. "
                       "There's some wood you could use to build something.",
        'PATHS': {
            'WEST': 'EAST_DOG'
        }
    },
    'WIN': {
        'NAME': "You've won the game!",
        'DESCRIPTION': "You've escaped the island and survived the dogs. "
                       "You can type \'restart\' to restart the game.",
    }

}

# Controller
playing = True
current_node = world_map['START_ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in ['restart']:
        current_node = world_map['START_ROOM']
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("You can't go that way.")
    elif command.lower() in ['zork']:
        print("Wrong game.")
    else:
        print("I don't know that command.")
