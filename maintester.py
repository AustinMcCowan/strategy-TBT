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
    
    print("\n TEST")
    
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
            if unit_list[i].health <= 0.5:
                print("--unit was destroyed--\n--ending test--")
                breakout = True
                
        position = (-1)
        for unit in unit_list:
            position += 1
            if unit.health <= 0.5: # If units health drops equals or drops below .5, they are considered destroyed.
                unit_list.pop(position)
                position = (-1)
                continue
            
            
        
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

