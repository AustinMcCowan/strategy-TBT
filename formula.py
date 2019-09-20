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
    # print/return will change later on
    print(target.title, "Health:", target.health,"|", target.title, "damage:", target.atk)
    print(self.title, "Health:", self.health, "|", self.title, "damage:", self.atk)
    print(self.title, "attack", target.title)        
    target.health = (target.health - self.atk)
    target.atk = (target.health/10)*(target.damage)
    # If the target unit survives, it counterattacks
    if target.health > 0:
        target.atk = (target.health/10)*(target.damage)
        print(target.title, "Health:", target.health,"|", target.title, "damage:", target.atk)
        print(target.title, "counterattacks", self.title)
        self.health = (self.health - target.atk)
        self.atk = (self.health/10)*(self.damage)
        # if the attacking unit doesn't survive the counterattack, it is instead destroyed
        if self.health > 0:
            print(self.title, "Health:", self.health, "|", self.title, "damage:", self.atk)
            print("ENDSCENARIO=========")
        else:
            print("Counterattack was lethal,", self.title, "destroyed")
            print("ENDSCENARIO=========")
            del self        
    else:
        print(target.title, "was destroyed")
        print("ENDSCENARIO=========")
        del target
            
# tester units, first value = attack value
unit1 = unitObject(5.0, 0, 0, "blue")

unit2 = unitObject(5.0, 0, 0, "red")


# attack function, can be used universally
attack(unit1, unit2)
attack(unit2, unit1)
attack(unit1, unit2)
attack(unit2, unit1)
