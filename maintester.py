#!/usr/bin/python3
# Austin McCowan
# 11/15/2019

# maintester file

import units as u
import attack as ak
import tkinter as tk

global red_list
global blue_list
red_list = []
blue_list = []

def delete_unit(unit_team):
    for i in range(len(unit_team)):
        if unit_team[i].health <= 0.5:
            print("--unit was destroyed--")
            unit_team.pop(i)
            break    


# Main Method
if __name__ == "__main__":
    print("\n TEST")
    print("Preset teams: Red and blue\n")
    u.unitCR8("tank", red_list)
    u.unitCR8("tank", red_list)
    u.unitCR8("tank", red_list)
    u.unitCR8("tank", blue_list)
    u.unitCR8("tank", blue_list)
    u.unitCR8("tank", blue_list)
    turn_decider = (5)
    global current
    global other
    current = red_list
    other = red_list
    
    print("=============")
    print("Red Team: ")
    for i in range(len(red_list)):
        print(red_list[i].title)
    print("\nBlue Team: ")
    for i in range(len(blue_list)):
        print(blue_list[i].title)
    print("=============")
    
    while True:
        print("")
        # Check if unit has reached or went under 0 to be deleted
        delete_unit(red_list)
        delete_unit(blue_list)
        if turn_decider > 0:
            team_announcer = "Red"
            current = red_list
            other = blue_list
        elif turn_decider < 0:
            team_announcer = "Blue"
            current = blue_list
            other = red_list
        else:
            raise Exception("How did you break this")
        
        
        # Stops tester if only one or less unit remains
        if len(red_list) <= 1 or len(blue_list) <= 1:
            print("--not enough units to continue test, ending test--")
            break
        
        # testing
        print("Current turn:", team_announcer)        
        call = input('''| to attack, type 'attack' or 'a' | to create a unit, type 'create' or 'c' |
| to check the list of units, type 'list' or 'l' | type 'q' to quit: ''')
        
        # attacking (Current turn team vs other)
        if call == "attack" or call == "a":
            first = input("Attacking unit: ")
            second = input("Defending unit: ")
            first_unit = None
            second_unit = None
            
            # sets indexes/what units attack/defend
            for i in range(len(current)):
                if current[i].title == first:
                    first_unit = i
            for i in range(len(other)):
                if other[i].title == second:
                    second_unit = i
                    
            if first_unit == None or second_unit == None:
                print("Invalid Unit or Target")
                continue
            else:
                # This if statement still runs the attack code, but will force the turn to stay unchanged if an invalid attack was made
                if ak.attack(current[first_unit], other[second_unit]) == None:
                    continue
                
        # creating   
        elif call == "create" or call == "c":
            try:
                produce = input("Type of unit to create: ")
                u.unitCR8(produce, current)
            except:
                print("failed to create unit")
            
        # check list of units    
        elif call == "list" or call == "l":
            print("\n=============")
            print("Red Team: ")            
            for unit in red_list:
                print(unit.title, "| Health: ", unit.health)
            
            print("\nBlue Team: ")
            for unit in blue_list:
                print(unit.title, "| Health: ", unit.health)
            print("=============")
            continue
        
        # End test
        elif call == "q":
            print("\nDONE")
            break
        else:
            continue
        
        if turn_decider > 0:
            red_list = current
            blue_list = other
        elif turn_decider < 0:
            blue_list = current
            red_list = other
            
        turn_decider = turn_decider*(-1)
        

