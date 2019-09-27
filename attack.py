#!/usr/bin/python3
# Austin McCowan
# 9/27/2019

'''Attack function'''

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