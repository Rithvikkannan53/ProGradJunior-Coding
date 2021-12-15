#RCCard Data Management Program

class RCCategories:

    def __init__(Self,REG_DATE,CHASSIS_NO,ENGINE_NO,OWNERNAME,S_W_D_OF,ADDRESS,MODEL,BODY,WHEEL_BASE,MFG_DATE,FUEL,REG_UPTO,TAX_UPTO,NO_OF_CYL,UNLADEN_WT,SEATING,STDG_SLPR,CC,O_SL_NO,MFR,CLASS,COLOUR):
        self.REG_DATE
        self.CHASSIS_NO
        self.ENGINE_NO
        self.OWNERNAME
        self.S_W_D_OF
        self.ADDRESS
        self.MODEL
        self.BODY
        self.WHEEL_BASE
        self.MFG_DATE
        self.FUEL
        self.REG_UPTO
        self.TAX_UPTO
        self.NO_OF_CYL
        self.UNLADEN_WT
        self.SEATING
        self.STDG_SLPR
        self.CC
        self.O_SL_NO
        self.MFR
        self.CLASS
        self.COLOUR
        
#function for creating RCCard details
    def create():
        ob = RCCard(Self,REG_DATE,CHASSIS_NO,ENGINE_NO,OWNERNAME,S_W_D_OF,ADDRESS,MODEL,BODY,WHEEL_BASE,MFG_DATE,FUEL,REG_UPTO,TAX_UPTO,NO_OF_CYL,UNLADEN_WT,SEATING,STDG_SLPR,CC,O_SL_NO,MFR,CLASS,COLOUR)
        lists.append(ob)

#function for displaying RCCard details
    def display(self,ob):
        print("REG DATE: ",ob.REG_DATE)
        print("CHASSIS NO: ",ob.CHASSIS_NO)
        print("ENGINE NO: ",ob.ENGINE_NO)
        print("OWNERNAME: ",ob.OWNERNAME)
        print("S/W/D OF: ",ob.S_W_D_OF)
        print("ADDRESS: ",ob.ADDRESS)
        print("MODEL: ",ob.MODEL)
        print("BODY: ",ob.BODY)
        print("WHEEL BASE: ",ob.WHEEL_BASE)
        print("MFG DATE: ",ob.MFG_DATE)
        print("FUEL: ",ob.FUEL)
        print("REG UPTO: ",ob.REG_UPTO)
        print("TAX UPTO: ",ob.TAX_UPTO)
        print("NO OF CYL: ",ob.NO_OF_CYL)
        print("UNLADEN WT: ",ob.UNLADEN_WT)
        print("SEATING: ",ob.SEATING)
        print("STDGSLPR: ",ob.STDG_SLPR)
        print("CC: ",ob.CC)
        print("OSLNO: ",ob.O_SL_NO)
        print("MFR: ",ob.MFR)
        print("CLASS: ",ob.CLASS)
        print("COLOUR: ",ob.COLOUR)
        print("\n")

#creating an empty list
lists = []

#creating an object to access the RCCard Details
obj = RCCard(' ', 0, 0)

print("Operations used...\n")
print("1. Add the RCCard details \n2.List of RCCard details \n3.Exit")

obj.create(10_1_2008,MA3EMD81S00170112,F10DN3296856,K_RITHVIK,K_S_P_G_KANNAN,FLAT_NO_52_VISHALAMMA_NILAYA_KEMPAPURA_MAIN_ROAD_YEMLUR_LI_BANGALORE_560037,MARUTHI_ZEN_LXI_BS3,SALOON,_,2007,PETROL,9_1_2023,LTT,4,855,5,_,1061,2,MARUTI,LMVCAR,PERASILVE)
obj.create(3_1_2011,ME4JC449MA8215444,JC44E1091998,K_RITHVIK,KANNAN_K_S_P_G,FLAT_NO_52_VISHALAMMA_NILAYA_KEMPAPURA_MAIN_ROAD_YEMLUR_LI_BANGALORE_560037,HONDA_ACTIVA,SOLO,_,12_2010,PETROL,2_1_2026,LTT,1,112,2,_,109,1,HONDA,MCYCLE,GREY)

print("\n")
print("List of RCCard details...")
for i in range(lists.__len__()):
    obj.display(lists[i])

print("Data added successfully..")
