#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
'''Develop/brainstorm/test formula -- two entities with separate values, construct health and damage conditions
attacks are a scenario between two units, and will consist of multiple conditions. Both objects will have stats affected
based on the stats of the other. '''

import attack as ak

global unitnames
global unit_list

'''>>>ATTEMPT TO SEGMENT UNITS TO HAVE EFFICIENCY TO CERTAIN TYPES'''
# object to represent unit
class UnitObject(object):
    # basic stats
    # Efficiency will scale from 0 (can't damage) to 10 ( Max damage )
    # May need to add more efficiencies :/ 
       
    def __init__(self, title):
        self.damage = 0
        self.health = 10        
        self.atk = (self.health/10)*(self.damage)
        self.title = title
        
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
            self.tankEF = 4
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
def unitCR8(title):
    if title not in unitnames:
        print("Error: Invalid unit type")
        return None
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

unit_list = []    
unitnames = ["tank", "infantry", "recon", "antiair", "fighter", "attackheli"]

# Main Method
if __name__ == "__main__":
    # Initial attack testing
    '''unit1 = UnitObject("tank#1")
    unit2 = UnitObject("infantry#2")'''
    
    ''' Will run multiple times until one unit is dead. After a unit is considered "dead", or if either unit has a health 
        of 0 or below, the attack function will simply just pass and not rerun all code''' 
    '''for i in range(20):
        ak.attack(unit1, unit2)
        ak.attack(unit2, unit1)
    '''
    print("\n LIST TEST")
    
    # Although built using old unit naming style, showcases how to delete unit.
    # Plan to create another function that is for deleting units, eventually all of this (unit creating, unit list, etc) will spin together
    ''' >>>>> DELETING A UNIT: 
    unit_list = []
    for i in range(4):
        unit_list.append(UnitObject(0,0,0,"tank", 0, 0, 0, 0))
    unit_list.append(UnitObject(0,0,0,"infantry", 0, 0, 0, 0,))
    print(unit_list[2].title)
    
    for i in range(len(unit_list)):
        if unit_list[i].title == "infantry":
            unit_list.pop(i)
    print(unit_list[4].title)'''
    
    # Builds a unit list
    '''unit_list.append(UnitObject("tank#1"))
    unit_list.append(UnitObject("tank#2"))
    unit_list.append(UnitObject("tank#3"))
    unit_list.append(UnitObject("tank#4"))
    unit_list.append(UnitObject("tank#5"))'''
    unitCR8("tank")
    unitCR8("tank")
    unitCR8("tank")
    unitCR8("tank")
    unitCR8("tank")
    unitCR8("tank")
    
    
    for i in range(len(unit_list)):
        print(unit_list[i].title)  
        
    while True:
        # Check if unit has reached or went under 0 to end loop
        breakout = False
        for i in range(len(unit_list)):
            if unit_list[i].health <= 0:
                print("--unit was destroyed--\n--ending test--")
                breakout = True
                
        position = 0
        for unit in unit_list:
            if unit.health <= 0.5: # If units health drops equals or drops below .5, they are considered destroyed.
                unit_list.pop(position)
            position += 1
            
        
        if breakout != False:
            break
                
        # attacking     
        call = input("TEST attack: a = tank1 > tank2 | b = tank2 > tank1 | type anything else to quit: ")
        if call == "a":
            ak.attack(unit_list[0], unit_list[1])
        elif call == "b":
            ak.attack(unit_list[1], unit_list[0])
        else:
            print("\nDONE")
            break
        
    for unit in unit_list:
        print(unit.title)

 