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
    def __init__(unit, damage, health, atk, title, airEF, heliEF, armorEF, infEF):
        unit.damage = 1
        unit.health = 10
        unit.atk = (unit.health/10)*(unit.damage)
        unit.title = title
        # Efficiency will scale from 0 (can't damage) to 10 ( Max damage )
        # May need to add more efficiencies :/ 
        # May change later on to make unitCR8 autofill unit efficiencies instead of placing them here
        unit.airEF = 0
        unit.heliEF = 0 
        unit.infEF = 0 
        unit.armorEF = 0
        if unit.title == "tank":
            unit.airEF = 0
            unit.heliEF = 3
            unit.armorEF = 5
            unit.infEF = 4
        if unit.title == "infantry":
            unit.airEF = 0
            unit.heliEF = 1
            unit.armorEF = 1
            unit.infEF = 3
        if unit.title == "recon":
            unit.airEF = 0
            unit.heliEF = 3
            unit.armorEF = 2
            unit.infEF = 4
        if unit.title == "antiair":
            unit.airEF = 7
            unit.heliEF = 9
            unit.armorEF = 3
            unit.infEF = 8
        if unit.title == "fighter":
            unit.airEF = 7
            unit.heliEF = 10
            unit.armorEF = 0
            unit.infEF = 0
        if unit.title == "attackheli":
            unit.airEF = 3
            unit.heliEF = 6
            unit.armorEF = 6
            unit.infEF = 5
    # Will create a unit based on type, then will set a title to the unit based on the type and current iteration of that unit type.
    def unitCR8(self, title):
         pass
     
# Main Method
if __name__ == "__main__":
    # When unitCR8 is finished, units will be have all stats filled in automatically.
    unit1 = unitObject(0, 0, 0, "tank", 0, 0, 0, 0)
    unit2 = unitObject(0, 0, 0, "infantry", 0, 0, 0, 0)
    
    ''' Will run multiple times until one unit is dead. After a unit is considered "dead", or if either unit has a health 
        of 0 or below, the attack function will simply just pass and not rerun all code''' 
    for i in range(20):
        ak.attack(unit1, unit2)
        ak.attack(unit2, unit1)
    
