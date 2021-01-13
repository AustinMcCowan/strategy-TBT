#!/usr/bin/python3
# Austin McCowan
# 12/11/2020
''' Tile design and control file '''

''' Use a dictionary to link information about a tile type to the tiles themselves, i.e just find the key (tile name), and
then find the index of the piece of information and done. Since all tile types will share the same format/order of information in their
lists, this should not create problems.
'''
# Information may include: functionality, defense rating, movement cost...
tiletypes = {
    "grass":[], 
    "road":[], 
    "factory":[],
    "water":[],
    "mountain":[],
    "city":[]
}

class TileObject(object):
    
    def __init__(self, tile_id, move_cost):
        pass