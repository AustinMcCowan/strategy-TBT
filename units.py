#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
''' Unit design and control file '''

global unitnames
global unit_move_limits # ONLY ACCEPTABLE TITLES. OTHER TITLES USED WILL RAISE ERROR/PROBLEM
'''Make these two separate lists because its easier to loop through. Also not that difficult to assign values, just grab index'''
unitnames = ["tank", "infantry", "recon", "antiair", "fighter", "attackheli"]
unit_move_limits = [5, 3, 7, 5, 10, 8]
# object to represent unit
class UnitObject(object):
    # available refers to a unit being able to attack, and movable refers to a unit being able to move.
    # When a unit moves, movable is set to false. When a unit attacks, available and movable is set to false
    def __init__(self, title, health=10, pos_x = 0, pos_y = 0, color="", available = False, move_limit = 0, movable = True, move_type = None):
        # Initializes base information
        self.damage = 0
        self.health = health       
        self.atk = (self.health/10)*(self.damage)
        self.title = title
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.available = available
        self.move_limit = move_limit
        self.movable = movable
        self.move_type = None
        # Initializes efficiencies 
        self.fighterEF = 0
        self.attackheliEF = 0 
        self.infantryEF = 0 
        self.tankEF = 0
        self.reconEF = 0
        self.antiairEF = 0
        
        # Efficiency will scale from 0 (can't damage) to 10 ( Max damage ); Balancing unit types.
        # Sets unit efficiencies automatically based on unit type/name
        reader = self.title.split("#")
        
        # Stops invalid titles from being created through brute force; fixes error where unit created fully formatted would raise an error
        if reader[0] not in unitnames:
            raise Exception('invalid unit type attempted to be created')
        
        if reader[0] == "tank":
            self.fighterEF = 0
            self.attackheliEF = 2
            self.tankEF = 5
            self.infantryEF = 5
            self.reconEF = 6
            self.antiairEF = 5
        elif reader[0] == "infantry":
            self.fighterEF = 0
            self.attackheliEF = 1
            self.tankEF = 1
            self.infantryEF = 3
            self.reconEF = 2
            self.antiairEF = 1
        elif reader[0] == "recon":
            self.fighterEF = 0
            self.attackheliEF = 2
            self.tankEF = 1
            self.infantryEF = 5
            self.reconEF = 4
            self.antiairEF = 1
        elif reader[0] == "antiair":
            self.fighterEF = 7
            self.attackheliEF = 9
            self.tankEF = 2
            self.infantryEF = 10
            self.reconEF = 7
            self.antiairEF = 5
        elif reader[0] == "fighter":
            self.fighterEF = 6
            self.attackheliEF = 10
            self.tankEF = 0
            self.infantryEF = 0
            self.reconEF = 0
            self.antiairEF = 0
        elif reader[0] == "attackheli":
            self.fighterEF = 1
            self.attackheliEF = 4
            self.tankEF = 6
            self.infantryEF = 5
            self.reconEF = 8
            self.antiairEF = 3

        # Initialize Move type:
        if reader[0] in ("infantry"):
            self.move_type = "foot"

        elif reader[0] in ("recon"):
            self.move_type = "tires"

        elif reader[0] in ("tank", "antiair"):
            self.move_type = "tread"
        
        elif reader[0] in ("fighter", "attackheli"):
            self.move_type = "air"

# Unit creation and insertion into the given unit list. WILL ONLY WORK WITH A LIST
def unitCR8(title, unit_list, team="", usable=False, posx=0, posy=0, movable = False):   
    if title not in unitnames:
        raise Exception('invalid unit type attempted to be created')
    elif len(unit_list) >= 50: # Unit cap is 50. 
        print("Unit cap reached")
        return None         
    else:
        distance = unit_move_limits[unitnames.index(title)]
        name = title
        number = 1
        
        '''Cycles through the team list chosen, and finds units that share the same type, and increases that units number 
        if it is shared with another unit of the same type. The reason it loops 50 times is due to 2 reasons: The unit cap is 50.
        And the fact that a unit could have a higher number than a unit farther in the list (which means this loop needs to
        loop again to see if the new number is equal to that units number).'''  
        for i in range(50): # Uses 50 -> unit cap
            for i in range(len(unit_list)):
                namer = unit_list[i].title.split("#")
                namer[1] = int(namer[1])
                if namer[0] == title:
                    if namer[1] == number:
                        number += 1
        number = str(number)
        name = name + "#" + number
        unit_list.append(UnitObject(name, color=team, available=usable, move_limit=distance, pos_x=posx, pos_y=posy, movable=movable))
    
     