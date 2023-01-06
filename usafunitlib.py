import unitterms as ui # For wing, group, and squadron global data
import logging as lg # For logging
import wingdb as wdb # Wind misc data

lg.basicConfig(level=lg.DEBUG, handlers=[lg.FileHandler("unitliblog.txt"), lg.StreamHandler()], format="%(asctime)s [%(levelname)s] %(message)s") # logging

def c2main():
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
                
    wingdata = input("Select your wing under the 15th Air Force. Or type 'base' to see the 15th Air Forces units organized via base")  # 15th AF Wing Selection
    if wingdata == ui.af15w['fw1']:
        wt = wdb.db1.term
        def fw1g(x): # 1st Fighter Wing Units
            lg.info(f"{wdb.cg(wingdata)} {group.opGroup(x)} and the {group.mgGroup(x)}")
            userInput = input(wdb.gs(wingdata))
            if userInput == ' '.join([wt, ui.gt['og']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['oss']}, 27th {ui.st['fs']}, 94th {ui.st['fs']}, 7th {ui.st['fts']}, and the 71st {ui.st['fts']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw1g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt,ui.gt['mg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['mt']} and the {wt} {ui.st['mu']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw1g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == wdb.z:
                    return c2main()
            else:
                lg.info(wdb.ng(wingdata))
                return fw1g(wt)
        fw1g(wt)
    elif wingdata == ui.af15w['fw4']:
        wt = wdb.db4.term
        def fw4g(x): # 4th Fighter Wing Units
            lg.info(f"{wdb.cg(wingdata)} {group.opGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, and the {group.mgGroup(x)}")
            userInput = input(wdb.gs(wingdata))
            if userInput == ' '.join([wt, ui.gt['og']]):
                lg.info(f"{wdb.cs(wingdata)} {wt} {ui.st['oss']}, 333d, 334th, 335th, 336th {ui.st['fs']}s and the {wt} {ui.st['ts']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw4g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['msg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['cts']}, {wt} {ui.st['fss']}, {wt} {ui.st['lrs']}, and the {wt} {ui.st['sfs']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw4g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['meg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['hos']} and the {wt} {ui.st['omrs']}")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return fw4g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['mg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['amxs']}, {wt} {ui.st['ems']}, {wt} {ui.st['cms']}, and the 333d, 334th, 335th, 336th {ui.st['fgs']}s ")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return fw4g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == wdb.z:
                return c2main()
            else:
                lg.info(wdb.ng(wingdata))
                return fw4g(wt)
        fw4g(wt)
    elif wingdata == ui.af15w['fw20']:
        wt = wdb.db20.term
        def fw20g(x):    # 20th Fighter Wing Units
            lg.info(f"{wdb.cg(wingdata)} {group.opGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, and the {group.mgGroup(x)}")
            userInput = input(wdb.gs(wingdata))
            if userInput == ' '.join([wt, ui.gt['og']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['oss']}, and the 55th, 77th, 79th, {ui.st['fs']}s")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw20g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['msg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['fss']}, {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['sfs']}, {wt} {ui.st['lrs']}, and the {wt} {ui.st['cts']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return fw20g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['meg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['hos']} and the {wt} {ui.st['omrs']}")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return fw20g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['mg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['cms']} and the {wt} {ui.st['ems']}")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return fw20g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == wdb.z:
                return c2main()
            else:
                lg.info(wdb.ng(wingdata))
                return fw20g(wt)
        fw20g(wt)
    elif wingdata == ui.af15w['w23']:
        wt = wdb.db23.term
        def w23g(x): #23d Wing Units
            lg.info(f"{wdb.cg(wingdata)} {group.fgGroup(x)}, {group.msgGroup(x)}, {group.megGroup(x)}, {group.mgGroup(x)}, and the {group.rgGroup('347th')}")
            userInput = input(wdb.gs(wingdata))
            if userInput == ' '.join([wt, ui.gt['fg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['oss']}, 74th, 75th {ui.st['fs']}s")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return w23g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['msg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['ces']}, {wt} {ui.st['cs']}, {wt} {ui.st['cts']}, {wt} {ui.st['lrs']}, {wt} {ui.st['fss']}, and the {wt} {ui.st['sfs']}")
                userInput = input(wdb.x)
                if userInput == wdb.a:
                    return w23g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['meg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['mss']}, {wt} {ui.st['hos']}, and the {wt} {ui.st['omrs']}")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return w23g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join([wt, ui.gt['mg']]):
                lg.info(f"{wdb.cs(userInput)} {wt} {ui.st['mof']}, {wt} {ui.st['mu']}, {wt} {ui.st['mt']}, 41st, 71st {ui.st['rgs']}, 74th, and 75th {ui.st['fgs']}")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return w23g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == ' '.join(['347th', ui.gt['rg']]):
                lg.info(f"{wdb.cs(userInput)} 347th {ui.st['oss']}, and the 38th, 41st, and 71st {ui.st['rs']}s")
                userInput = input(wdb.x)               
                if userInput == wdb.a:
                    return w23g(wt)
                else:
                    lg.warning(wdb.y)
            elif userInput == wdb.z:
                return c2main()
            else:
                lg.info(wdb.ng(wingdata))
                return w23g(wt)
        w23g(wt)
    elif wingdata == ui.af15w["agow93"]:
        wt = wdb.db93.term
    elif wingdata == ui.af15w["fw325"]:
        wt = wdb.db325.term
    elif wingdata == ui.af15w["fw366"]:
        wt = wdb.db366.term
    elif wingdata == ui.af15w["fw388"]:
        wt = wdb.db388.term
    elif wingdata == ui.af15w["w432"]:
        wt = wdb.db432.term
    elif wingdata == ui.af15w["acw461"]:
        wt = wdb.db461.term
    elif wingdata == ui.af15w["fg495"]:
        wt = wdb.db495.term
    elif wingdata == ui.af15w["acw552"]:
        wt = wdb.db552.term
    elif wingdata == ui.af15w["abw633"]:
        wt = wdb.db633.term
    else: 
        lg.info("No wing or base under the 15th Air Force exists under that title")
        return c2main() 
c2main()