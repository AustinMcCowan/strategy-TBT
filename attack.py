#!/usr/bin/python3
# Austin McCowan
# 9/27/2019

'''Attack function'''

# build attack initiate
def attack(self, target):
    # CATEGORIZING DAMAGE EFFICIENCY BETWEEN UNITS 
    # selfreader[0] , targetreader[0]
    selfreader = self.title.split("#")
    targetreader = target.title.split("#")
    if target.health <= 0.5:
        pass
    elif self.health <= 0.5:
        pass
    else:
        '''have to add all unit types to this :/ Based on amount of unit types, will exponentially increase: 2 types = 2x2, 3 types = 3...
        so 9 types of units will force me to have to create 81 sections...'''
        # Since units created are forced to abide by list of names created, should work fine. 
        if selfreader[0] == "tank":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.tankEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.tankEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.tankEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.tankEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.tankEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.tankEF
                            
            else:
                pass
            
        if selfreader[0] == "infantry":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.infantryEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.infantryEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.infantryEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.infantryEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.infantryEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.infantryEF
                            
            else:
                pass
           
        if selfreader[0] == "recon":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.reconEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.reconEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.reconEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.reconEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.reconEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.reconEF
                            
            else:
                pass
        
        if selfreader[0] == "antiair":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.antiairEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.antiairEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.antiairEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.antiairEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.antiairEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.antiairEF
                            
            else:
                pass
        
        if selfreader[0] == "fighter":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.fighterEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.fighterEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.fighterEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.fighterEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.fighterEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.fighterEF
                            
            else:
                pass
        
        if selfreader[0] == "attackheli":
            if targetreader[0] == "infantry":
                self.damage = self.infantryEF
                target.damage = target.attackheliEF
                
            elif targetreader[0] == "tank":
                self.damage = self.tankEF
                target.damage = target.attackheliEF
                
            elif targetreader[0] == "recon":
                self.damage = self.reconEF
                target.damage = target.attackheliEF
                 
            elif targetreader[0] == "antiair":
                self.damage = self.antiairEF
                target.damage = target.attackheliEF
                
            elif targetreader[0] == "fighter":
                self.damage = self.fighterEF
                target.damage = target.attackheliEF
                
            elif targetreader[0] == "attackheli":
                self.damage = self.attackheliEF
                target.damage = target.attackheliEF
                            
            else:
                pass
            
        
        
        # Sets up attack values
        self.atk = (self.health/10)*(self.damage)
        self.atk = round(self.atk, 2)
        target.atk = (target.health/10)*(target.damage)
        target.atk = round(target.atk, 2)        
        
        # Stops attack if the user has made an invalid attack
        if self.damage == 0:
            print("invalid attack; this unit cannot attack the defending unit")
            return None
        
        # ACTUAL ENCOUNTER:
        # status of the two units:  
        print(self.title, "Health:", self.health, "|", self.title, "damage:", self.atk)
        print(target.title, "Health:", target.health,"|", target.title, "damage:", target.atk)
        print(self.title, "attacks", target.title)
        
        # Attacking unit deals damage to defending unit
        target.health = (target.health - self.atk)
        target.health = round(target.health, 2)
        target.atk = (target.health/10)*(target.damage)*(.77) # balance counter attacks
        target.atk = round(target.atk, 2)
        
        # If the target unit survives, it counterattacks.
        if target.health > 0.5 and target.damage != 0:
            print(target.title, "Health:", target.health,"|", target.title, "counterdamage:", target.atk)
            print(target.title, "counterattacks", self.title)
            self.health = (self.health - target.atk)
            self.health = round(self.health, 2)
            self.atk = (self.health/10)*(self.damage)
            self.atk = round(self.atk, 2)
            # if the attacking unit doesn't survive the counterattack, it is instead destroyed (in main program)
            if self.health > 0.5:
                print(self.title, "Health:", self.health, "|", self.title, "damage:", self.atk)
                print("ENDSCENARIO=========")
            else:
                print("Counterattack was lethal,", self.title, "destroyed")
                print("ENDSCENARIO=========")
        elif target.damage == 0 and target.health > .5:
            print(target.title, "Health:", target.health,"|", target.title, "counterdamage:", target.atk)
            print(target.title, "cannot counter attack")
            print("ENDSCENARIO=========")
        else:
            print(target.title, "was destroyed")
            print("ENDSCENARIO=========")