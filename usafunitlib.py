import unitterms as ui # For wing, group, and squadron global data
import logging as lg # For logging
import logging.handlers
import customtkinter # For GUI
import tkinter # GUI dependency 
from PIL import Image, ImageTk # Image importing
import os 

lg.basicConfig(level=lg.DEBUG, handlers=[lg.FileHandler("unitliblog.txt")], format="%(asctime)s [%(levelname)s] %(message)s") # logging
should_roll_over = os.path.isfile("unitliblog.txt")
handler = logging.handlers.RotatingFileHandler("unitliblog.txt", mode='w', backupCount=5)

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
                                                        values=["Select a Wing...", f"{ui.af15w['fw1']}", f"{ui.af15w['fw4']}", f"{ui.af15w['fw20']}", f"{ui.af15w['w23']}", f"{ui.af15w['agow93']}", f"{ui.af15w['fw325']}", f"{ui.af15w['fw366']}", f"{ui.af15w['fw388']}", f"{ui.af15w['w432']}", f"{ui.af15w['acw461']}", f"{ui.af15w['fg495']}", f"{ui.af15w['acw552']}", f"{ui.af15w['abw633']}"], 
                                                        command=App.c2main,
                                                        variable=optionmenu_var)
        self.optionmenu.grid(row=3, column=0, padx=20, pady=(20, 10))

        # Image structure // reserved for later dev
        self.image_frame = customtkinter.CTkFrame(self,corner_radius=10)
        self.image_frame.grid(column=3, row=0, rowspan = 3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky='nsew')
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets\\img_assets\\")
        self.af15 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "af15.png")), size=(285, 280))
        self.image_display = customtkinter.CTkLabel(master=self, image=self.af15, text="")
        self.image_display.grid(column=3, row=0, rowspan = 3, columnspan=1, sticky='nsew')
        
        # Description
        self.textbox = customtkinter.CTkTextbox(self, font=('Arial', 15), wrap='word')
        self.textbox.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(20, 2.5), pady=(20, 20), sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, corner_radius=10)
        self.textbox2.grid(row=3, rowspan=1, column=3, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox.insert("0.0", "15th Air Force\n\n" + ui.af15['af15desc'])

    def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
    def back(self):
        optionmenu_var = customtkinter.StringVar(value="Select a Wing...")
        self.optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["Select a Wing...", f"{ui.af15w['fw1']}", f"{ui.af15w['fw4']}", f"{ui.af15w['fw20']}", f"{ui.af15w['w23']}", f"{ui.af15w['agow93']}", f"{ui.af15w['fw325']}", f"{ui.af15w['fw366']}", f"{ui.af15w['fw388']}", f"{ui.af15w['w432']}", f"{ui.af15w['acw461']}", f"{ui.af15w['fg495']}", f"{ui.af15w['acw552']}", f"{ui.af15w['abw633']}"], 
                                                        command=App.c2main,
                                                        variable=optionmenu_var)
        self.optionmenu.grid(row=3, column=0, padx=20, pady=(20, 10))
        self.textbox.delete('1.0', "end")
        self.textbox.insert("0.0", "15th Air Force\n\n" + ui.af15['af15desc'])
        self.af15 = customtkinter.CTkImage(Image.open(os.path.join(app.image_path, "af15.png")), size=(285, 280))
        self.image_display = customtkinter.CTkLabel(master=self, image=self.af15, text="")
        self.image_display.grid(column=3, row=0, rowspan = 3, columnspan=1, sticky='nsew')

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
    def image_load(patch):
            App.patch = customtkinter.CTkImage(Image.open(os.path.join(app.image_path, f"{patch}.png")), size=(285, 280))
            app.image_display = customtkinter.CTkLabel(master=app, image=app.patch, text="")
            app.image_display.grid(column=3, row=0, rowspan = 3, columnspan=1, sticky='nsew')
            
    def insert_desc(unit, maindict, sub2dict, sub3dict):
        app.textbox.delete('1.0', "end")
        app.textbox.insert("0.0", f"{unit}\n\n" + maindict[sub2dict][sub3dict])

    def wing_desc(title, wing):
            app.textbox.delete('1.0', "end")
            app.textbox.insert("0.0", f"{ui.af15w[title]}\n\n" + wing['wing'])
    
    def c2main(wdata):
        if wdata == ui.af15w['fw1']: #1st Fighter Wing
            wt = "1st"
            App.wing_desc('fw1', ui.fw1d)
            App.image_load('fw1st')
            def fw1g(x): # 1st Fighter Wing Units
                optionmenu_var1 = customtkinter.StringVar(value="Select a Group")
                optionmenu_var2 = customtkinter.StringVar(value="Select a Squadron")
                def fw1gui(wdata):
                    if wdata == ' '.join([wt, ui.gt['og']]):
                        App.insert_desc(f"{wt} {ui.gt['og']}", ui.fw1d, 'opgroup', 'opsg')
                        App.image_load('opg1st')
                        lg.info("1stOpGroup options and assets displayed")
                        def og1sq(wdata):
                            if wdata == f"{wt} {ui.st['oss']}":
                                App.insert_desc(f"{wt} {ui.st['oss']}", ui.fw1d, 'opgroup', 'oss1')
                                App.image_load('blank')
                                lg.info("1st OSS displayed")
                            elif wdata == f"27th {ui.st['fs']}":
                                App.insert_desc(f"27th {ui.st['fs']}", ui.fw1d, 'opgroup', 'fs27')
                                App.image_load('blank')
                                lg.info("27th FS displayed")
                            elif wdata == f"94th {ui.st['fs']}":
                                App.insert_desc(f"94th {ui.st['fs']}", ui.fw1d, 'opgroup', 'fs94')
                                App.image_load('blank')
                                lg.info("94th FS displayed")
                            elif wdata == f"7th {ui.st['ts']}":
                                App.insert_desc(f"7th {ui.st['ts']}", ui.fw1d, 'opgroup', 'ts7')
                                App.image_load('blank')
                                lg.info("7th TS displayed")
                            elif wdata == f"71st {ui.st['fts']}":
                                App.insert_desc(f"71st {ui.st['fts']}", ui.fw1d, 'opgroup', 'fts71')
                                App.image_load('blank')
                                lg.info("71st FTS displayed")
                            elif wdata == 'Return':
                                app.textbox.delete('1.0', "end")
                                App.image_load('fw1st')
                                app.textbox.insert("0.0", f"{ui.af15w['fw1']}\n\n" + ui.fw1d['wing'])
                                lg.info("Returning")
                                return fw1g(x)
                        app.optionmenu.configure(values=["Select a Squadron...", f"{wt} {ui.st['oss']}", f"27th {ui.st['fs']}", f"94th {ui.st['fs']}", f"7th {ui.st['ts']}", f"71st {ui.st['fts']}", 'Return'], variable=optionmenu_var2, command=og1sq)
                    elif wdata == ' '.join([wt,ui.gt['mg']]):
                        App.insert_desc(f"{wt} {ui.gt['mg']}" ,ui.fw1d, 'maintgroup', 'maintg')
                        App.image_load('mxg1st')
                        lg.info("1stMaintGroup units and assets displayed")
                        def mg1sq(wdata):
                            if wdata == f"{wt} {ui.st['mt']}":
                                App.insert_desc(f"{wt} {ui.st['mt']}", ui.fw1d, 'maintgroup', 'mxs1')
                                App.image_load('blank')
                                lg.info("1st MXS displayed")
                            elif wdata == f"{wt} {ui.st['mu']}":
                                App.insert_desc(f"{wt} {ui.st['mu']}", ui.fw1d, 'maintgroup', 'mu1')
                                App.image_load('blank')
                                lg.info("1st MS displayed")
                            elif wdata == f"27th {ui.st['fgs']}":
                                App.insert_desc(f"27th {ui.st['fgs']}", ui.fw1d, 'maintgroup', 'fgs27')
                                App.image_load('blank')
                                lg.info("27th FGS displayed")
                            elif wdata == f"94th {ui.st['fgs']}":
                                App.insert_desc(f"94th {ui.st['fgs']}", ui.fw1d, 'maintgroup', 'fgs94')
                                App.image_load('blank')
                                lg.info("94th FGS displayed")
                            elif wdata == 'Return':
                                app.textbox.delete('1.0', "end")
                                App.image_load('fw1st')
                                App.wing_desc('fw1', ui.fw1d)
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
            pass
        elif wdata == ui.af15w['fw20']: # 20th Fighter Wing
            pass
        elif wdata == ui.af15w['w23']: # 23d Wing
            pass
        elif wdata == ui.af15w["agow93"]:
            pass
        elif wdata == ui.af15w["fw325"]:
            pass
        elif wdata == ui.af15w["fw366"]:
            pass
        elif wdata == ui.af15w["fw388"]:
            pass
        elif wdata == ui.af15w["w432"]:
            pass
        elif wdata == ui.af15w["acw461"]:
            pass
        elif wdata == ui.af15w["fg495"]:
            pass
        elif wdata == ui.af15w["acw552"]:
            pass
        elif wdata == ui.af15w["abw633"]:
            pass
if __name__ == "__main__":
    app = App()
    app.iconbitmap("af15icon.ico")
    app.mainloop()
