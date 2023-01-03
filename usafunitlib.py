import ui
def c2main():
    class group:
        @staticmethod
        def opGroup():
            return f"{x} {ui.gt['og']}"   
        @staticmethod
        def mgGroup():
            return f"{x} {ui.gt['mg']}"
        @staticmethod 
        def megGroup():
            return f"{x} {ui.gt['meg']}"
        @staticmethod
        def msgGroup():
            return f"{x} {ui.gt['msg']}"
        @staticmethod
        def fgGroup():
            return f"{x} {ui.gt['fg']}"
        @staticmethod 
        def rgGroup():
            return f"{x} {ui.gt['rg']}"
        @staticmethod
        def bdsGroup():
            return f"{x} {ui.gt['bds']}"
        @staticmethod
        def asogGroup():
            return f"{x} {ui.gt['asog']}"

    userInput = input("Select your wing under the 15th Air Force.")
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
        print("No wing under the 15th Air Force exists under that title.")
        return c2main()     

    def fw1g():
        if wingdata == ui.af15w["fw1"]:
            y = "yes"
            z = "Yes"
            print(f"The subordinate groups of the {wingdata} are the {group.opGroup()} and the {group.mgGroup()}")
            userInput = input(f"Select a group under the {wingdata}")
            if userInput == ' '.join([x, ui.gt['og']]):
                print(f"The subordinate squadrons of the {x} {ui.gt['og']} are the {x} {ui.st['oss']}, 27th {ui.st['fs']}, 94th {ui.st['fs']}, 7th {ui.st['fts']}, and the 71st {ui.st['fts']}.")
                userInput = input("would you like to return?")
                if userInput == y or z:
                    return fw1g()
                else:
                    print("Invalid")
            elif userInput == ' '.join([x,ui.gt['mg']]):
                print(f"The subordinate squadrons of the {x} {ui.gt['mg']} are the {x} {ui.st['mt']} and the {x} {ui.st['mu']}.")
                userInput = input("would you like to return?")
                if userInput == y or z:
                    return fw1g()
                else:
                    print("Invalid")
            else:
                print(f"No group under that title exist under the {ui.af15w['fw1']}.")
                return fw1g()
    fw1g()         
c2main()