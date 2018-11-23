from tkinter import *

conduitType = ["Heavy duty rigid UPVC conduit", "Corflo conduit", 
"Medium duty corrugated", "Medium duty rigid UPVC conduit"]
PVC = [" ", "1", "1.5", "2.5", "4" , "6" ,"10" ,"16"]
XLPE = [" ", "25", "35", "50", "70" , "95" ,"120" ,"150","185","240","300",
"400","500","630"]
UPVC = ["20",	"25",	"32", "40",	"50",	"63",	
"80",	"80", "100", "100","125", "150",]  
CORFLO = ["100", "100",	"125", "150"]
MDC = ["20", "25", "32", "40"]
MDRUC = ["16", "20", "25", "32", "40", "50",]

class Application(Frame):

    def __init__(self, master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self): 
        self.conduitLbl = Label (self, text = "Type of Conduit", 
        height=2, width=20)#Label
        self.conduitLbl.grid(row=0, column = 0)

        self.conduit = StringVar(master)
        self.conduit.set("Heavy duty rigid UPVC conduit") # default value
        self.conduitOptions = OptionMenu(master, self.conduit, *conduitType)
        self.conduitOptions.config(width=28)
        self.conduitOptions.grid(row=0, column=1)
        
        self.PVCLabel = Label (master, text = "PVC", height=2, width=20)#Label
        self.PVCLabel.grid(row=1, column = 0)
        self.cable = StringVar(master)

        self.cable.set("") # default value
        self.PVCom = OptionMenu(master, self.cable, *PVC, )
        self.PVCom.grid(row=1, column=1)
        
        self.XLPELabel = Label (master, text = "XLPE", height=2, width=20)#Label
        self.XLPELabel.grid(row=2, column = 0)
        self.cable1 = StringVar(master)

        self.cable1.set("") # default value
        self.XLPEMenu = OptionMenu(master, self.cable1, *XLPE)
        self.XLPEMenu.grid(row=2, column=1)

        self.circuitLbl = Label (master, text = "Number of Circuits:", height=1, width=20) #Label
        self.circuitLbl.grid(row=4, column = 0)

        self.circuit = StringVar(master)
        self.getCircuit = Entry (master) #text box 
        self.getCircuit.grid(row=4, column=1)  
        self.circuit.set("")        
            
        btn = Button(master, text="Click me", bg="light grey", command=self.onButtonClick)
        btn.grid(row = 5,column=0)           
        self.conduitTypeResult = Label (master, text = "Conduit Type-> ", height=1, width=40) #Label
        self.conduitTypeResult.grid(row=0, column =2)    
        self.PVCResult = Label (master, text = "PVC-> ", height=2, width=25) #Label
        self.PVCResult.grid(row=1, column =2)
        self.XLPEResult = Label (master, text = "XLPE-> ", height=2, width=25) #Label
        self.XLPEResult.grid(row=2, column =2)    
        self.circuitNo = Label (master, text = "Number of Circuits-> ", height=2, width=25) #Label
        self.circuitNo.grid(row=3, column =2)   
        self.conduitResult = Label (master, text = "", height=2, width=40) #Label
        self.conduitResult.grid(row=4, column =2)

    def onButtonClick(self):

        self.conduitTypeResult.configure(text="Conduit Type-> "+self.conduit.get())
        self.PVCResult.configure(text="PVC-> " +self.cable.get())
        self.XLPEResult.configure(text="XLPE-> "+self.cable1.get())
        self.circuitNo.configure(text="Number of Circuits-> "+self.getCircuit.get())

        def getConduitType(self):
            self.x = self.conduit.get()
            return self.x

        def getPVC(self):
            self.x = self.cable.get()
            return self.x

        def getXLPE(self):
            self.x = self.cable1.get()
            return self.x

        def getCircuits(self):
            self.x = self.getCircuit.get()
            return self.x        

        def circuitNo(self):
            #return getCircuits(self)
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25" or getXLPE(self)=="35" or getXLPE(self)=="50" )
                and getCircuits(self) == "0" and getPVC(self) ==""):
                return '20'
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="70" or getXLPE(self)=="95") and getCircuits(self) == "0" and getPVC(self) ==""):
                return "20 or 25"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120" or getXLPE(self)=="150") and getCircuits(self) == "0" and getPVC(self) ==""):
                return "20, 25 or 32"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="185" or 
            getXLPE(self)=="240" or getXLPE(self)=="300") and getCircuits(self) == "0" and getPVC(self) ==""):
                return "20, 25, 32 or 40" 
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="400" or getXLPE(self)=="500") and getCircuits(self) == "0" and getPVC(self) ==""):
                return "20, 25, 32, 40 or 50"    
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="630") and getCircuits(self) == "0" and getPVC(self) ==""):
                return "20, 25, 32, 40, 50 or 63"

            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25" or getXLPE(self)=="35")
                and getCircuits(self) == "1" and getPVC(self) ==""):
                return '25 or 32'
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="50") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "25,	32 or 40"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="70") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "25,	32,	40 or 50"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="95") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "32 or 40" 
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120" or getXLPE(self)=="150") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "40 or 50"    
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="185" or 
            getXLPE(self)=="240") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "50 or 63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="300") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "50, 63 or 80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="400" or getXLPE(self)=="500") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "63 or 80(NZ) or 80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="630") and getCircuits(self) == "1" and getPVC(self) ==""):
                return "80(NZ), 80(AUS) or 100(NZ)"
            
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="35") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "40"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="70") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "50"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="150") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "150"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="240") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="300") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="630") and getCircuits(self) == "2" and getPVC(self) ==""):
                return "100(AUS)"
            
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "40"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="50") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "50"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="95") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="185") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="240") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="400" or getXLPE(self)=="500") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "100(NZ) or 100(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="630") and getCircuits(self) == "3" and getPVC(self) ==""):
                return "125"

            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "50"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="50") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="150") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="185") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="300") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "100(NZ) or 100(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="500") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "125"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="630") and getCircuits(self) == "4" and getPVC(self) ==""):
                return "150"
            
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25") and getCircuits(self) == "5" and getPVC(self) ==""):
                return "50"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120") and getCircuits(self) == "5" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="150") and getCircuits(self) == "5" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="240") and getCircuits(self) == "5" and getPVC(self) ==""):
                return "100(NZ) or 100(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="400") and getCircuits(self) == "5" and getPVC(self) ==""):
                return "125"
            
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="50") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="95") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="185") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "100(NZ) or 100(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="300") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "125"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="500") and getCircuits(self) == "6" and getPVC(self) ==""):
                return "150"
            #7
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="35") and getCircuits(self) == "7" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="95") and getCircuits(self) == "7" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="150") and getCircuits(self) == "7" and getPVC(self) ==""):
                return "100(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="400") and getCircuits(self) == "7" and getPVC(self) ==""):
                return "150"
            #8                       
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="70") and getCircuits(self) == "8" and getPVC(self) ==""):
                return "80(NZ)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="150") and getCircuits(self) == "8" and getPVC(self) ==""):
                return "100(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="240") and getCircuits(self) == "8" and getPVC(self) ==""):
                return "125"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="300") and getCircuits(self) == "8" and getPVC(self) ==""):
                return "150"
            #9
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="25") and getCircuits(self) == "9" and getPVC(self) ==""):
                return "63"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="70") and getCircuits(self) == "9" and getPVC(self) ==""):
                return "80(AUS)"
            if (getConduitType(self) == "Heavy duty rigid UPVC conduit" and (getXLPE(self)=="120") and getCircuits(self) == "9" and getPVC(self) ==""):
                return "100(NZ)"


            
                  
                    

            
            # getXLPE(self)=="25" or getXLPE(self)=="35" or getXLPE(self)=="50" or 
            # getXLPE(self)=="70" or getXLPE(self)=="95" or getXLPE(self)=="120" or getXLPE(self)=="150" or getXLPE(self)=="185" or 
            # getXLPE(self)=="240" or getXLPE(self)=="300" or getXLPE(self)=="400" or getXLPE(self)=="500" or getXLPE(self)=="630"

            else:
                return "null"
        
        self.conduitResult.configure(text="Number of Conduits-> \n" + circuitNo(self))
            
            

         

         

        
            
master = Tk()
master.title("Application")
app = Application(master)

master.mainloop()



