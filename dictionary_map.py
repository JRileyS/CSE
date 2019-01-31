world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right "
                       "now. There are two doors on the north wall.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    }
}

######Jacob's Experiment######
#world_map = {
#    'FLOWERBED': {
#        'NAME': "Flowerbed",
#        'DESCRIPTION': "You're suddenly in a strange flowerbed, at the "
#                       "bottom of a giant fall. How'd you survive that? "
#                       "There's also a path to the east of you.",
#        'PATHS': {
#            'EAST': "GREAT_DOOR"
#        }
#    },
#    'GREAT_DOOR': {
#        'NAME': "The Great Door",
#        'DESCRIPTION': "All you can see is a door to the north and a "
#                      "path to the west back to the flowerbed.",
#        'PATHS': {
#            'WEST': 'FLOWERBED',
#            'NORTH': 'FLOWEY'
#        }
#    },
#    'FLOWEY': {
#        'NAME': 'Strange Room',
#        'DESCRIPTION': "You can see a strange flower in the room, "
#                       "just standing there. It has a face?",
#        'PATHS': {
#            'SOUTH': 'GREAT_DOOR'
#        }
#    }
#}

# Controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        room_name = current_node['PATHS'][command]
        current_node = world_map[room_name]
    else:
        print("I don't know that command.")
