#!/usr/bin/python3
# Austin McCowan
# 9/27/2019

'''Attack function'''

# build attack initiate
def attack(conscript, target):
    # CATEGORIZING DAMAGE EFFICIENCY BETWEEN UNITS 
    # conscriptreader[0] , targetreader[0]
    conscriptreader = conscript.title.split("#")
    targetreader = target.title.split("#")
    if target.health <= 0.5:
        pass
    elif conscript.health <= 0.5:
        pass
    else:
        # Since units created are forced to abide by list of names created, should work fine.
        # Set the target damage
        counter_modifier = 1.00 # Set this as a variable, as some units may punch back differently (and could be used for indirect units)
        if conscriptreader[0] == "tank":
            target.damage = target.tankEF
        
        elif conscriptreader[0] == "infantry":
            target.damage = target.infantryEF
            
        elif conscriptreader[0] == "recon":
            target.damage = target.reconEF
        
        elif conscriptreader[0] == "antiair":
            target.damage = target.antiairEF
            
        elif conscriptreader[0] == "fighter":
            target.damage = target.fighterEF
        
        elif conscriptreader[0] == "attackheli":
            target.damage = target.attackheliEF
        
        else:
            pass
        
        # Set conscript damage
        if targetreader[0] == "tank":
            conscript.damage = conscript.tankEF
            
        elif targetreader[0] == "infantry":
            conscript.damage = conscript.infantryEF
        
        elif targetreader[0] == "recon":
            conscript.damage = conscript.reconEF
        
        elif targetreader[0] == "antiair":
            conscript.damage = conscript.antiairEF
        
        elif targetreader[0] == "fighter":
            conscript.damage = conscript.fighterEF
            
        elif targetreader[0] == "attackheli":
            conscript.damage = conscript.attackheliEF
        
        else:
            pass
        
        
        # Sets up attack values
        conscript.atk = (conscript.health/10)*(conscript.damage)
        conscript.atk = round(conscript.atk, 2)
        target.atk = (target.health/10)*(target.damage)
        target.atk = round(target.atk, 2)        
        
        msg = ''
        # Stops attack if the user has made an invalid attack
        if conscript.damage == 0:
            msg = "invalid attack; this unit cannot attack the defending unit"
            return (None, msg)
        
        # This should almost never occur in finished product due to unavailable units being removed from being selectable in current turn
        if conscript.available == False:
            msg = "invalid command; this unit has already been used"
            return (None, msg)
        
        # ACTUAL ENCOUNTER:
        # status of the two units:  
        msg += conscript.color + " " + str(conscript.title) + " Health: " + str(conscript.health) + " | " + conscript.color + " " + str(conscript.title) + " damage: " + str(conscript.atk) + "\n"
        msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " damage: " + str(target.atk) + "\n"
        msg += conscript.color + " " + str(conscript.title) + " attacks " + target.color + " " + str(target.title) + "\n"
        
        # Attacking unit deals damage to defending unit
        target.health = (target.health - conscript.atk)
        target.health = round(target.health, 2)
        target.atk = (target.health/10)*(target.damage)*(counter_modifier) # balance counter attacks
        target.atk = round(target.atk, 2)
        
        # If the target unit survives, it counterattacks.
        if target.health > 0.5 and target.damage != 0:
            msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " counterdamage: " + str(target.atk) + "\n"
            msg += target.color + " " + str(target.title) + " counterattacks " + conscript.color + " " + str(conscript.title) + "\n"
            conscript.health = (conscript.health - target.atk)
            conscript.health = round(conscript.health, 2)
            conscript.atk = (conscript.health/10)*(conscript.damage)
            conscript.atk = round(conscript.atk, 2)
            # if the attacking unit doesn't survive the counterattack, it is instead destroyed (in main program)
            if conscript.health > 0.5:
                msg += conscript.color + " " + str(conscript.title) + " Health: " + str(conscript.health) + " | " + conscript.color + " " + str(conscript.title) + " damage: " + str(conscript.atk) + "\n"
                msg += "ENDSCENARIO========="+"\n"
            else:
                msg += "Counterattack was lethal, " + conscript.color + " " + str(conscript.title) + " destroyed " + "\n"
                msg += "ENDSCENARIO========="+"\n"
            
        elif target.damage == 0 and target.health > .5:
            msg += target.color + " " + str(target.title) + " Health: " + str(target.health) + " | " + target.color + " " + str(target.title) + " counterdamage: " + str(target.atk) + "\n"
            msg += target.color + " " + str(target.title) + " cannot counter attack " + "\n"
            msg += "ENDSCENARIO=========" + "\n"
            
        else:
            msg += target.color + " " + str(target.title) + "was destroyed" + "\n"
            msg += "ENDSCENARIO=========" + "\n"
            
        conscript.available = False
        return (True, msg)