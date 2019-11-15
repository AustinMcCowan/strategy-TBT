#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
''' Unit design and control file '''

global unitnames # ONLY ACCEPTABLE TITLES. OTHER TITLES USED WILL RAISE ERROR/PROBLEM
unitnames = ["tank", "infantry", "recon", "antiair", "fighter", "attackheli"]

# object to represent unit
class UnitObject(object):
    # basic stats
    # Efficiency will scale from 0 (can't damage) to 10 ( Max damage )
    # May need to add more efficiencies :/ 
       
    def __init__(self, title):
        # Initializes base information
        self.damage = 0
        self.health = 10        
        self.atk = (self.health/10)*(self.damage)
        self.title = title
        
        # Stops invalid titles from being created through brute force (through the unitobject class itself)
        if title not in unitnames:
            raise Exception('invalid unit type attempted to be created')    
        
        # Initializes efficiencies 
        self.fighterEF = 0
        self.attackheliEF = 0 
        self.infantryEF = 0 
        self.tankEF = 0
        self.reconEF = 0
        self.antiairEF = 0
        
        # Efficiency will scale from 0 (can't damage) to 10 ( Max damage ), Balancing unit types.
        # Sets unit efficiencies automatically based on unit type/name
        reader = self.title.split("#")
        if reader[0] == "tank":
            self.fighterEF = 0
            self.attackheliEF = 2
            self.tankEF = 5
            self.infantryEF = 5
            self.reconEF = 6
            self.antiairEF = 5
        if reader[0] == "infantry":
            self.fighterEF = 0
            self.attackheliEF = 1
            self.tankEF = 1
            self.infantryEF = 3
            self.reconEF = 2
            self.antiairEF = 1
        if reader[0] == "recon":
            self.fighterEF = 0
            self.attackheliEF = 2
            self.tankEF = 1
            self.infantryEF = 5
            self.reconEF = 4
            self.antiairEF = 1
        if reader[0] == "antiair":
            self.fighterEF = 7
            self.attackheliEF = 9
            self.tankEF = 2
            self.infantryEF = 10
            self.reconEF = 7
            self.antiairEF = 5
        if reader[0] == "fighter":
            self.fighterEF = 6
            self.attackheliEF = 10
            self.tankEF = 0
            self.infantryEF = 0
            self.reconEF = 0
            self.antiairEF = 0
        if reader[0] == "attackheli":
            self.fighterEF = 1
            self.attackheliEF = 4
            self.tankEF = 6
            self.infantryEF = 5
            self.reconEF = 8
            self.antiairEF = 3
            
# Unit creation, and insertion into the unit list
def unitCR8(title, unit_list):
    if title not in unitnames:
        raise Exception('invalid unit type attempted to be created')
    elif len(unit_list) >= 49:
        return None
    else:
        name = title
        number = 1
        for i in range(50): # Uses 50 -> unit cap
            for i in range(len(unit_list)):
                namer = unit_list[i].title.split("#")
                namer[1] = int(namer[1])
                if namer[0] == title:
                    if namer[1] == number:
                        number += 1
        number = str(number)
        name = name + "#" + number
        unit_list.append(UnitObject(name))
    
     