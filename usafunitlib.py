import ui

def c2main():
    class group: # Group Methods
        @staticmethod
        def opGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['op']}"
            else: 
                return f"{uid} {ui.gt['op']}"
        @staticmethod
        def mgGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['mg']}"
            else: 
                return f"{uid} {ui.gt['mg']}"
        @staticmethod 
        def megGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['meg']}"
            else: 
                return f"{uid} {ui.gt['meg']}"
        @staticmethod
        def msgGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['msg']}"
            else: 
                return f"{uid} {ui.gt['msg']}"
        @staticmethod
        def fgGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['fg']}"
            else: 
                return f"{uid} {ui.gt['fg']}"
        @staticmethod 
        def rgGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['rg']}"
            else: 
                return f"{uid} {ui.gt['rg']}"
        @staticmethod
        def bdsGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['bds']}"
            else: 
                return f"{uid} {ui.gt['bds']}"
        @staticmethod
        def asogGroup(uid):
            if uid == x:
                return f"{x} {ui.gt['asog']}"
            else: 
                return f"{uid} {ui.gt['asog']}"

    userInput = input("Select your wing under the 15th Air Force")  # 15th AF Wing Selection
    if userInput == ui.af15w["fw1"]:
        wingdata = ui.af15w["fw1"]
        x = "1st"
    elif userInput == ui.af15w["fw4"]:
        wingdata = ui.af15w["fw4"]
        x = "4th"
    elif userInput == ui.af15w["fw20"]:
        wingdata = ui.af15w["fw20"]
        x = "20th"
    elif userInput == ui.af15w["w23"]:
        wingdata = ui.af15w["w23"]
        x = "23d"
    elif userInput == ui.af15w["agow93"]:
        wingdata = ui.af15w["agow93"]
        x = "93d"
    elif userInput == ui.af15w["fw325"]:
        wingdata = ui.af15w["fw325"]
        x = "325th"
    elif userInput == ui.af15w["fw366"]:
        wingdata = ui.af15w["fw366"]
        x = "366th"
    elif userInput == ui.af15w["fw388"]:
        wingdata = ui.af15w["fw388"]
        x = "388th"
    elif userInput == ui.af15w["w432"]:
        wingdata = ui.af15w["w432"]
        x = "432nd" 
    elif userInput == ui.af15w["acw461"]:
        wingdata = ui.af15w["acw461"]
        x = "461st"
    elif userInput == ui.af15w["fg495"]:
        wingdata = ui.af15w["fg495"]
        x = "495th"
    elif userInput == ui.af15w["acw552"]:
        wingdata = ui.af15w["acw552"]
        x = "552nd"
    elif userInput == ui.af15w["abw633"]:
        wingdata = ui.af15w["abw633"]
        x = "633d"
    else: 
        print("No wing under the 15th Air Force exists under that title")
        return c2main()     

    def fw1g(): # 1st Fighter Wing Units
        if wingdata == ui.af15w["fw1"]:
            print(f"The subordinate groups of the {wingdata} are the {group.opGroup('1st')} and the {group.mgGroup('1st')}")
            userInput = input(f"Select a group under the {wingdata}")
            if userInput == ' '.join([x, ui.gt['og']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['oss']}, 27th {ui.st['fs']}, 94th {ui.st['fs']}, 7th {ui.st['fts']}, and the 71st {ui.st['fts']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw1g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x,ui.gt['mg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['mt']} and the {x} {ui.st['mu']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw1g()
                else:
                    print("Invalid")
            elif userInput == "back":
                return c2main()
            else:
                print(f"No group under that title exist under the {ui.af15w['fw1']}")
                return fw1g()
    
    def fw4g(): # 4th Fighter Wing Units
        if wingdata == ui.af15w["fw4"]:
            print(f"The subordinate groups of the {wingdata} are the {group.opGroup('4th')}, {group.msgGroup('4th')}, {group.megGroup('4th')}, and the {group.mgGroup('4th')}")
            userInput = input(f"Select a group under the {wingdata}")
            if userInput == ' '.join([x, ui.gt['og']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['oss']}, 333d, 334th, 335th, 336th {ui.st['fs']}s and the {x} {ui.st['ts']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw4g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['msg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['ces']}, {x} {ui.st['cs']}, {x} {ui.st['cts']}, {x} {ui.st['fss']}, {x} {ui.st['lrs']}, and the {x} {ui.st['sfs']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw4g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['meg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['hos']} and the {x} {ui.st['omrs']}")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return fw4g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([ui.gt['mg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['amxs']}, {x} {ui.st['ems']}, {x} {ui.st['cms']}, and the 333d, 334th, 335th, 336th {ui.st['fgs']}s ")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return fw4g()
                else:
                    print("Invalid")
            elif userInput == "back":
                return c2main()
            else:
                print(f"No group under that title exist under the {ui.af15w['fw4']}")
                return fw4g()
    def fw20g():    # 20th Fighter Wing Units
        if wingdata == ui.af15w["fw20"]:
            print(f"The subordinate groups of the {wingdata} are the {group.opGroup('20th')}, {group.msgGroup('20th')}, {group.megGroup('20th')}, and the {group.mgGroup('20th')}")
            userInput = input(f"Select a group under the {wingdata}")
            if userInput == ' '.join([x, ui.gt['og']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['oss']}, and the 55th, 77th, 79th, {ui.st['fs']}s")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw20g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['msg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['fss']}, {x} {ui.st['ces']}, {x} {ui.st['cs']}, {x} {ui.st['sfs']}, {x} {ui.st['lrs']}, and the {x} {ui.st['cts']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return fw20g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['meg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['hos']} and the {x} {ui.st['omrs']}")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return fw20g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([ui.gt['mg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['cms']} and the {x} {ui.st['ems']}")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return fw20g()
                else:
                    print("Invalid")
            elif userInput == "back":
                return c2main()
            else:
                print(f"No group under that title exist under the {ui.af15w['fw20']}")
                return fw20g()
    def w23g(): #23d Wing Units
        if wingdata == ui.af15w["w23"]:
            print(f"The subordinate groups of the {wingdata} are the {group.fgGroup('23d')}, {group.msgGroup('23d')}, {group.megGroup('23d')}, {group.mgGroup('23d')}, and the {group.rgGroup('347th')}")
            userInput = input(f"Select a group under the {wingdata}")
            if userInput == ' '.join([x, ui.gt['fg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['oss']}, 74th, 75th {ui.st['fs']}s")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return w23g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['msg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['ces']}, {x} {ui.st['cs']}, {x} {ui.st['cts']}, {x} {ui.st['lrs']}, {x} {ui.st['fss']}, and the {x} {ui.st['sfs']}")
                userInput = input("would you like to return?")
                if userInput == "yes":
                    return w23g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['meg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} {ui.st['mss']}, {x} {ui.st['hos']}, and the {x} {ui.st['omrs']}")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return w23g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x, ui.gt['mg']]):
                print(f"The subordinate squadrons of the {userInput} are the {x} Maintenance Operations Flight, {x} {ui.st['mu']}, {x} {ui.st['mt']}, 41st, 71st {ui.st['rgs']}, 74th, and 75th {ui.st['fgs']}")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return w23g()
                else:
                    print("Invalid")
            elif userInput == ' '.join('347th', ui.gt['rg']):
                print(f"The subordinate squadrons of the {userInput} are the 347th {ui.st['oss']}, and the 38th, 41st, and 71st {ui.st['rs']}s")
                userInput = input("would you like to return?")               
                if userInput == "yes":
                    return w23g()
                else:
                    print("Invalid")
        elif userInput == "back":
                return c2main()
        else:
                print(f"No group under that title exist under the {ui.af15w['w23']}")
                return w23g()

    w23g()
    fw20g()
    fw4g()            
    fw1g()         
c2main()