import ui
import logging as lg

lg.basicConfig(level=lg.DEBUG, handlers=[lg.FileHandler("unitliblog.txt"), lg.StreamHandler()], format="%(asctime)s [%(levelname)s] %(message)s") # logging

class fwdb:
    def __init__(self, term, img, desc, base): # Wing Misc Data Structure
        self.term = term
        self.img = img
        self.desc = desc
        self.base = base

    def id_db(self):
        return (self.term, self.img, self.desc, self.base) # Wing Method

    # Wing Misc Data

db1 = fwdb("", "{}", "", "")
db4 = fwdb("", "{}", "", "")
db20 = fwdb("", "{}", "", "")
db23 = fwdb("", "{}", "", "")
db93 = fwdb("", "{}", "", "")
db325 = fwdb("", "{}", "", "")
db355 = fwdb("", "{}", "", "")
db366 = fwdb("", "{}", "", "")
db388 = fwdb("", "{}", "", "")
db432 = fwdb("", "{}", "", "")
db461 = fwdb("", "{}", "", "")
db495 = fwdb("", "{}", "", "")
db552 = fwdb("", "{}", "", "")
db633 = fwdb("", "{}", "", "")
