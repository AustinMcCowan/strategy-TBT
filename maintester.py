#!/usr/bin/python3
# Austin McCowan
# 11/15/2019

# maintester file

import units as u
import attack as ak

global unit_list
unit_list = []
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
    
    # Builds a unit list (OLD)
    '''unit_list.append(UnitObject("tank#1"))
    unit_list.append(UnitObject("tank#2"))
    unit_list.append(UnitObject("tank#3"))
    unit_list.append(UnitObject("tank#4"))
    unit_list.append(UnitObject("tank#5"))'''
    u.unitCR8("tank", unit_list)
    u.unitCR8("tank", unit_list)
    u.unitCR8("tank", unit_list)
    u.unitCR8("tank", unit_list)
    u.unitCR8("tank", unit_list)
    u.unitCR8("tank", unit_list)
    
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

