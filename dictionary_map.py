######Jacob's Experiment######
world_map = {
    'FLOWERBED': {
        'NAME': "Flowerbed",
        'DESCRIPTION': "You're suddenly in a strange flowerbed, at the "
                       "bottom of a giant fall. How'd you survive that? "
                       "There's also a path to the east of you.",
        'PATHS': {
            'EAST': "GREAT_DOOR_1"
        }
    },
    'GREAT_DOOR_1': {
        'NAME': "The Great Door",
        'DESCRIPTION': "All you can see is a door to the north and a "
                      "path to the west back to the flowerbed.",
        'PATHS': {
            'WEST': 'FLOWERBED',
            'NORTH': 'FLOWEY'
        }
    },
    'FLOWEY': {
        'NAME': 'Strange Room',
        'DESCRIPTION': "You can see a strange flower in the room, "
                       "just standing there. The flower has "
                       "a... face?!",
        'PATHS': {
            'SOUTH': 'GREAT_DOOR_1'
        }
    }
}

# Controller
playing = True
current_node = world_map['FLOWERBED']
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
