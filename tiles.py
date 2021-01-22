#!/usr/bin/python3
# Austin McCowan
# 12/11/2020
''' Tile design and control file '''

''' Use a dictionary to link information about a tile type to the tiles themselves, i.e just find the key (tile name), and
then find the index of the piece of information and done. Since all tile types will share the same format/order of information in their
lists, this should not create problems.
'''
# Information may include: functionality, defense rating, movement cost...
# For defense rating, each star grants a 10% defense buff. to a max of 40%!
# information format: Functionality, defense rating, movement costs: foot, tires, tread (air isnt needed as its always 1)
global tiletypes
tiletypes = {
    "grass":[False, 1, 2, 2], 
    "road":[False, 1, 1, 1], 
    "factory":[True, 2, 2, 2],
    "water":[False, 100, 100, 100],
    "mountain":[False, 3, 100, 100],
    "city":[True, 2, 2, 2],
    "forest":[False, 2, 3, 3]
}

class TileObject(object):
    
    def __init__(self, tile_id, move_cost, pos_x, pos_y, defense=0, occupied=False):
        # Set up base stats for tiles
        # Decided to make move_cost a dictionary as to reduce variable count
        self.move_cost = {"foot": None,
                          "tires": None,
                          "tread": None, 
                          "air": 1}
        self.tile_id = tile_id 
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.functionality = False
        self.usable = None
        self.health = None

        # Start setting up functionality
        reader = self.tile_id.split("#")
        if reader[0] not in tiletypes:
            raise Exception('Invalid tile type detected')
        if reader[0] in ["city", "factory"]:
            self.functionality = True

        # Will enable the usable variable if functionality exists, this is 
        if self.functionality != False:
            self.usable = True
        
