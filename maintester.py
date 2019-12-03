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
        # Check if unit has reached or went under 0 to be deleted
        delete_list = []
        for i in range(len(unit_list)):
            if unit_list[i].health <= 0.5:
                print("--unit was destroyed--")
                delete = i
                break
        unit_list.pop(delete)
            
        # Stops tester if only one or less unit remains
        if len(unit_list) <= 1:
            print("--not enough units to continue test, ending test--")
            break
            
        # testing 
        call = input('''TEST | to attack, type 'attack' or 'a' | to create a unit, type 'create' or 'c' |\n| to check the list of units, type 'list' or 'l' | type anything else to quit: ''')
        
        # attacking
        if call == "attack" or call == "a":
            first = input("Attacking unit: ")
            second = input("Defending unit: ")
            first_unit = 0
            second_unit = 0
            
            # sets indexes/what units attack/defend
            for i in range(len(unit_list)):
                if unit_list[i].title == first:
                    first_unit = i
                if unit_list[i].title == second:
                    second_unit = i           
            ak.attack(unit_list[first_unit], unit_list[second_unit])
            
        # creating   
        elif call == "create" or call == "c":
            produce = input("Type of unit to create: ")
            u.unitCR8(produce, unit_list)
            
        # check list of units    
        elif call == "list" or call == "l":
            for unit in unit_list:
                print(unit.title)
                
        # End test
        else:
            print("\nDONE")
            break

