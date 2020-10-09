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
        # Since units created are forced to abide by list of names created, should work fine.
        # Set the target damage
        if selfreader[0] == "tank":
            target.damage = target.tankEF
        
        elif selfreader[0] == "infantry":
            target.damage = target.infantryEF
            
        elif selfreader[0] == "recon":
            target.damage = target.reconEF
        
        elif selfreader[0] == "antiair":
            target.damage = target.antiairEF
            
        elif selfreader[0] == "fighter":
            target.damage = target.fighterEF
        
        elif selfreader[0] == "attackheli":
            target.damage = target.attackheliEF
        
        else:
            pass
        
        # Set self damage
        if targetreader[0] == "tank":
            self.damage = self.tankEF
            
        elif targetreader[0] == "infantry":
            self.damage = self.infantryEF
        
        elif targetreader[0] == "recon":
            self.damage = self.reconEF
        
        elif targetreader[0] == "antiair":
            self.damage = self.antiairEF
        
        elif targetreader[0] == "fighter":
            self.damage = self.fighterEF
            
        elif targetreader[0] == "attackheli":
            self.damage = self.attackheliEF
        
        else:
            pass
        
        
        # Sets up attack values
        self.atk = (self.health/10)*(self.damage)
        self.atk = round(self.atk, 2)
        target.atk = (target.health/10)*(target.damage)
        target.atk = round(target.atk, 2)        
        
        msg = ''
        # Stops attack if the user has made an invalid attack
        if self.damage == 0:
            msg = "invalid attack; this unit cannot attack the defending unit"
            return (None, msg)
        
        # This should almost never occur in finished product due to unavailable units being removed from being selectable in current turn
        if self.available == False:
            msg = "invalid command; this unit has already been used"
            return (None, msg)
        
        # ACTUAL ENCOUNTER:
        # status of the two units:  
        msg += self.color + " " + str(self.title) + " Health: " + str(self.health) + " | " + self.color + " " + str(self.title) + " damage: " + str(self.atk) + "\n"
        msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " damage: " + str(target.atk) + "\n"
        msg += self.color + " " + str(self.title) + " attacks " + target.color + " " + str(target.title) + "\n"
        
        # Attacking unit deals damage to defending unit
        target.health = (target.health - self.atk)
        target.health = round(target.health, 2)
        target.atk = (target.health/10)*(target.damage)*(.77) # balance counter attacks
        target.atk = round(target.atk, 2)
        
        # If the target unit survives, it counterattacks.
        if target.health > 0.5 and target.damage != 0:
            msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " counterdamage: " + str(target.atk) + "\n"
            msg += target.color + " " + str(target.title) + " counterattacks " + self.color + " " + str(self.title) + "\n"
            self.health = (self.health - target.atk)
            self.health = round(self.health, 2)
            self.atk = (self.health/10)*(self.damage)
            self.atk = round(self.atk, 2)
            # if the attacking unit doesn't survive the counterattack, it is instead destroyed (in main program)
            if self.health > 0.5:
                msg += self.color + " " + str(self.title) + " Health: " + str(self.health) + " | " + self.color + " " + str(self.title) + " damage: " + str(self.atk) + "\n"
                msg += "ENDSCENARIO========="+"\n"
            else:
                msg += "Counterattack was lethal, " + self.color + " " + str(self.title) + " destroyed " + "\n"
                msg += "ENDSCENARIO========="+"\n"
            
        elif target.damage == 0 and target.health > .5:
            msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " counterdamage: " + str(target.atk) + "\n"
            msg += target.color + " " + str(target.title) + " cannot counter attack " + "\n"
            msg += "ENDSCENARIO=========" + "\n"
            
        else:
            msg += target.color + " " + str(target.title) + "was destroyed" + "\n"
            msg += "ENDSCENARIO=========" + "\n"
            
        self.available = False
        return (True, msg)