######Jacob's Experiment######
world_map = {
    'START_ROOM': {
        'NAME': "Starting Room",
        'DESCRIPTION': "You're suddenly in a strange room, at the "
                       "bottom of a giant fall. How'd you survive that? "
                       "There's paths to each cardinal direction.",
        'PATHS': {
            'EAST': "EAST_START",
            'WEST': "WEST_START",
            'NORTH': "NORTH_START",
            'SOUTH': "SOUTH_START"
        }
    },
    'EAST_START': {
        'NAME': "Eastern Start",
        'DESCRIPTION': "You can see paths to the east and north, "
                       "along with a path west, back to where you started.",
        'PATHS': {
            'EAST': 'EAST_ARENA',
            'NORTH': 'ARMORY'
        }
    },
    'WEST_START': {
        'NAME': "Western Start",
        'DESCRIPTION': "You can see a path to your west, along with "
                       "a path to the east back to your starting point."
    },
    'EAST_ARENA': {
        'NAME': "Eastern Arena",
        'DESCRIPTION': "You see a dog in the arena, coding a "
                       "game. Maybe you should leave it be.",
        'PATHS': {
            'WEST': 'EAST_START'
        }
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
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("You can't go that way.")
    else:
        print("I don't know that command.")
