import unitterms as ui
import logging as lg

lg.basicConfig(level=lg.DEBUG, handlers=[lg.FileHandler("unitliblog.txt"), lg.StreamHandler()], format="%(asctime)s [%(levelname)s] %(message)s") # logging

# Main script common variables
x = "Would you like to return?"
y = "Invalid, a valid input is 'back'"
z = "back"
a = "yes"
ng = "No group under that title exist under the"

# Main script common unit functions
def cg(winginput):
    return (f"The subordinate groups of the {winginput} are the")
def cs(sqInput):
    return (f"The subordinate squadrons of the {sqInput} are the")
def bu(bInput):
    return(f"Would you like to see the subordinate units of the wings based at {bInput}? Select your unit to continue, back to return")
def ub(ubInput):
    return (f"The units based at {ubInput} are the")

class fwdb:
    def __init__(self, term, img, desc, base): # Wing Misc Data Structure
        self.term = term
        self.img = img 
        self.desc = desc
        self.base = base
    
    def id_db(self):
        return (self.term, self.img, self.desc, self.base) # Wing Method
    
# Wing Misc Data
db1 = fwdb("1st","","","")
db4 = fwdb("4th","","","")
db20 = fwdb("20th","","","")
db23 = fwdb("23d","","","")
db93 = fwdb("93d","","","")
db325 = fwdb("325th","","","")
db355 = fwdb("355th","","","")
db366 = fwdb("366th","","","")
db388 = fwdb("388th","","","")
db432 = fwdb("432nd","","","")
db461 = fwdb("461st","","","")
db495 = fwdb("495th","","","")
db552 = fwdb("522nd","","","")
db633 = fwdb("633d","","","")