#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
'''Develop/brainstorm/test formula -- two entities with separate values, construct health and damage conditions
attacks are a scenario between two units, and will consist of multiple conditions. Both objects will have stats affected
based on the stats of the other. '''

import attack as ak

'''>>>ATTEMPT TO SEGMENT UNITS TO HAVE EFFICIENCY TO CERTAIN TYPES'''
# object to represent unit
class unitObject:
    # basic stats
    damage = 0
    health = 10
    atk = 0
    
    # Efficiency will scale from 0 (can't damage) to 10 ( Max damage )
    # May need to add more efficiencies :/ 
    
    airEF = 0
    heliEF = 0 
    infEF = 0 
    armorEF = 0    
    def __init__(unit, title): 
        unit.atk = (unit.health/10)*(unit.damage)
        unit.title = title
        
        # Efficiency will scale from 0 (can't damage) to 10 ( Max damage )
        reader = unit.title.split("#")
        if reader[0] == "tank":
            unit.airEF = 0
            unit.heliEF = 3
            unit.armorEF = 5
            unit.infEF = 4
        if reader[0] == "infantry":
            unit.airEF = 0
            unit.heliEF = 1
            unit.armorEF = 1
            unit.infEF = 3
        if reader[0] == "recon":
            unit.airEF = 0
            unit.heliEF = 3
            unit.armorEF = 2
            unit.infEF = 4
        if reader[0] == "antiair":
            unit.airEF = 7
            unit.heliEF = 9
            unit.armorEF = 3
            unit.infEF = 8
        if reader[0] == "fighter":
            unit.airEF = 7
            unit.heliEF = 10
            unit.armorEF = 0
            unit.infEF = 0
        if reader[0] == "attackheli":
            unit.airEF = 3
            unit.heliEF = 6
            unit.armorEF = 6
            unit.infEF = 5
     
# Main Method
if __name__ == "__main__":
    # Initial attack testing
    '''unit1 = unitObject("tank#1")
    unit2 = unitObject("infantry#2")'''
    
    ''' Will run multiple times until one unit is dead. After a unit is considered "dead", or if either unit has a health 
        of 0 or below, the attack function will simply just pass and not rerun all code''' 
    '''for i in range(20):
        ak.attack(unit1, unit2)
        ak.attack(unit2, unit1)
    '''
    print("\n LIST TEST")
    
    # Although built using old unit naming style, showcases how to delete unit.
    ''' >>>>> DELETING A UNIT: 
    unit_list = []
    for i in range(4):
        unit_list.append(unitObject(0,0,0,"tank", 0, 0, 0, 0))
    unit_list.append(unitObject(0,0,0,"infantry", 0, 0, 0, 0,))
    print(unit_list[2].title)
    
    for i in range(len(unit_list)):
        if unit_list[i].title == "infantry":
            unit_list.pop(i)
    print(unit_list[4].title)'''
    
    # Builds a unit list
    unit_list = []
    unit_list.append(unitObject("tank#1"))
    unit_list.append(unitObject("tank#2"))
    unit_list.append(unitObject("tank#3"))
    unit_list.append(unitObject("tank#4"))
    unit_list.append(unitObject("tank#5"))
    # Unit creation, and insertion into the unit list
    name = "tank"
    number = 1
    for i in range(50): # Uses 50 -> unit cap
        for i in range(len(unit_list)):
            namer = unit_list[i].title.split("#")
            namer[1] = int(namer[1])
            if namer[0] == "tank":
                if namer[1] == number:
                    number += 1
    number = str(number)
    name = name + "#" + number
    unit_list.append(unitObject(name))
    
    for i in range(len(unit_list)):
        print(unit_list[i].title)  
        
    while True:
        # Check if unit has reached or went under 0 to end loop
        breakout = False
        for unit in unit_list:
            if unit.health <= 0:
                print("--unit was destroyed--\n--ending test--")
                breakout = True
        if breakout != False:
            break
        
        # attacking     
        call = input("TEST attack: a = tank1 > tank2 | b = tank 2 > tank 1 | anything else to quit: ")
        if call == "a":
            ak.attack(unit_list[0], unit_list[1])
        elif call == "b":
            ak.attack(unit_list[1], unit_list[0])
        else:
            print("\nDONE")
            break     

 