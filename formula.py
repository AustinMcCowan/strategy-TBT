#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
'''Develop/brainstorm/test formula -- two entities with separate values, construct health and damage conditions
attacks are a scenario between two units, and will consist of multiple conditions. Both objects will have stats affected
based on the stats of the other. '''

# object to represent unit
class unitObject:
    # basic stats
    def __init__(unit, damage, health, atk, title):
        unit.damage = damage #Base damage. Will later change to be adjusted when implementing unit types.
        unit.health = 10
        unit.atk = (unit.health/10)*(unit.damage)
        unit.title = title #string, unit name.
# build attack initiate
def attack(self, target):
    print(target.title, "Health: ", target.title, "damage: ", target.atk)
    print(self.title, "Health: ", self.health, self.title, "damage: ", self.atk)
    print("Unit1 attack unit2")        
    target.health = (target.health - self.atk)
    # If the target unit survives, it counterattacks
    if target.health > 0:
        target.atk = (target.health/10)*(target.damage)
        print("Unit2 Health: ", target.health, "Unit2 damage: ", target.atk)
        print("Unit2 counterattacks unit1")
        self.health = (self.health - target.atk)
        # if the attacking unit doesn't survive the counterattack, it is instead destroyed
        if self.health > 0:
            self.atk = (self.health/10)*(self.damage)
            print("Unit1 Health: ", self.health, "Unit1 damage: ", self.atk)
            print("=========")
        else:
            print("Counterattack was lethal, Attacking unit destroyed")
            print("=========")
            del self            
    else:
        print("Attacked Unit was destroyed")
        print("=========")
        del target
            
# tester units, first value = attack value
unit1 = unitObject(5.0, 0, 0, "blue")
unit2 = unitObject(5.0, 0, 0, "red")

# attack function, can be used universally; IMPORTANT
attack(unit1, unit2)
attack(unit2, unit1)
attack(unit1, unit2)

# Formatted attack with status confirmation
'''print("Unit2 Health: ", unit2.health, "Unit2 damage: ", unit2.atk)
print("Unit1 Health: ", unit1.health, "Unit1 damage: ", unit1.atk)
print("Unit1 attack unit2")
unit2.health = (unit2.health - unit1.atk)
print("Unit2 Health: ", unit2.health, "Unit2 damage: ", unit2.atk)

if unit2.health > 0:
    unit2.atk = (unit2.health/10)*(unit2.damage)
    print("Unit2 Health: ", unit2.health, "Unit2 damage: ", unit2.atk)
    print("Unit2 counter unit1")
    unit1.health = (unit1.health - unit2.atk)
    print("Unit1 Health: ", unit1.health, "Unit1 damage: ", unit1.atk)
    unit1.atk = (unit1.health/10)*(unit1.damage)
    print("Unit1 Health: ", unit1.health, "Unit1 damage: ", unit1.atk)
else:
    print("Attacked Unit dead")
    del unit2 '''
