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
        # Efficiency will scale from 0 (can't damage) to 5 ( Max damage )
        unit.airEF = 0
        unit.heliEF = 0 
        unit.infEF = 0 
        unit.armorEF = 0
        if unit.title == "tank":
            unit.airEF = 0
            unit.heliEF = 2
            unit.armorEF = 3
            unit.infEF = 3 
        if unit.title == "infantry":
            unit.airEF = 0
            unit.heliEF = 1
            unit.armorEF = 1
            unit.infEF = 2
    # Will create a unit based on type, then will set a title to the unit based on the type and current iteration of that unit type.
    def unitCR8(self, title):
         pass
     
# attack function, can be used universally
if __name__ == "__main__":
    unit1 = unitObject(0, 0, 0, "tank", 0, 0, 0, 0)
    unit2 = unitObject(0, 0, 0, "infantry", 0, 0, 0, 0)
    
    ''' Will run multiple times until one unit is dead. After a unit is considered "dead", or if either unit has a health 
        of 0 or below, the attack function will simply just pass and not rerun all code''' 
    for i in range(20):
        ak.attack(unit1, unit2)
        ak.attack(unit2, unit1)
    