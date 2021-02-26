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
    "grass":[False, 1, 1, 2, 2], 
    "road":[False, 0, 1, 1, 1], 
    "factory":[True, 3, 2, 2, 2],
    "water":[False, 0, 100, 100, 100],
    "mountain":[False, 4, 3, 100, 100],
    "city":[True, 3, 2, 2, 2],
    "forest":[False, 2, 2, 3, 3]
}

class TileObject(object):
    # Holds tile positions (i.e 1:(1,2,1,4), 2:(2,2,1,4)...) Might move to Data class in maintester
    tiles = {}

    def __init__(self, tile_id, pos_x=0, pos_y=0, color=None, occupied=False):
        # Set up base stats for tiles
        # Decided to make move_cost a dictionary as to reduce variable count
        self.move_cost = {"foot": None,
                          "tires": None,
                          "tread": None, 
                          "air": 1}
        self.tile_id = tile_id 
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.defense = 0
        # These parameters / variables / stats are set to none as they are not required for each tile type.
        self.functionality = False # May actually remove functionality in future, as it is redundant when I can just check the reader. Although its simpler to type this.
        self.usable = None # Used when a tile is a factory, refresh on turn end, disable when factory is used. Cannot be used when not captured.
        self.health = None # Enabled when functionality exists. It allows infantry to capture (Should be set to 20, subtract unit health from it when being captured. Revert when unit stops)
        self.color = color # When captured (if having functionality) changes what color it is based on capturing unit.

        # Start setting up functionality, tiles with functionality will bring in income and can be captured.
        reader = self.tile_id.split("#")
        if reader[0] not in tiletypes:
            raise Exception('Invalid tile type detected')
        if reader[0] in ["city", "factory"]:
            self.functionality = True
            self.health = 20 # If a tile has functionality, it can be captured. When it reaches 0, it will convert to the team color that captured it.

        # Will enable the usable variable if functionality exists and the tile is a factory
        if (self.functionality != False) and (reader[0] == "factory") and (self.color != None):
            self.usable = True

        # Sets movement costs
        self.move_cost["foot"] = tiletypes[reader[0]][2]
        self.move_cost["tires"] = tiletypes[reader[0]][3]
        self.move_cost["tread"] = tiletypes[reader[0]][4]
        self.defense = tiletypes[reader[0]][1]
        
def tileCR8(tile_id, tile_list, posx, posy, color=None, occupied=False):
    tile_reader = tile_id.split("#")
    if tile_reader[0] not in list(tiletypes.keys()):
        raise Exception("Error: Incompatible tile type attempted to be used")
    else:
        tile_list.append(TileObject(tile_id, posx, posy, color, occupied))