#!/usr/bin/python3
# Austin McCowan
# 9/6/2019
'''Develop/brainstorm/test formula -- two entities with separate values, construct health and damage conditions
attacks are a scenario between two units, and will consist of multiple conditions. Both objects will have stats affected
based on the stats of the other. '''

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
     
     
# build attack initiate
def attack(self, target):
    # CATEGORIZING DAMAGE EFFICIENCY BETWEEN UNITS      
    if target.health <= 0:
        pass
    elif self.health <= 0:
        pass
    else:
        if self.title == "tank":
            if target.title == "infantry":
                self.damage = self.infEF
                target.damage = target.armorEF
                self.atk = (self.health/10)*(self.damage)
                self.atk = round(self.atk, 2)
                target.atk = (target.health/10)*(target.damage)
                target.atk = round(target.atk, 2)
            elif target.title == "tank":
                self.damage = self.armorEF
                target.damage = target.armorEF
                self.atk = (self.health/10)*(self.damage)
                self.atk = round(self.atk, 2)
                target.atk = (target.health/10)*(target.damage)
                target.atk = round(target.atk, 2)
            else:
                pass
        if self.title == "infantry":
            if target.title == "infantry":
                self.damage = self.infEF
                target.damage = target.infEF               
                self.atk = (self.health/10)*(self.damage)
                self.atk = round(self.atk, 2)                
                target.atk = (target.health/10)*(target.damage)
                target.atk = round(target.atk, 2)
            elif target.title == "tank":
                self.damage = self.armorEF
                target.damage = target.infEF              
                self.atk = (self.health/10)*(self.damage)
                self.atk = round(self.atk, 2)              
                target.atk = (target.health/10)*(target.damage)
                target.atk = round(target.atk, 2)
            else:
                pass        
        # print/return will change later on
        # stats starting:
        print(self.title, "Health:", self.health, "|", self.title, "damage:", self.atk)
        print(target.title, "Health:", target.health,"|", target.title, "damage:", target.atk)
        print(self.title, "attacks", target.title)
        # Actual attack and target unit getting stats adjusted
        target.health = (target.health - self.atk)
        target.health = round(target.health, 2)
        target.atk = (target.health/10)*(target.damage)
        target.atk = round(target.atk, 2)
        # If the target unit survives, it counterattacks
        if target.health > 0:
            target.atk = (target.health/10)*(target.damage)
            target.atk = round(target.atk, 2)
            print(target.title, "Health:", target.health,"|", target.title, "damage:", target.atk)
            print(target.title, "counterattacks", self.title)
            self.health = (self.health - target.atk)
            self.health = round(self.health, 2)
            self.atk = (self.health/10)*(self.damage)
            self.atk = round(self.atk, 2)
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
            
# attack function, can be used universally
if __name__ == "__main__":
    unit1 = unitObject(0, 0, 0, "tank", 0, 0, 0, 0)
    unit2 = unitObject(0, 0, 0, "infantry", 0, 0, 0, 0)
    for i in range(20):
        attack(unit1, unit2)
        attack(unit2, unit1)
    
