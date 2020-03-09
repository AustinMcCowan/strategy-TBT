#!/usr/bin/python3
# Austin McCowan
# 11/15/2019

# maintester file

import units as u
import attack as ak
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


# Hold and initialize starting information. 
class Data(object):
    red_list = []
    blue_list = []
    current = []
    other = []
    turn_decider = (5)
    team_announcer = ''
    def __init__(self):
        
        # Initial units to start with
        u.unitCR8("tank", Data.red_list)
        u.unitCR8("tank", Data.red_list)
        u.unitCR8("tank", Data.red_list)
        u.unitCR8("tank", Data.blue_list)
        u.unitCR8("tank", Data.blue_list)
        u.unitCR8("tank", Data.blue_list)      
        
        # Initial team setting
        if Data.turn_decider > 0:
            Data.team_announcer = "Red"
            Data.current = Data.red_list
            Data.other = Data.blue_list
            
        elif Data.turn_decider < 0:
            Data.team_announcer = "Blue"
            Data.current = Data.blue_list
            Data.other = Data.red_list
        else:
            raise Exception("How did you break this?")
        
    def delete_unit(unit_team):
        for i in range(len(unit_team)):
            if unit_team[i].health <= 0.5:
                print("--unit was destroyed--")
                unit_team.pop(i)
                break
            
    # Occurs before action and at start of program (Already done in __init__)        
    def temp_list_set():
        if Data.turn_decider > 0:
            Data.team_announcer = "Red"
            Data.current = Data.red_list
            Data.other = Data.blue_list
            
        elif Data.turn_decider < 0:
            Data.team_announcer = "Blue"
            Data.current = Data.blue_list
            Data.other = Data.red_list
        else:
            raise Exception("How did you break this?")
        
    # Occurs after action        
    def update_teams():
        if Data.turn_decider > 0:
            Data.red_list = Data.current
            Data.blue_list = Data.other
        elif Data.turn_decider < 0:
            Data.blue_list = Data.current
            Data.red_list = Data.other
        
        # Switches turn    
        Data.turn_decider = Data.turn_decider*(-1)
        # Deletes dead units
        Data.delete_unit(Data.red_list)
        Data.delete_unit(Data.blue_list)
        # Now that turn is changed, the temp lists do too.
        Data.temp_list_set()

# Subframe for attacking        
class VisualAttackFrame(tk.Frame):
    def __init__(self, parent, attack_list, defend_list):
        self.attack_list = attack_list
        self.defend_list = defend_list        
        tk.Frame.__init__(self, master=parent, bg="#CCC", highlightbackground = "blue", highlightthickness=1)
        
        self.lbl_attack = tk.Label(self, text="Unit Attacking:", bg="#CCC")
        self.lbl_attack.grid(row=0, column=0, columnspan=2, sticky='news')
        
        self.tkvar_attack = tk.StringVar(self)
        self.tkvar_attack.set(self.attack_list[0])
        self.drp_attack = tk.OptionMenu(self, self.tkvar_attack, *self.attack_list, bg="#CCC")
        self.drp_attack.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.lbl_defend = tk.Label(self, text="Unit Defending:", bg="#CCC")
        self.lbl_defend.grid(row=2, column=0, columnspan=2, sticky='news')
        
        self.tkvar_defend = tk.StringVar(self)
        self.tkvar_defend.set(self.defend_list[0])
        self.drp_defend = tk.OptionMenu(self, self.tkvar_defend, *self.defend_list, bg="#CCC")
        self.drp_defend.grid(row=3, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", bg="#CCC")
        self.btn_cancel.grid(row=4, column=0, sticky='news')
        
        self.btn_confirm = tk.Button(self, text="Confirm", bg="#CCC")
        self.btn_confirm.grid(row=4, column=1, sticky='news')
        
    def send_attack_order(self):
        # Grab data from frame and use it on attack_call
        first = ''
        
# Subframe for creating units
class VisualCreateFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)    

# GUI
class Visual(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_sampletext = tk.Label(self, text = ''' to attack, type 'attack' or 'a', to create a unit, type 'create' or 'c' ,
 to check the list of units, type 'list' or 'l', type 'q' to quit: ''', bg="#BBB")
        self.lbl_sampletext.grid(row=0,column=0, rowspan=3, sticky='news')
        
        starter_team_announce = "Current Team: " + Data.team_announcer
        self.lbl_current_team = tk.Label(self, text = starter_team_announce)
        self.lbl_current_team.grid(row=0, column=1, columnspan=2, padx=15)
        
        self.btn_attack = tk.Button(self, text="Attack", command = self.open_attack_frame)
        self.btn_attack.grid(row=1, column=1, sticky='news')
        
        self.btn_create = tk.Button(self, text="Create", command = self.create_call)
        self.btn_create.grid(row=2, column=1, sticky='news')
        
        self.btn_list = tk.Button(self, text="List", command = self.list_call)
        self.btn_list.grid(row=1, column=2, sticky='news')        
        
        self.btn_quit = tk.Button(self, text="Quit", command = self.quit_call)
        self.btn_quit.grid(row=2, column=2, sticky='news')
        
        self.scr_text = ScrolledText(self, heigh = 10, width=40)
        self.scr_text.grid(row=3, column=0, rowspan=2, sticky='news')
        
        self.information = ''
        
    def update(self):
        Data.update_teams()
        txt = "Current Team: " + Data.team_announcer
        self.lbl_current_team.configure(text = txt)  
        
    def open_attack_frame(self):
        temp_attack_list = []
        temp_defend_list = []
        
        for i in range(len(Data.current)):
            temp_attack_list.append(Data.current[i].title)
            
        for i in range(len(Data.other)):
            temp_defend_list.append(Data.other[i].title)
        
        self.frm_attack = VisualAttackFrame(self, temp_attack_list, temp_defend_list)
        self.frm_attack.grid(row=3, column=1, rowspan=2, columnspan=2, sticky='news')
        
    def attack_call(self, first, second):
        # attacking (Current turn team vs other)

        first_unit = None
        second_unit = None
        
        # sets indexes/what units attack/defend
        for i in range(len(Data.current)):
            if Data.current[i].title == first:
                first_unit = i
        for i in range(len(Data.other)):
            if Data.other[i].title == second:
                second_unit = i
                
        if first_unit == None or second_unit == None:
            print("Invalid Unit or Target")
        else:
            # This if statement still runs the attack code, but will force the turn to stay unchanged if an invalid attack was made
            result = ak.attack(Data.current[first_unit], Data.other[second_unit])
            self.scr_text.insert("insert", result[1])
            if result[0] == None:
                pass
            else:
                self.update()
        self.frm_attack.destroy()
         
    def create_call(self):
        try:
            produce = input("Type of unit to create: ")
            u.unitCR8(produce, Data.current)
            self.update()
            
        except:
            print("failed to create unit")        
            
    def list_call(self):
        print("\n=============")
        print("Red Team: ")            
        for unit in Data.red_list:
            print(unit.title, "| Health: ", unit.health)
        
        print("\nBlue Team: ")
        for unit in Data.blue_list:
            print(unit.title, "| Health: ", unit.health)
        print("=============")        
    
    def quit_call(self):
        root.destroy()
        
                
# Initialize stuff
root = tk.Tk()
root.title("maintester.py")
data_storage = Data()

frame_visual = Visual()
frame_visual.grid(row = 0, column = 0, sticky = "news")
frame_visual.tkraise()
root.mainloop()


# Archived 
'''
# Main Method
if __name__ == "__main__":
    print("\n TEST")
    print("Preset teams: Red and blue\n")    
    print("=============")
    print("Red Team: ")
    
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
            raise Exception("How did you break this?")
        
        frame_visual.update_team(team_announcer)
        
        # Stops tester if only one or less unit remains
        if len(red_list) <= 1 or len(blue_list) <= 1:
            print("--not enough units to continue test, ending test--")
            break
        
        # testing
        print("Current turn:", team_announcer)        
        '''
        
'''
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
'''