import unitterms as ui # For wing, group, and squadron global data
import logging as lg # For logging
import wingdb as wdb # Wing misc data
import customtkinter # For GUI
import tkinter # GUI dependency 
from PIL import Image, ImageTk # Image importing
import os 

lg.basicConfig(level=lg.DEBUG, handlers=[lg.FileHandler("unitliblog.txt")], format="%(asctime)s [%(levelname)s] %(message)s") # logging

class App(customtkinter.CTk): # GUI Framework 
    def __init__(self):
        super().__init__()

        # configure window
        self.title("15th AF Unit Lib")
        self.geometry(f"{1366}x{768}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_columnconfigure((4), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # sidebar with option menu
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="15th AF Unit Lib", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("Dark")
        optionmenu_var = customtkinter.StringVar(value="Select a Wing...")
        self.optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["Select a Wing...", f"{ui.af15w['fw1']}", f"{ui.af15w['fw4']}", f"{ui.af15w['fw20']}", f"{ui.af15w['w23']}"], 
                                                        command=App.c2main,
                                                        variable=optionmenu_var)
        self.optionmenu.grid(row=3, column=0, padx=20, pady=(20, 10))

        # Image structure // reserved for later dev
        self.image_frame = customtkinter.CTkFrame(self, width=200, height=240, corner_radius=10)
        self.image_frame.grid(column=3, row=0, rowspan = 3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky='nsew')
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets\\img_assets\\")
        self.wing_1st_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "1stFW_display.png")).resize((200, 240),Image.Resampling.BILINEAR))
        self.image_display = customtkinter.CTkLabel(master=self.image_frame, image=self.wing_1st_image, text="", fg_color=None, compound='center')
        self.image_display.grid(column=3, row=0, rowspan = 3, columnspan=1)
        # Description
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(20, 2.5), pady=(20, 20), sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, corner_radius=10)
        self.textbox2.grid(row=3, rowspan=1, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
    def back(self):
        optionmenu_var = customtkinter.StringVar(value="Select a Wing...")
        self.optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["Select a Wing...", f"{ui.af15w['fw1']}", f"{ui.af15w['fw4']}", f"{ui.af15w['fw20']}", f"{ui.af15w['w23']}"], 
                                                        command=App.c2main,
                                                        variable=optionmenu_var)
        self.optionmenu.grid(row=3, column=0, padx=20, pady=(20, 10))
        self.textbox.delete('1.0', "end")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def c2main(wdata):
        class group: # Group Methods
            @staticmethod
            def opGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['og']}"
                else: 
                    return f"{uid} {ui.gt['og']}"
            @staticmethod
            def mgGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['mg']}"
                else: 
                    return f"{uid} {ui.gt['mg']}"
            @staticmethod 
            def megGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['meg']}"
                else: 
                    return f"{uid} {ui.gt['meg']}"
            @staticmethod
            def msgGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['msg']}"
                else: 
                    return f"{uid} {ui.gt['msg']}"
            @staticmethod
            def fgGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['fg']}"
                else: 
                    return f"{uid} {ui.gt['fg']}"
            @staticmethod 
            def rgGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['rg']}"
                else: 
                    return f"{uid} {ui.gt['rg']}"
            @staticmethod
            def bdsGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['bds']}"
                else: 
                    return f"{uid} {ui.gt['bds']}"
            @staticmethod
            def asogGroup(uid):
                if uid == wt:
                    return f"{wt} {ui.gt['asog']}"
                else: 
                    return f"{uid} {ui.gt['asog']}"
                
        if wdata == ui.af15w['fw1']: #1st Fighter Wing
            wt = wdb.db1.term
            app.textbox.insert("0.0", ui.fw1d['wing'])
            def fw1g(x): # 1st Fighter Wing Units
                lg.info(f"{wdb.cg(wdata)} {group.opGroup(x)} and the {group.mgGroup(x)}")
                optionmenu_var1 = customtkinter.StringVar(value="Select a Group")
                optionmenu_var2 = customtkinter.StringVar(value="Select a Squadron")
                def fw1gui(wdata):
                    if wdata == ' '.join([wt, ui.gt['og']]):
                        app.textbox.delete('1.0', "end")
                        app.textbox.insert("0.0", ui.fw1d['opgroup']['opsg'])
                        lg.info("1stOpGroup options and assets displayed")
                        def og1sq(wdata):
                            if wdata == f"{wt} {ui.st['oss']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['opgroup']['oss1'])
                                lg.info("1st OSS displayed")
                            elif wdata == f"27th {ui.st['fs']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['opgroup']['fs27'])
                                lg.info("27th FS displayed")
                            elif wdata == f"94th {ui.st['fs']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['opgroup']['fs94'])
                                lg.info("94th FS displayed")
                            elif wdata == f"7th {ui.st['ts']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['opgroup']['ts7'])
                                lg.info("7th TS displayed")
                            elif wdata == f"71st {ui.st['fts']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['opgroup']['fts71'])
                                lg.info("71st FTS displayed")
                            elif wdata == 'Return':
                                app.textbox.delete('1.0', "end")
                                lg.info("Returning")
                                return fw1g(x)
                        app.optionmenu.configure(values=["Select a Squadron...", f"{wt} {ui.st['oss']}", f"27th {ui.st['fs']}", f"94th {ui.st['fs']}", f"7th {ui.st['ts']}", f"71st {ui.st['fts']}", 'Return'], variable=optionmenu_var2, command=og1sq)
                    elif wdata == ' '.join([wt,ui.gt['mg']]):
                        app.textbox.delete('1.0', "end")
                        app.textbox.insert("0.0", ui.fw1d['maintgroup']['maintg'])
                        lg.info("1stMaintGroup units and assets displayed")
                        def mg1sq(wdata):
                            if wdata == f"{wt} {ui.st['mt']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['maintgroup']['mxs'])
                                lg.info("1st MXS displayed")
                            elif wdata == f"{wt} {ui.st['mu']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['maintgroup']['mu'])
                                lg.info("1st MS displayed")
                            elif wdata == f"27th {ui.st['fgs']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['maintgroup']['fgs27'])
                                lg.info("27th FGS displayed")
                            elif wdata == f"94th {ui.st['fgs']}":
                                app.textbox.delete('1.0', "end")
                                app.textbox.insert("0.0", ui.fw1d['maintgroup']['fgs94'])
                                lg.info("94th FGS displayed")
                            elif wdata == 'Return':
                                app.textbox.delete('1.0', "end")
                                lg.info("Returning")
                                return fw1g(x)
                        app.optionmenu.configure(values=["Select a Squadron...", f"{wt} {ui.st['mt']}", f"{wt} {ui.st['mu']}", f"27th {ui.st['fgs']}", f"94th {ui.st['fgs']}", 'Return'], variable=optionmenu_var2, command=mg1sq)  
                    elif wdata == 'Return':
                        app.textbox.delete('1.0', "end")
                        lg.info("Returning to Main")
                        return app.back()
                app.optionmenu.configure(values=["Select a Group...", ' '.join([wt, ui.gt['og']]), ' '.join([wt,ui.gt['mg']]), 'Return'], variable=optionmenu_var1, command=fw1gui)
            fw1g(wt)
        elif wdata == ui.af15w['fw4']: # 4th Fighter Wing
            wt = wdb.db4.term
            def fw4g(x): # 4th Fighter Wing Units
                lg.info(f"{wdb.cg(wdata)} {group.opGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, and the {group.mgGroup(x)}")
                userInput = input(wdb.gs(wdata))
                if userInput == ' '.join([wt, ui.gt['og']]):
                    lg.info(f"{wdb.cs(wdata)} {wt} {ui.st['oss']}, 333d, 334th, 335th, 336th {ui.st['fs']}s and the {wt} {ui.st['ts']}")
                elif userInput == ' '.join([wt, ui.gt['msg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['cts']}, {wt} {ui.st['fss']}, {wt} {ui.st['lrs']}, and the {wt} {ui.st['sfs']}")
                elif userInput == ' '.join([wt, ui.gt['meg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['hos']} and the {wt} {ui.st['omrs']}")
                elif userInput == ' '.join([wt, ui.gt['mg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['amxs']}, {wt} {ui.st['ems']}, {wt} {ui.st['cms']}, and the 333d, 334th, 335th, 336th {ui.st['fgs']}s ")
            fw4g(wt)
        elif wdata == ui.af15w['fw20']: # 20th Fighter Wing
            wt = wdb.db20.term
            def fw20g(x):    # 20th Fighter Wing Units
                lg.info(f"{wdb.cg(wdata)} {group.opGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, and the {group.mgGroup(x)}")
                userInput = input(wdb.gs(wdata))
                if userInput == ' '.join([wt, ui.gt['og']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['oss']}, and the 55th, 77th, 79th, {ui.st['fs']}s")
                elif userInput == ' '.join([wt, ui.gt['msg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['fss']}, {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['sfs']}, {wt} {ui.st['lrs']}, and the {wt} {ui.st['cts']}")
                elif userInput == ' '.join([wt, ui.gt['meg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['hos']} and the {wt} {ui.st['omrs']}")
                elif userInput == ' '.join([wt, ui.gt['mg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['cms']} and the {wt} {ui.st['ems']}")
            fw20g(wt)
        elif wdata == ui.af15w['w23']: # 23d Wing
            wt = wdb.db23.term
            def w23g(x): #23d Wing Units
                lg.info(f"{wdb.cg(wdata)} {group.fgGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, {group.mgGroup(x)}, and the {group.rgGroup('347th')}")
                userInput = input(wdb.gs(wdata))
                if userInput == ' '.join([wt, ui.gt['fg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['oss']}, 74th, 75th {ui.st['fs']}s")
                elif userInput == ' '.join([wt, ui.gt['msg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['cts']}, {wt} {ui.st['lrs']}, {wt} {ui.st['fss']}, and the {wt} {ui.st['sfs']}")
                elif userInput == ' '.join([wt, ui.gt['meg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['mss']}, {wt} {ui.st['hos']}, and the {wt} {ui.st['omrs']}")
                elif userInput == ' '.join([wt, ui.gt['mg']]):
                    lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['mof']}, {wt} {ui.st['mu']}, {wt} {ui.st['mt']}, 41st, 71st {ui.st['rgs']}, 74th, and 75th {ui.st['fgs']}")
                elif userInput == ' '.join(['347th', ui.gt['rg']]):
                    lg.info(f"{wdb.cs(userInput)} 347th {ui.st['oss']}, and the 38th, 41st, and 71st {ui.st['rs']}s")
            w23g(wt)
if __name__ == "__main__":
    app = App()
    app.mainloop()
