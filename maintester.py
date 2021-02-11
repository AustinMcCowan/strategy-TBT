#!/usr/bin/python3
# Austin McCowan
# 11/15/2019

# maintester file

import units as u
import attack as ak
import tkinter as tk
import tiles as t
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import ttk

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
        u.unitCR8("tank", Data.red_list, "Red", True)
        u.unitCR8("tank", Data.red_list, "Red", True)
        u.unitCR8("tank", Data.red_list, "Red", True)
        u.unitCR8("tank", Data.blue_list, "Blue", True)
        u.unitCR8("tank", Data.blue_list, "Blue", True)
        u.unitCR8("tank", Data.blue_list, "Blue", True)      
        
        # Initial team setting
        Data.temp_list_set()
        
    # Since only one unit can be destroyed at a time due to update occuring after every action. This should not cause problems   
    def delete_unit(unit_team):
        for i in range(len(unit_team)):
            if unit_team[i].health <= 0.5: 
                print("--unit was destroyed--")
                unit_team.pop(i)
                break
            
    # Occurs after action and at start of program (Already done in __init__)        
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
            raise Exception("Error: temp unit lists failed to update")
        
    # Occurs after all actions        
    def update_teams():
        if Data.turn_decider > 0:
            Data.red_list = Data.current
            Data.blue_list = Data.other
        elif Data.turn_decider < 0:
            Data.blue_list = Data.current
            Data.red_list = Data.other
            
        # a temporary boolean that will be used to determine if the turn should switch
        end_turn = True
        
        # Checks the list of units available in the current team, if there is atleast one: do not switch team.
        try:
            i = 0
            while i < len(Data.current):
                if Data.current[i].available == True:
                    i = 51
                    end_turn = False
                else:
                    i += 1
        except:
            pass
        
        # Checks to see if the End turn button was pressed
        if frame_visual.endturn == True:
            end_turn = True
        
        # Finally, checks if any of the criteria above were fulfilled. If so: Ends turn.    
        if end_turn == True:   
            Data.turn_decider = Data.turn_decider*(-1)
            for unit in Data.other:
                unit.available = True
            
        # Deletes dead units, updates temp lists
        Data.delete_unit(Data.red_list)
        Data.delete_unit(Data.blue_list)
        Data.temp_list_set()            
        frame_visual.endturn = False
        
# Subframe for attacking/commands        
class VisualAttackFrame(tk.Frame):
    def __init__(self, parent, attack_list, defend_list):
        self.attack_list = attack_list
        self.defend_list = defend_list
        color = Data.team_announcer.lower()
        
        tk.Frame.__init__(self, master=parent, bg="#CCC", highlightbackground = color, highlightthickness=1)
        
        self.lbl_attack = tk.Label(self, text="Unit Attacking:", bg="#CCC")
        self.lbl_attack.grid(row=0, column=0, columnspan=2, sticky='news')
        
        self.tkvar_attack = tk.StringVar(self)
        self.tkvar_attack.set(self.attack_list[0])
        self.drp_attack = tk.OptionMenu(self, self.tkvar_attack, *self.attack_list)
        self.drp_attack.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.lbl_defend = tk.Label(self, text="Unit Defending:", bg="#CCC")
        self.lbl_defend.grid(row=2, column=0, columnspan=2, sticky='news')
        
        self.tkvar_defend = tk.StringVar(self)
        self.tkvar_defend.set(self.defend_list[0])
        self.drp_defend = tk.OptionMenu(self, self.tkvar_defend, *self.defend_list)
        self.drp_defend.grid(row=3, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", bg="#CCC", command=self.destroy)
        self.btn_cancel.grid(row=4, column=0, sticky='news')
        
        self.btn_confirm = tk.Button(self, text="Confirm", bg="#CCC", command=self.send_attack_order)
        self.btn_confirm.grid(row=4, column=1, sticky='news')
        
    def send_attack_order(self):
        # Grab data from frame and use it on attack_call
        first = self.tkvar_attack.get()
        second = self.tkvar_defend.get()
        
        frame_visual.attack_call(first, second)
        
        
# Subframe for creating units
class VisualCreateFrame(tk.Frame):
    def __init__(self, parent):
        color = Data.team_announcer.lower()
        
        tk.Frame.__init__(self, master=parent, bg="#CCC", highlightbackground = color, highlightthickness=1)
        
        self.lbl_create = tk.Label(self, text="Create Unit:")
        self.lbl_create.grid(row=0, column=0, columnspan=2, sticky='news')
        
        self.unitnames = ["tank", "infantry", "recon", "antiair", "fighter", "attackheli"]
        self.tkvar_names = tk.StringVar(self)
        self.tkvar_names.set(self.unitnames[0])
        
        self.dbx_pick_unit = tk.OptionMenu(self, self.tkvar_names, *self.unitnames)
        self.dbx_pick_unit.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.destroy)
        self.btn_cancel.grid(row=2, column=0, sticky='news')
        
        self.btn_confirm = tk.Button(self, text="Confirm", command=self.send_create_order)
        self.btn_confirm.grid(row=2, column=1, sticky='news')
    
        self.grid_columnconfigure(0, weight=50)
        self.grid_columnconfigure(1, weight=50)
        
    def send_create_order(self):
        picked_unit = self.tkvar_names.get()
        
        frame_visual.create_call(picked_unit)
# handles and spawns the grid. 
class GridControl(tk.Frame):
    # Everything is placeholder as of right now
    def __init__(self, parent, boardsize = 30):
        color = Data.team_announcer.lower()
        self.parent = parent
        tk.Frame.__init__(self, master=parent, highlightbackground = color, highlightthickness=1)
        # Creates the canvas (the main piece for this class) and places it
        self.gridboard = Canvas(self, bg="#0F0")
        self.presence = "alive"
        self.gridboard.grid(column=0, row=0, sticky='news')
        self.gridboard.create_line((10, 5, 200, 50))
        self.boardsize = boardsize
    
    # Holds the file paths for the images to be used in draw_tile, only placeholder for now. 
    # Variations include: (tile type, unit type, availability in unit), availability in interactive tile, color of unit, color of tile
    blueunit_img = {"active-infantry-grass":"image", "active-infantry-road":"image"}
    bluefuncttile_blueunit_img = {}
    inactive_bluefuncttile_blueunit_img = {}
    redfuncttile_blueunit_img = {}
    inactive_redfuncttile_blueunit_img = {}

    redunit_img = {"active-infantry-grass":"image", "active-infantry-road":"image"}
    bluefuncttile_redunit_img = {}
    inactive_bluefuncttile_redunit_img = {}
    redfuncttile_redunit_img = {}
    inactive_redfuncttile_redunit_img = {}
    
    justtile_img = {}
    bluefuncttile_img = {}
    inactive_bluefuncttile_img = {}
    redfuncttile_img = {}
    inactive_redfuncttile_img = {}
    
    ''' I will need to develop a tile system to better control tiles and drawing. I may create images for every scenario (i.e infantry
    on road, infantry on factory, tank on grass, used tank on grass). Create a dictionary (plausibly 2: one for units, one for tile type)'''
    # Will be used to place and draw units on the board. draw_board (may be renamed later) will be used after every action most likely.
    def draw_tile(self, unit, tile, posx, posy):
        # Set up an error message to be deployed whenever a tile fails to draw.
        tile_location = "(" + str(posx) + "," + str(self.boardsize - posy) + ")"
        error = "Error has occured: Drawing tile at " + tile_location + " has failed"
        
        # Inner function reserved to actually create the image
        def paint_tile(imgbranch):
            img = imgbranch[dict_reader]
            imgfile = PhotoImage(file=img)
            self.gridboard.create_image(posx, posy, image=imgfile) # Currently only a format ( i guess )
        
        # This will check what kind of tile it is through a chain of "if/elif/else"
        dict_reader = None
        if unit != None:
            activity = ""
            if unit.availability == True:
                activity = "active"
            elif unit.availability == False:
                activity = "inactive"
            else:
                raise Exception(error)
            
            unit_type = unit.title.split("#")[0]
            tile_type = tile.tile_id.split("#")[0]
            dict_reader = str(activity) + "-" + str(unit_type) + "-" + str(tile_type)

            if unit.color.lower() == "red":
                if tile.usable == True:
                    if tile.color.lower() == "blue":  
                        paint_tile(bluefuncttile_redunit_img)
                    elif tile.color.lower() == "red": 
                        paint_tile(redfuncttile_redunit_img)
                    else:
                        raise Exception(error) # Tile cannot be usable if not captured by red/blue

                elif tile.usable == False:
                    if tile.color.lower() == "blue":  
                        paint_tile(inactive_bluefuncttile_redunit_img)
                    elif tile.color.lower() == "red": 
                        paint_tile(inactive_redfuncttile_redunit_img)
                    else:
                        raise Exception(error) # Tile cannot be usable if not captured by red/blue
                
                elif tile.usable == None: 
                    paint_tile(redunit_img)
                
                else: 
                    raise Exception(error)
                
            elif unit.color.lower() == "blue":
                if tile.usable == True:
                    if tile.color.lower() == "blue": 
                        paint_tile(bluefuncttile_blueunit_img)
                    elif tile.color.lower() == "red":
                        paint_tile(redfuncttile_blueunit_img)
                    else:
                        raise Exception(error) # Tile cannot be usable if not captured by red/blue

                elif tile.usable == False:
                    if tile.color.lower() == "blue":
                        paint_tile(inactive_bluefuncttile_blueunit_img)
                    elif tile.color.lower() == "red": 
                        paint_tile(inactive_redfuncttile_blueunit_img)
                    else: 
                        raise Exception(error) # Tile cannot be usable if not captured

                elif tile.usable == None: # 
                    paint_tile(blueunit_img)

                else:
                    raise Exception(error) # 'usable' is broken on unit.

            else:
                raise Exception(error) # Unit is either assigned to no team or a false one.  

        # For drawing tiles without units on them   
        elif unit == None:
            tile_type = tile.tile_id.split("#")[0]
            dict_reader = str(tile_type)

            if tile.usable == True:
                if tile.color.lower() == "blue":
                    paint_tile(bluefuncttile_img)
                elif tile.color.lower() == "red": 
                    paint_tile(redfuncttile_img)
                else:
                    raise Exception(error) # Tile cannot be usable if not captured by red/blue

            elif tile.usable == False:
                if tile.color.lower() == "blue": 
                    paint_tile(inactive_bluefuncttile_img)
                elif tile.color.lower() == "red": 
                    paint_tile(inactive_redfuncttile_img)
                else:
                    raise Exception(error) # Tile cannot be usable if not captured by red/blue
            
            elif tile.usable == None: 
                paint_tile(justtile_img)
            
            else: 
                raise Exception(error)
            
        else:
            raise Exception(error)
        
    # Will run drawTile for everytile
    def draw_board(self):
        posx = 0
        posy = 0
        # For each column
        for i in range(self.boardsize):
            posy = i+1
            # For each row
            for j in range(self.boardsize):
                posx = j+1
                pass
    
    # Will check to see if a tile is occupied during a move
    def check_tile(self):
        pass

                
# GUI
class Visual(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.endturn = False
        
        self.lbl_information = tk.Label(self, text = '''Placeholder text inbound''', bg="#BBB")
        self.lbl_information.grid(row=0, column=0, rowspan=3, sticky='news')
        
        self.color_adjust()
        starter_team_announce = "Current Team: " + Data.team_announcer
        self.lbl_current_team = tk.Label(self, text = starter_team_announce)
        self.lbl_current_team.grid(row=0, column=2, columnspan=2)
        
        self.btn_attack = tk.Button(self, text="Attack", command = self.open_attack_frame)
        self.btn_attack.grid(row=1, column=2, sticky='news')
        
        self.btn_create = tk.Button(self, text="Create", command = self.open_create_frame)
        self.btn_create.grid(row=2, column=2, sticky='news')
        
        self.btn_list = tk.Button(self, text="List", command = self.list_call)
        self.btn_list.grid(row=1, column=3, sticky='news')        
        
        self.btn_endturn = tk.Button(self, text="End Turn", command = self.endturn_call)
        self.btn_endturn.grid(row=2, column=3, sticky='news')
        
        self.scr_text = ScrolledText(self, height = 10, width = 60)
        self.scr_text.grid(row=3, column=0, sticky='news')
        
        
        self.frm_board = GridControl(self)
        self.frm_board.grid(row=0, column=1, rowspan=4, sticky='news')
        print(self.frm_board.presence)
        self.frm_board.draw_board()
        
        '''Since this zone/area of the program will be empty unless a command is taking place, a placeholder with dark grey 
        background is placed here to indicate it is empty/no action occuring'''
        self.frm_empty = tk.Frame(self, bg = "#AAA")
        self.frm_empty.grid(row=3, column=2, columnspan=2, sticky='news')
        
        
    def color_adjust(self):
        if "red" in Data.team_announcer.lower():
            color = "#ffa8a8"
            
        if "blue" in Data.team_announcer.lower():
            color = "#c1ecec"
        
        self.lbl_information.config(bg=color)
        
    # Updates the gui and basically asks itself if its okay to switch turns
    # So when anything significant happens or changes, call this function.
    def update(self):
        Data.update_teams()
        txt = "Current Team: " + Data.team_announcer
        self.lbl_current_team.configure(text = txt)
        self.color_adjust()
            
    def open_attack_frame(self):
        # Stops the spam creation of frames
        try:
            self.frm_create.destroy()
        except:
            pass
        
        try:
            self.frm_attack.destroy()
        except:
            pass
        
        # Actual code
        temp_attack_list = []
        temp_defend_list = []
        
        # Takes the current turn units (that are available) and puts them in a temp list
        for unit in Data.current:
            if unit.available == True:
                temp_attack_list.append(unit.title)
                
        # Puts all opposite team units in a temp list (as their availability changes nothing)     
        for unit in Data.other:
            temp_defend_list.append(unit.title)
        
        # Creates the attack frame and then raises it
        self.frm_attack = VisualAttackFrame(self, temp_attack_list, temp_defend_list)
        self.frm_attack.grid(row=3, column=2, rowspan=2, columnspan=2, sticky='news')
        self.frm_attack.tkraise()
        
        
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
            self.update()
        self.frm_attack.destroy()
        
    def open_create_frame(self):
        # Stops the spam creation of frames
        try:
            self.frm_create.destroy()
        except:
            pass
        
        try:
            self.frm_attack.destroy() 
        except:
            pass
        
        self.frm_create = VisualCreateFrame(self)
        self.frm_create.grid(row=3, column=2, rowspan=2, columnspan=2, sticky='news')
        self.frm_create.tkraise()
        
    def create_call(self, produce):
        try:
            u.unitCR8(produce, Data.current, Data.team_announcer)
            self.update()
            
        except:
            print("failed to create unit")
            
        self.frm_create.destroy() 
        
    def list_call(self):
        msg = ''
        msg += "\n=======================================\n"
        msg += "Red Team:\n"            
        for unit in Data.red_list:
            msg += str(unit.title) + " | Health: " + str(unit.health) + "\n"
        
        msg += "\nBlue Team:\n"
        for unit in Data.blue_list:
            msg += str(unit.title) + " | Health: " + str(unit.health) + "\n"
        msg += "=======================================\n"
        self.scr_text.insert("insert", msg)
    
    def endturn_call(self):
        try:
            self.frm_create.destroy()
        except:
            pass
        
        try:
            self.frm_attack.destroy()
        except:
            pass
        
        self.endturn = True 
        self.update()

# Initialize stuff
root = tk.Tk()
root.title("maintester.py")
data_storage = Data()

# Setting up layout and gui
frame_visual = Visual()
frame_visual.grid(row = 0, column = 0, sticky = "news")
frame_visual.grid_columnconfigure(0, weight = 0)
frame_visual.grid_columnconfigure(1, weight = 500)
frame_visual.grid_columnconfigure(2, weight = 125)
frame_visual.grid_columnconfigure(3, weight = 125)
frame_visual.grid_rowconfigure(0, weight = 4)
frame_visual.grid_rowconfigure(1, weight = 16)
frame_visual.grid_rowconfigure(2, weight = 16)
frame_visual.grid_rowconfigure(3, weight = 64)
frame_visual.tkraise()

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.mainloop()
