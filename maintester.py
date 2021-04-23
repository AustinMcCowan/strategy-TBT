#!/usr/bin/python3
# Austin McCowan
# 11/15/2019

# maintester file

import units as u
import attack as ak
import tiles as t
try:
    import tkinter as tk
    from tkinter.scrolledtext import ScrolledText
    from tkinter import *
    from tkinter import ttk
    from PIL import ImageTk, Image
except:
    import Tkinter as tk
    from Tkinter.scrolledtext import ScrolledText
    from Tkinter import *
    from Tkinter import ttk
    from PIL import ImageTk, Image

# Hold and initialize starting information. 
class Data(object):
    red_list = []
    blue_list = []
    current = []
    other = []
    turn_decider = (5)
    team_announcer = ''
    tile_list = [] 
    def __init__(self):
        
        # Initial units to start with (TO BE REMOVED/REWORKED)
        '''
        u.unitCR8("tank", Data.red_list, "Red", True)
        u.unitCR8("infantry", Data.red_list, "Red", True)
        u.unitCR8("recon", Data.red_list, "Red", True)
        u.unitCR8("tank", Data.blue_list, "Blue", True)
        u.unitCR8("infantry", Data.blue_list, "Blue", True)
        u.unitCR8("recon", Data.blue_list, "Blue", True)      
        '''

        # Initialize map layout / units (formatted as such = index:["tilecolor#tiletype", "team#unittype"/None])
        # For tiles, color is optional, and is only usable on factories or cities
        Data.layout = {
            0:["grass", "red#tank"],
            1:["grass", None],
            2:["grass", None],
            3:["grass", None],
            4:["grass", None],
            5:["grass", None],
            6:["grass", None],
            7:["grass", None],
            8:["grass", None],
            9:["grass", "blue#tank"],
            10:["grass", "red#infantry"],
            11:["grass", None],
            12:["grass", None],
            13:["grass", None],
            14:["grass", None],
            15:["grass", None],
            16:["grass", None],
            17:["grass", None],
            18:["grass", None],
            19:["grass", "blue#infantry"],
            20:["grass", "red#recon"],
            21:["grass", None],
            22:["grass", None],
            23:["grass", None],
            24:["grass", None],
            25:["grass", None],
            26:["grass", None],
            27:["grass", None],
            28:["grass", None],
            29:["grass", "blue#recon"],
            30:["grass", None],
            31:["grass", None],
            32:["grass", None],
            33:["grass", None],
            34:["grass", None],
            35:["grass", None],
            36:["grass", None],
            37:["grass", None],
            38:["grass", None],
            39:["grass", None],
            40:["grass", None],
            41:["grass", None],
            42:["grass", None],
            43:["grass", None],
            44:["grass", None],
            45:["grass", None],
            46:["grass", None],
            47:["grass", None],
            48:["grass", None],
            49:["grass", None],
            50:["grass", None],
            51:["grass", None],
            52:["grass", None],
            53:["grass", None],
            54:["grass", None],
            55:["grass", None],
            56:["grass", None],
            57:["grass", None],
            58:["grass", None],
            59:["grass", None],
            60:["grass", None],
            61:["grass", None],
            62:["grass", None],
            63:["grass", None],
            64:["grass", None],
            65:["grass", None],
            66:["grass", None],
            67:["grass", None],
            68:["grass", None],
            69:["grass", None],
            70:["grass", None],
            71:["grass", None],
            72:["grass", None],
            73:["grass", None],
            74:["grass", None],
            75:["grass", None],
            76:["grass", None],
            77:["grass", None],
            78:["grass", None],
            79:["grass", None],
            80:["grass", None],
            81:["grass", None],
            82:["grass", None],
            83:["grass", None],
            84:["grass", None],
            85:["grass", None],
            86:["grass", None],
            87:["grass", None],
            88:["grass", None],
            89:["grass", None],
            90:["grass", None],
            91:["grass", None],
            92:["grass", None],
            93:["grass", None],
            94:["grass", None],
            95:["grass", None],
            96:["grass", None],
            97:["grass", None],
            98:["grass", None],
            99:["grass", None]
        }

        '''>> COORDINATES ARE IMPORTANT FOR HANDLING MOUSE CLICKS AND TILE SETTING <<'''
        # Will sync posx with proper pixel locations on canvas/gridboard (may need to update each time window is resized)
        Data.x_coordinates = {} 

        # Will sync posy with proper pixel locations on canvas/gridboard (May need to update each time window is resized)
        Data.y_coordinates = {}

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

# A popup menu that Handles actions from mouse clicks and the other popups
class GridActionMenu(tk.Frame):
    def __init__(self, parent, pos_x=None, pos_y=None, unit=None, factory=None):
        tk.Frame.__init__(self, master=parent, bg="#CCC", highlightthickness=1)
        self.unit = unit
        self.attack_button = tk.Button(self, text="Attack")
        self.create_button = tk.Button(self, text="Create")
        self.move_button = tk.Button(self, text="Move", command = self.action)
        
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.moving = False
        self.unit = unit
        self.factory = factory

        self.button_render()

    def button_render(self):
        if self.unit != None:
            self.attack_button.pack()
            self.move_button.pack()
        
        if (self.factory != None) and (self.factory != False):
            self.create_button.pack()

    def unrender_buttons(self):
        self.attack_button.pack_forget()
        self.move_button.pack_forget()
        self.create_button.pack_forget()

    # Changes side menus to display information of the tile clicked on
    def info_render(self):
        pass

    # Opens a create frame popup
    def open_create_popup(self):
        pass

    # opens a attack frame popup
    def open_attack_popup(self):
        attack_list = []
        
        
        
    # Commits an action
    def action(self):
        self.moving = True
        frame_visual.frm_board.popup.withdraw()
        
    
# handles and spawns the grid. 
class GridControl(tk.Frame):
    # Everything is placeholder as of right now
    def __init__(self, parent, boardsize = 10):
        color = Data.team_announcer.lower()
        self.parent = parent
        tk.Frame.__init__(self, master=parent, highlightbackground = color, highlightthickness=1)
        # Creates the canvas (the main piece for this class) and places it
        self.gridboard = tk.Canvas(self, bg="#0F0")
        self.presence = "alive"
        self.gridboard.grid(column=0, row=0, sticky='news')
        self.boardsize = boardsize # Which translates to both directions (width and length being = to boardsize)
        self.set_coordinates()
        self.gridboard.bind('<Button-1>', self.mouse_click) # Might change this to right click later
        self.gridboard.bind('<Button>', self.info_click)

        # Sets up action menu
        self.popup_exists = False
        self.popup = tk.Tk()
        self.popup.wm_title("Action Menu")
        self.action_menu = GridActionMenu(self.popup)
        self.action_menu.pack()
        self.popup.withdraw()

        # Holds the file paths for the images to be used in draw_tile, only placeholder for now. 
        # Reworked png image dictionaries
        self.blueunit_images = {}
        self.redunit_images = {}
        self.tile_images = {}

        # Keep reference to images
        self.images = []

    # Update the info tab only
    def info_click(self, event):
        # Grab the unit and tile of the point clicked
        pass

        # Send information to the info frame

    def mouse_click(self, event):
        print("Mouse Position: {0}, {1}".format(event.x, event.y)) # Check for response
        
        # Hide popup and its insides.
        def reset():
            try:
                self.popup.withdraw()
                self.popup_exists = False
                self.action_menu.moving = False
                self.action_menu.chosen_unit = None
                self.action_menu.unrender_buttons()
                self.action_menu.pos_x = None
                self.action_menu.pos_y = None
            except:
                self.popup_exists = False
                self.popup = tk.Tk()
                self.popup.wm_title("Action Menu")
                self.action_menu = GridActionMenu(self.popup)
                self.action_menu.pack()
                self.popup.withdraw()
            
        print(f"{self.popup_exists}, {self.action_menu.moving}")
            
        # 1. If When canvas is clicked, no action is in progress, and no menu is open/active: OPEN MENU, SET CONTENT -----------------------------------
        if (self.popup_exists == False) and (self.action_menu.moving == False):
            # Grab window information
            win_x = self.gridboard.winfo_rootx()
            win_y = self.gridboard.winfo_rooty()
            pos_x = win_x + event.x
            pos_y = win_y + event.y

            # Grab current click location information (do this outside of moving click to also preset buttons)
            current_x, current_y = 0, 0
            for i in range(len(Data.x_coordinates)):
                    # Sets current location data
                    if event.x > Data.x_coordinates[i][0]:
                        if event.x < Data.x_coordinates[i][1]:
                            current_x = i
                            print("grabbed current tile pos x")
                        else:
                            pass
                    else:
                        pass

            for i in range(len(Data.y_coordinates)):
                    # Sets current location data
                    if event.y > Data.y_coordinates[i][0]:
                        if event.y < Data.y_coordinates[i][1]:
                            current_y = i
                            print("grabbed current tile pos y")
                        else: 
                            pass
                    else: 
                        pass

            # Grab unit data if any 
            chosen_unit = None
            for unit in Data.current:
                    if (unit.pos_x == current_x) and (unit.pos_y == current_y):
                        chosen_unit = unit   
            
            # Grab factory data on click if there is no unit present
            factory_check = False
            if chosen_unit != None: 
                for tile in Data.tile_list:
                    if (tile.pos_x == current_x) and (tile.pos_y == current_y):
                        try:
                            if tile.color.lower() == Data.team_announcer.lower():
                                if tile.tile_id.split("#")[0] == "factory":
                                    factory_check = True
                        except:
                            pass
                        finally:
                            break
                            
            # make sure there is a reason to open up action menu
            if (chosen_unit != None) or (factory_check != False):
                try:
                    self.popup.iconify()
                    self.popup.geometry(f'+{pos_x}+{pos_y}')
                except:
                    self.popup = tk.Tk()
                    self.popup.wm_title("Action Menu")
                    self.action_menu = GridActionMenu(self.popup)
                    self.action_menu.pack()
                    self.popup.geometry(f'+{pos_x}+{pos_y}')
                finally:
                    self.action_menu.pos_x = current_x
                    self.action_menu.pos_y = current_y
                    self.action_menu.unit = chosen_unit
                    self.action_menu.factory = factory_check
                    self.popup_exists = True
                    self.action_menu.button_render()
                    self.popup.tkraise()
                    print("rendered")

        # 2. When canvas is clicked, menu is active/hidden, and action is selected: COMMIT MOVE, DO NOT OPEN MENU, RESET MENU CONTENT ---------------------
        elif (self.popup_exists == True) and (self.action_menu.moving == True):    
            # Grid coordinates
            current_x = self.action_menu.pos_x
            current_y = self.action_menu.pos_y
            # tile locations
            target_x, target_y = 0, 0
            chosen_unit = None
            print("first step")
            #---- Grab position data ----
            # Grabs x coordinates
            for i in range(len(Data.x_coordinates)):
                # Sets target locaiton data
                if event.x > Data.x_coordinates[i][0]:
                    if event.x < Data.x_coordinates[i][1]:
                        target_x = i
                        print("grabbed target tile pos x")
                    else:
                        pass
                else:
                    pass

            # Sets y coordinates        
            for i in range(len(Data.y_coordinates)):                  
                # Sets target location data
                if event.y > Data.y_coordinates[i][0]:
                    if event.y < Data.y_coordinates[i][1]:
                        target_y = i
                        print("grabbed target tile pos y")
                    else: 
                        pass
                else: 
                    pass
            
            # Grab unit selected
            chosen_unit = self.action_menu.unit

            # Check if distance moved is capable by units move range (MAY REMOVE TILE MOVE COST DUE TO COMPLEXITY)
            

            # Check clicked location for anything
            print("second step")
            tile_info = self.check_tile(target_x, target_y) # Checks tile information and returns it 
            unit_presence = False
            for result in tile_info:
                try:
                    if result[0] == True:
                        unit_presence = True
                        print("checked tile")
                except TypeError:
                    pass

                except:
                    print("Error has occured in grabbing tile information")

            # Move unit at current action location to clicked location
            print("third step")
            if unit_presence != True:
                for unit in Data.current:
                    if (unit.pos_x == current_x) and (unit.pos_y == current_y):
                        unit.pos_x = target_x
                        unit.pos_y = target_y
                        print("unit moved")
                        break
                frame_visual.update()
            else:
                print("tile occupied")

            # Delete any chance for a misread 
            reset()
        
        # 3. when canvas is clicked, action menu is open: HIDE MENU / RESET CONTENT ---------------------------------------------------------------
        elif self.popup_exists == True: 
            reset()


    ''' I will need to develop a tile system to better control tiles and drawing. I may create images for every scenario (i.e infantry
    on road, infantry on factory, tank on grass, used tank on grass). Create a dictionary (plausibly 2: one for units, one for tile type)'''
    # Will be used to place and draw units on the board. draw_board (may be renamed later) will be used after every action most likely.
    def draw_tile(self, unit, tile, posx, posy):
        # Set up an error message to be deployed whenever a tile fails to draw.
        tile_location = "(" + str(posx) + "," + str(posy) + ")"
        error = "Error has occured: Drawing tile at " + tile_location + " has failed"
        
        # Inner function reserved to actually create the image
        def paint_image(imgbranch, test):
            # Finding the image
            # img_path = imgbranch[reader]
            if test == "unit":
                img_path = 'img/jpgball.jpeg'
            else:
                img_path = 'img/testball.png'

            img = Image.open(img_path)

            # Setting up coordinates/positions
            current_x = Data.x_coordinates[posx][0] - 1
            current_y = Data.y_coordinates[posy][0] - 1
            edge_x = Data.x_coordinates[posx][1] + 1
            edge_y = Data.y_coordinates[posy][1] + 1
            x_size = (edge_x - current_x)
            y_size = (edge_y - current_y)
            position_x = current_x + (x_size/2)
            position_y = current_y + (y_size/2)

            # Applying Coordinates/positions and setting image
            if int(x_size) <= 0:
                x_size = 1
            else:
                pass
            if int(y_size) <= 0:
                y_size = 1
            else: 
                pass
            
            img = img.resize((int(x_size), int(y_size)), Image.ANTIALIAS) # Properly fitting image into its coordinates
            img = ImageTk.PhotoImage(img)
            
            # --- KEEP REFERENCE TO IMAGE OUTSIDE OF LOCAL SCOPE ---
            # put image inside the class scope if its not already.
            if img not in self.images:
                self.images.append(img)
            
            # Grab the class scope image reference 
            chosen_image = None
            for i in range(len(self.images)):
                if img == self.images[i]:
                    chosen_image = i
            
            self.gridboard.create_image(position_x, position_y, image=self.images[i]) # Currently only a format ( i guess )
        
        # This will check what kind of tile it is through a chain of "if/elif/else"
        #try:
        reader = None
        tile_type = tile.tile_id.split("#")[0]

        # Paint the tile
        try:
            reader = str(tile_type)
            paint_image(self.tile_images, 'b')
        except:
            raise Exception(error) # Failed to draw tile

        if unit != None:
            # Set up reader 
            activity = ""
            unit_type = unit.title.split("#")[0]
            if unit.available == True:
                activity = "active"
            elif unit.available == False:
                activity = "inactive"
            else:
                raise Exception(error)

            reader = str(activity) + "-" + str(unit_type)

            # Paint the unit    
            try:
                if unit.color.lower() == "red":
                    paint_image(self.redunit_images, 'unit')

                elif unit.color.lower() == "blue":
                    paint_image(self.blueunit_images, 'unit')

                else:
                    raise Exception(error) # Unit is either assigned to no team or a false one.
            except:
                raise Exception(error) # Failed to draw image
           

    def set_coordinates(self): # This will spew out some wacky coordinates at first, but its irrelevant as they are reset nearly immediately.
        frameheight, framewidth = self.gridboard.winfo_height(), self.gridboard.winfo_width()
        current_x, current_y = 1, 1
        interval_height = frameheight / self.boardsize
        interval_width = framewidth / self.boardsize
        set_height = interval_height - 1
        set_width = interval_width - 1

        for i in range(self.boardsize): 
            Data.x_coordinates[i] = [current_x, set_width]
            current_x = set_width + 2 # Removes overlapping 
            set_width += interval_width

            Data.y_coordinates[i] = [current_y, set_height]
            current_y = set_height + 2 # Removes overlapping
            set_height += interval_height

    # Will run through the board size, creating and drawing a tile for each slot. This function will only ever need to be ran once.
    # I need to set an initialize for the tiles, since having them be created inside draw_board will mean tiles will be created every action.
    def initialize_board(self):
        posx = 0
        posy = 0
        index = 0
        # For each column
        for i in range(self.boardsize):
            posy = i
            # For each row
            for j in range(self.boardsize):
                posx = j
                chosen_unit = None
                # ---- UNIT SETTING ----
                ''' Need to create an instruction list of sorts that basically determines what tiles / units are
                placed on the board, in order of index, i.e 1:("grass", "red_infantry") (DONE)'''
                # tile_id = Data.layout[index][0] + "#" + str(index)   << format for tile_id of sorts
                # This should work later due to units not being able to occupy the same space.
                if Data.layout[index][1] != None:
                    layout_unit_reader = Data.layout[index][1].split("#")
                    if layout_unit_reader[0].lower() == "red":
                        u.unitCR8(layout_unit_reader[1], Data.red_list, "Red", True, posx, posy)
                    elif layout_unit_reader[0].lower() == "blue":
                        u.unitCR8(layout_unit_reader[1], Data.blue_list, "Blue", True, posx, posy)

                # ---- TILE CHECKING ----
                tile_info = self.check_tile(posx, posy) # Checks tile information and returns it 
                unit_presence = False # Used to check if there is a unit present

                # Sets conditions for tiles due to unit presence conditions
                for result in tile_info:
                    try:
                        if result[0] == True:
                            chosen_unit = result[1]
                            unit_presence = True
                    except TypeError:
                        pass

                    except:
                        print("Error has occured in grabbing tile information")

                # ---- TILE SETTING ----
                try:
                    layout_tile_reader = Data.layout[index][0].split("#")
                except:
                    layout_tile_reader = Data.layout[index][0]

                # Checks to see if there is color present and tiletype present
                tile_id = ""
                try:
                    if len(layout_tile_reader) > 1:
                        tile_id = layout_tile_reader[1] + "#" + str(index)
                        tile_color = layout_tile_reader[0]
                        t.tileCR8(tile_id, Data.tile_list, posx, posy, color=tile_color, occupied=unit_presence)
                    else:
                        tile_id = Data.layout[index][0] + "#" + str(index)
                        t.tileCR8(tile_id, Data.tile_list, posx, posy, occupied=unit_presence)
                except:
                    print("Tile type missing; Solving issue...")
                    Data.layout[index][0] = "grass"
                    tile_id = Data.layout[index][0] + "#" + str(index)
                    t.tileCR8(tile_id, Data.tile_list, posx, posy, occupied=unit_presence)


                # ---- DRAWING ----
                
                # If a unit is present on the tile, use it. If not, put None value in its place
                if unit_presence == True:
                    self.draw_tile(chosen_unit, Data.tile_list[index], posx, posy)
                else:
                    self.draw_tile(None, Data.tile_list[index], posx, posy) 
                index += 1 # Just add this afterwards so as to not cause problems with indexing on information list
                
        Data.temp_list_set()

    # Will run drawtile for every tile.
    def draw_board(self):
        posx = 0
        posy = 0
        index = 0
        self.gridboard.delete("all") # Remove all items on the canvas to prevent memory problems.
        # For each column
        for i in range(self.boardsize):
            posy = i
            # For each row
            for j in range(self.boardsize):
                posx = j
                chosen_unit = None
                # tile_id = list[index][0] + "#" + str(index)   << format for tile_id of sorts
                # This should work later due to units not being able to occupy the same space.
                tile_info = self.check_tile(posx, posy) # Checks tile information and returns it 
                unit_presence = False # Used to check if there is a unit present

                # Grabs unit (if there is) from unit_presence and confirms this with 'does_unit_exist'
                for result in tile_info:
                    try:
                        if result[0] == True:
                            chosen_unit = result[1]
                            unit_presence = True
                    except TypeError:
                        pass

                    except:
                        print("Error has occured in grabbing tile information")
                
                # If a unit is present on the tile, use it. If not, put None value in its place
                if unit_presence == True:
                    self.draw_tile(chosen_unit, Data.tile_list[index], posx, posy)
                else:
                    self.draw_tile(None, Data.tile_list[index], posx, posy)

                # drawTile(unit, tile, posx, posy) 
                index += 1 # Just add this afterwards so as to not cause problems with indexing on information list

    # Will check to see if a tile is occupied during a move. Will be used to stop actions if unit is present.
    def check_tile(self, posx, posy):
        # Format as so: [blue unit check, red unit check]
        result = [None, None]
        for unit in Data.red_list:
            if (unit.pos_x == posx) and (unit.pos_y == posy):
                result[0] = (True, unit)
                break
            else:
                continue
        
        for unit in Data.blue_list:
            if (unit.pos_x == posx) and (unit.pos_y == posy):
                result[1] = (True, unit)
                break
            else:
                continue

        # Just another safeguard to insure a problem hasn't occured in unit placement 
        # Reason for not 'if result[0] == result[1]:' is because they could both be None, which is fine.
        if None not in result:
            raise Exception("Error has occured during draw: Red unit and blue unit coexist on one tile")
        else:
            return result


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
        print(self.frm_board.presence) # Makes sure the board is actually created/exists.
        self.frm_board.initialize_board() # Set up initial units and set the tiles
        
        '''Since this zone/area of the program will be empty unless a command is taking place, a placeholder with dark grey 
        background is placed here to indicate it is empty/no action occuring'''
        self.frm_empty = tk.Frame(self, bg = "#AAA")
        self.frm_empty.grid(row=3, column=2, columnspan=2, sticky='news')

    # This method will be responsible for handling changes in the window size and will update coordinates in Data, as well as redraw the board.
    def resize(self, event):
        frameheight, framewidth = self.frm_board.winfo_height(), self.frm_board.winfo_width()
        self.frm_board.gridboard.config(width=framewidth, height=frameheight)
        #print("width: " + str(self.frm_board.gridboard.winfo_width()))
        #print("height: "+ str(self.frm_board.gridboard.winfo_height()))
        self.frm_board.set_coordinates()
        self.frm_board.draw_board()

    def color_adjust(self):
        if "red" in Data.team_announcer.lower():
            color = "#ffa8a8"
            
        if "blue" in Data.team_announcer.lower():
            color = "#c1ecec"
        
        self.lbl_information.config(bg=color)
        
    # Updates the gui and basically asks itself if its okay to switch turns
    # So when anything significant happens or changes, call this function.
    def update(self):
        try:
            Data.update_teams()
            self.frm_board.draw_board()
        except IndexError:
            print("IndexError: Data.tile_list not setup currently")
        finally:
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
frame_visual.grid_columnconfigure(1, weight = 400)
frame_visual.grid_columnconfigure(2, weight = 125, pad = 50, minsize = 150)
frame_visual.grid_columnconfigure(3, weight = 125, pad = 50, minsize = 150)
frame_visual.grid_rowconfigure(0, weight = 4)
frame_visual.grid_rowconfigure(1, weight = 16)
frame_visual.grid_rowconfigure(2, weight = 16)
frame_visual.grid_rowconfigure(3, weight = 64)
frame_visual.tkraise()
frame_visual.frm_board.bind("<Configure>", frame_visual.resize)

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.mainloop()
