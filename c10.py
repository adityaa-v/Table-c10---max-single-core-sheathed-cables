from tkinter import *

conduitType = ["Heavy duty rigid UPVC conduit", "Corflo conduit", 
"Medium duty corrugated", "Medium duty rigid UPVC conduit"]
CableType = ["-", "1", "1.5", "2.5", "4" , "6" ,"10" ,"16", "25", "35", "50", "70" , "95" ,"120" ,"150","185","240","300",
"400","500","630"]


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
        
        self.PVCLabel = Label (master, text = "Cable Type", height=2, width=20)#Label
        self.PVCLabel.grid(row=1, column = 0)
        self.cable = StringVar(master)

        self.cable.set("-") # default value
        self.PVCom = OptionMenu(master, self.cable, *CableType, )
        self.PVCom.config(width=15)
        self.PVCom.grid(row=1, column=1)

        self.circuitLbl = Label (master, text = "Number of Circuits:", height=1, width=20) #Label
        self.circuitLbl.grid(row=2, column = 0)

        self.circuit = IntVar(master)
        self.getCircuit = Entry (master) #text box 
        self.getCircuit.grid(row=2, column=1)  
        self.circuit.set("-")        
            
        btn = Button(master, text="Calculate", bg="light grey", command=self.onButtonClick)
        btn.grid(row = 3,column=1)           
        self.conduitTypeResult = Label (master, text = "Conduit Type-> ", height=1, width=40) #Label
        self.conduitTypeResult.grid(row=0, column =2)    
        self.PVCResult = Label (master, text = "Cable Type-> ", height=2, width=25) #Label
        self.PVCResult.grid(row=1, column =2)    
        self.circuitNo = Label (master, text = "Number of Circuits-> ", height=2, width=25) #Label
        self.circuitNo.grid(row=2, column =2)   

        self.conduitResult = Label (master, text = "-", height=2, width=40, font='Helvetica 9 bold') #Label
        self.conduitResult.grid(row=3, column =2)    

        close = Button(master, text="Close", bg="light grey", command=master.destroy)
        close.grid(row = 4,column=0) 
   
        def reset():
             self.PVCResult.configure(text="" )
             self.conduitTypeResult.configure(text="-" )
             self.PVCResult.configure(text="-" )
             self.conduit.set("Heavy duty rigid UPVC conduit")
             self.cable.set("-")

        tableview = Button(master, text="Reset", bg="light grey", command=reset)
        tableview.grid(row = 3,column=0) 

    def onButtonClick(self):
        
        def getConduitType(self):
            self.x = self.conduit.get()
            return self.x

        def getPVC(self):
            self.x = self.cable.get()
            return self.x      
        
        def getCircuits(self):
            self.x = self.getCircuit.get()
            return self.x     

        if (getPVC(self)=="-"):
            self.error = Label (master, text = "Either CableType or XLPE has to be selected", height=2, width=35, fg="red") #Label
            self.error.grid(row=4, column =1)

        else:
            self.error = Label (master, text = "", height=2, width=35, fg="red") #Label
            self.error.grid(row=4, column =1)

        self.conduitTypeResult.configure(text="Conduit Type:  " +self.conduit.get(), font='Helvetica 9 bold')

        if(getPVC(self)=="-"):
            self.PVCResult.configure(text="-" )
        else:
            self.PVCResult.configure(text="CableType:  " + self.cable.get(),font='Helvetica 9 bold' )
        
        self.circuitNo.configure(text="Number of Circuits:  "+self.getCircuit.get(), font='Helvetica 9 bold')

        def circuitNo(self):
    
            if (getConduitType(self)=="Heavy duty rigid UPVC conduit"):
                if ((getPVC(self)=="25" or getPVC(self)=="35" or getPVC(self)=="50" )
                    and getCircuits(self) == "0"):
                    return '20'
                if ((getPVC(self)=="70" or getPVC(self)=="95") and getCircuits(self) == "0"):
                    return "20 or 25"
                if ((getPVC(self)=="120" or getPVC(self)=="150") and getCircuits(self) == "0"):
                    return "20, 25 or 32"
                if ((getPVC(self)=="185" or 
                getPVC(self)=="240" or getPVC(self)=="300") and getCircuits(self) == "0"):
                    return "20, 25, 32 or 40" 
                if ((getPVC(self)=="400" or getPVC(self)=="500") and getCircuits(self) == "0"):
                    return "20, 25, 32, 40 or 50"    
                if ((getPVC(self)=="630") and getCircuits(self) == "0"):
                    return "20, 25, 32, 40, 50 or 63"

                if ((getPVC(self)=="25" or getPVC(self)=="35")
                    and getCircuits(self) == "1"):
                    return '25 or 32'
                if ((getPVC(self)=="50") and getCircuits(self) == "1"):
                    return "25,	32 or 40"
                if ((getPVC(self)=="70") and getCircuits(self) == "1"):
                    return "25,	32,	40 or 50"
                if ((getPVC(self)=="95") and getCircuits(self) == "1"):
                    return "32 or 40" 
                if ((getPVC(self)=="120" or getPVC(self)=="150") and getCircuits(self) == "1"):
                    return "40 or 50"    
                if ((getPVC(self)=="185" or 
                getPVC(self)=="240") and getCircuits(self) == "1"):
                    return "50 or 63"
                if ((getPVC(self)=="300") and getCircuits(self) == "1"):
                    return "50, 63 or 80(NZ)"
                if ((getPVC(self)=="400" or getPVC(self)=="500") and getCircuits(self) == "1"):
                    return "63 or 80(NZ) or 80(AUS)"
                if ((getPVC(self)=="630") and getCircuits(self) == "1"):
                    return "80(NZ), 80(AUS) or 100(NZ)"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "2"):
                    return "40"
                if ((getPVC(self)=="70") and getCircuits(self) == "2"):
                    return "50"
                if ((getPVC(self)=="120") and getCircuits(self) == "2"):
                    return "63"
                if ((getPVC(self)=="150") and getCircuits(self) == "2"):
                    return "150"
                if ((getPVC(self)=="240") and getCircuits(self) == "2"):
                    return "80(NZ)"
                if ((getPVC(self)=="300") and getCircuits(self) == "2"):
                    return "80(AUS)"
                if ((getPVC(self)=="630") and getCircuits(self) == "2"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "3"):
                    return "40"
                if ((getPVC(self)=="50") and getCircuits(self) == "3"):
                    return "50"
                if ((getPVC(self)=="95") and getCircuits(self) == "3"):
                    return "63"
                if ((getPVC(self)=="185") and getCircuits(self) == "3"):
                    return "80(NZ)"
                if ((getPVC(self)=="240") and getCircuits(self) == "3"):
                    return "80(AUS)"
                if ((getPVC(self)=="400" or getPVC(self)=="500") and getCircuits(self) == "3"):
                    return "100(NZ) or 100(AUS)"
                if ((getPVC(self)=="630") and getCircuits(self) == "3"):
                    return "125"

                if ((getPVC(self)=="25") and getCircuits(self) == "4"):
                    return "50"
                if ((getPVC(self)=="50") and getCircuits(self) == "4"):
                    return "63"
                if ((getPVC(self)=="150") and getCircuits(self) == "4"):
                    return "80(NZ)"
                if ((getPVC(self)=="185") and getCircuits(self) == "4"):
                    return "80(AUS)"
                if ((getPVC(self)=="300") and getCircuits(self) == "4"):
                    return "100(NZ) or 100(AUS)"
                if ((getPVC(self)=="500") and getCircuits(self) == "4"):
                    return "125"
                if ((getPVC(self)=="630") and getCircuits(self) == "4"):
                    return "150"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "5"):
                    return "50"
                if ((getPVC(self)=="120") and getCircuits(self) == "5"):
                    return "80(NZ)"
                if ((getPVC(self)=="150") and getCircuits(self) == "5"):
                    return "80(AUS)"
                if ((getPVC(self)=="240") and getCircuits(self) == "5"):
                    return "100(NZ) or 100(AUS)"
                if ((getPVC(self)=="400") and getCircuits(self) == "5"):
                    return "125"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "6"):
                    return "63"
                if ((getPVC(self)=="95") and getCircuits(self) == "6"):
                    return "80(NZ)"
                if ((getPVC(self)=="120") and getCircuits(self) == "6"):
                    return "80(AUS)"
                if ((getPVC(self)=="185") and getCircuits(self) == "6"):
                    return "100(NZ) or 100(AUS)"
                if ((getPVC(self)=="300") and getCircuits(self) == "6"):
                    return "125"
                if ((getPVC(self)=="500") and getCircuits(self) == "6"):
                    return "150"
                #7
                if ((getPVC(self)=="35") and getCircuits(self) == "7"):
                    return "63"
                if ((getPVC(self)=="95") and getCircuits(self) == "7"):
                    return "80(AUS)"
                if ((getPVC(self)=="150") and getCircuits(self) == "7"):
                    return "100(NZ)"
                if ((getPVC(self)=="400") and getCircuits(self) == "7"):
                    return "150"
                #8                       
                if ((getPVC(self)=="70") and getCircuits(self) == "8"):
                    return "80(NZ)"
                if ((getPVC(self)=="150") and getCircuits(self) == "8"):
                    return "100(AUS)"
                if ((getPVC(self)=="240") and getCircuits(self) == "8"):
                    return "125"
                if ((getPVC(self)=="300") and getCircuits(self) == "8"):
                    return "150"
                #9
                if ((getPVC(self)=="25") and getCircuits(self) == "9"):
                    return "63"
                if ((getPVC(self)=="70") and getCircuits(self) == "9"):
                    return "80(AUS)"
                if ((getPVC(self)=="120") and getCircuits(self) == "9"):
                    return "100(NZ)"

                if ((getPVC(self)=="50") and getCircuits(self) == "10"):
                    return "80(NZ)"
                if ((getPVC(self)=="120") and getCircuits(self) == "10"):
                    return "100(AUS)"
                if ((getPVC(self)=="185") and getCircuits(self) == "10"):
                    return "125"
                if ((getPVC(self)=="240") and getCircuits(self) == "10"):
                    return "150"

                if ((getPVC(self)=="95") and getCircuits(self) == "11"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "12"):
                    return "80(AUS)"
                if ((getPVC(self)=="95") and getCircuits(self) == "12"):
                    return "100(AUS)"
                if ((getPVC(self)=="150") and getCircuits(self) == "12"):
                    return "125"

                if ((getPVC(self)=="35") and getCircuits(self) == "15"):
                    return "80(AUS)"
                if ((getPVC(self)=="70") and getCircuits(self) == "15"):
                    return "100(NZ)"              
                if ((getPVC(self)=="120") and getCircuits(self) == "15"):
                    return "125"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "16"):
                    return "80(NZ)"
                if ((getPVC(self)=="70") and getCircuits(self) == "16"):
                    return "100(AUS)"
                if ((getPVC(self)=="150") and getCircuits(self) == "16"):
                    return "150"
                
                if ((getPVC(self)=="95") and getCircuits(self) == "18"):
                    return "125"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "19"):
                    return "80(AUS"
                if ((getPVC(self)=="50") and getCircuits(self) == "19"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="120") and getCircuits(self) == "20"):
                    return "150"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "21"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "24"):
                    return "100(NZ)"
                if ((getPVC(self)=="70") and getCircuits(self) == "24"):
                    return "125"
                if ((getPVC(self)=="95") and getCircuits(self) == "24"):
                    return "150"

                if ((getPVC(self)=="35") and getCircuits(self) == "26"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "29"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "31"):
                    return "125"
                if ((getPVC(self)=="70") and getCircuits(self) == "31"):
                    return "150"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "39"):
                    return "125"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "41"):
                    return "150"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "48"):
                    return "125"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "52"):
                    return "150"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "62"):
                    return "150"
                #CableType AND HEAVY    
                
                #1
                if ((getPVC(self)=="4") and getCircuits(self) == "1"):
                    return "20"
                if ((getPVC(self)=="6") and getCircuits(self) == "1"):
                    return "20"
                if ((getPVC(self)=="10" or getPVC(self)=="16") and getCircuits(self) == "1"):
                    return "20 or 25"
                #3
                if ((getPVC(self)=="2.5") and getCircuits(self) == "3"):
                    return "20"
                if ((getPVC(self)=="4" or getPVC(self)=="6") and getCircuits(self) == "3"):
                    return "25"
                if ((getPVC(self)=="16") and getCircuits(self) == "3"):
                    return "32"

                #4
                if ((getPVC(self)=="1.5") and getCircuits(self) == "4"):
                    return "20"
                if ((getPVC(self)=="10") and getCircuits(self) == "4"):
                    return "32"
                #5
                if ((getPVC(self)=="1") and getCircuits(self) == "5"):
                    return "20"
                if ((getPVC(self)=="2.5") and getCircuits(self) == "5"):
                    return "25"
                if ((getPVC(self)=="16") and getCircuits(self) == "5"):
                    return "40"
                #6
                if ((getPVC(self)=="6") and getCircuits(self) == "6"):
                    return "32"
                if ((getPVC(self)=="10") and getCircuits(self) == "6"):
                    return "40"
                #7
                if ((getPVC(self)=="1.5") and getCircuits(self) == "7"):
                    return "25"
                if ((getPVC(self)=="4") and getCircuits(self) == "7"):
                    return "32"
                #8

                if ((getPVC(self)=="16") and getCircuits(self) == "8"):
                    return "50"

                #9
                if ((getPVC(self)=="1") and getCircuits(self) == "9"):
                    return "25"
                if ((getPVC(self)=="6") and getCircuits(self) == "9"):
                    return "40"
                #10
                if ((getPVC(self)=="2.5") and getCircuits(self) == "10"):
                    return "32"
                #11
                if ((getPVC(self)=="4") and getCircuits(self) == "11"):
                    return "40"
                if ((getPVC(self)=="10") and getCircuits(self) == "11"):
                    return "50"
                #13
                if ((getPVC(self)=="1.5") and getCircuits(self) == "13"):
                    return "32"
                if ((getPVC(self)=="16") and getCircuits(self) == "13"):
                    return "63"
                #16
                if ((getPVC(self)=="1") and getCircuits(self) == "16"):
                    return "32"
                if ((getPVC(self)=="2.5") and getCircuits(self) == "16"):
                    return "40"
                if ((getPVC(self)=="6") and getCircuits(self) == "16"):
                    return "50"
                #18
                if ((getPVC(self)=="10") and getCircuits(self) == "18"):
                    return "63"
                #19
                if ((getPVC(self)=="4") and getCircuits(self) == "19"):
                    return "50"
                #19
                if ((getPVC(self)=="1.5") and getCircuits(self) == "21"):
                    return "40"
                #24
                if ((getPVC(self)=="16") and getCircuits(self) == "24"):
                    return "80(NZ)"
                #24
                if ((getPVC(self)=="1") and getCircuits(self) == "26"):
                    return "40"
                if ((getPVC(self)=="6") and getCircuits(self) == "26"):
                    return "63"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "27"):
                    return "50"
                
                if ((getPVC(self)=="16") and getCircuits(self) == "28"):
                    return "82(AUS)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "31"):
                    return "63"

                if ((getPVC(self)=="10") and getCircuits(self) == "32"):
                    return "80(NZ)"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "32"):
                    return "80(NZ)"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "36"):
                    return "50"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "36"):
                    return "50"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "38"):
                    return "80(AUS)"

                if ((getPVC(self)=="1") and getCircuits(self) == "43"):
                    return "50"
                if ((getPVC(self)=="1") and getCircuits(self) == "43"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "44"):
                    return "63"
                    
                if ((getPVC(self)=="16") and getCircuits(self) == "46"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "48"):
                    return "80(NZ)"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "55"):
                    return "80(AUS)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "56"):
                    return "80(NZ)"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "58"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "59"):
                    return "63"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "63"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "64"):
                    return "80(AUS)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "64"):
                    return "80(AUS)"
                
                if ((getPVC(self)=="16") and getCircuits(self) == "70"):
                    return "125"
                
                if ((getPVC(self)=="1") and getCircuits(self) == "71"):
                    return "63"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "79"):
                    return "80(NZ)"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "85"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "92"):
                    return "80(AUS)"

                if ((getPVC(self)=="6") and getCircuits(self) == "92"):
                    return "100(AUS)"

                if ((getPVC(self)=="16") and getCircuits(self) == "92"):
                    return "150"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "95"):
                    return "125"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "99"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="1") and getCircuits(self) >= '99'):
                    return "80(NZ), 80(AUS), 100(NZ), 100(AUS), 125 or 150"

                if ((getPVC(self)=="1.5") and getCircuits(self) >= '99'):
                    return "80(NZ), 80(AUS), 100(NZ), 100(AUS), 125 or 150"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) >= '99'):
                    return "100(NZ), 100(AUS), 125 or 150"



        ##########          PROBLEM?????????????????????????????????????????????????????
                if ((getPVC(self)=="4") and (getCircuits(self) <= "99")):
                    return "null"                       

                if ((getPVC(self)=="4") and getCircuits(self) >= "100"):
                    return "100(AUS), 125 or 150"
    
                if ((getPVC(self)=="6") and getCircuits(self) >= '99'):
                    return "125 or 150"
                
                if ((getPVC(self)=="10") and getCircuits(self) >= '99'):
                    return "150"
                    
            if (getConduitType(self)=="Corflo conduit"):
                if ((getPVC(self)=="16") and getCircuits(self) == "43"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="16") and getCircuits(self) == "45"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "60"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "89"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "58"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "85"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "99"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "99"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="16") and getCircuits(self) == "67"):
                    return "125"
                
                if ((getPVC(self)=="10") and getCircuits(self) == "97"):
                    return "125"
                
                if ((getPVC(self)=="16") and getCircuits(self) == "88"):
                    return "150"

                if ((getPVC(self)=="1" or (getPVC(self)=="1.5" or (getPVC(self)=="2.5"))) and getCircuits(self) >= '99'):
                    return "100(NZ), 100(AUS), 125 or 150"
                    
                if ((getPVC(self)=="4") and getCircuits(self) >= '99'):
                    return "100(AUS), 125 or 150"
                    
                if ((getPVC(self)=="6") and getCircuits(self) >= '99'):
                    return "125 or 150"
                    
                if ((getPVC(self)=="10") and getCircuits(self) >= '99'):
                    return "150"
                
                if ((getPVC(self)=="630") and getCircuits(self) == "1"):
                    return "100(NZ) or 100(AUS)"
                
                if ((getPVC(self)=="400" or getPVC(self)=='500') and getCircuits(self) == "3"):
                    return "100(NZ) or 100(AUS)"               
                if ((getPVC(self)=="630") and getCircuits(self) == "3"):
                    return "125"
                
                if ((getPVC(self)=="300") and getCircuits(self) == "4"):
                    return "100(NZ) or 100(AUS)"               
                if ((getPVC(self)=="500") and getCircuits(self) == "4"):
                    return "125"
                if ((getPVC(self)=="630") and getCircuits(self) == "4"):
                    return "150"
                
                if ((getPVC(self)=="240") and getCircuits(self) == "5"):
                    return "100(NZ) or 100(AUS)"               
                if ((getPVC(self)=="400") and getCircuits(self) == "5"):
                    return "125"
                
                if ((getPVC(self)=="185") and getCircuits(self) == "6"):
                    return "100(NZ) or 100(AUS)"               
                if ((getPVC(self)=="300") and getCircuits(self) == "6"):
                    return "125"
                if ((getPVC(self)=="400" or getPVC(self)=="500") and getCircuits(self) == "6"):
                    return "150"
                
                if ((getPVC(self)=="150") and getCircuits(self) == "7"):
                    return "100(NZ)"               
                if ((getPVC(self)=="240") and getCircuits(self) == "7"):
                    return "125"
                
                if ((getPVC(self)=="150") and getCircuits(self) == "8"):
                    return "100(AUS)"  
                if ((getPVC(self)=="300") and getCircuits(self) == "8"):
                    return "150"  
                
                if ((getPVC(self)=="95") and getCircuits(self) == "11"):
                    return "100(NZ)"
                
                if ((getPVC(self)=="120") and getCircuits(self) == "10"):
                    return "100(AUS)" 
                if ((getPVC(self)=="240") and getCircuits(self) == "10"):
                    return "125" 
                if ((getPVC(self)=="300") and getCircuits(self) == "10"):
                    return "150" 
                
                if ((getPVC(self)=="95") and getCircuits(self) == "12"):
                    return "100(AUS)" 
                if ((getPVC(self)=="150") and getCircuits(self) == "12"):
                    return "125" 
                
                if ((getPVC(self)=="185") and getCircuits(self) == "13"):
                    return "150" 
                
                if ((getPVC(self)=="120") and getCircuits(self) == "14"):
                    return "125" 
                
                if ((getPVC(self)=="150") and getCircuits(self) == "16"):
                    return "150" 
                
                if ((getPVC(self)=="95") and getCircuits(self) == "17"):
                    return "125" 
                
                if ((getPVC(self)=="70") and getCircuits(self) == "15"):
                    return "100(NZ) or 100(AUS)" 
                
                if ((getPVC(self)=="120") and getCircuits(self) == "19"):
                    return "150" 
                if ((getPVC(self)=="50") and getCircuits(self) == "19"):
                    return "100(NZ)" 
                
                if ((getPVC(self)=="70") and getCircuits(self) == "20"):
                    return "125" 

                if ((getPVC(self)=="70") and getCircuits(self) == "23"):
                    return "125" 
                if ((getPVC(self)=="95") and getCircuits(self) == "23"):
                    return "150" 

                if ((getPVC(self)=="35") and getCircuits(self) == "24"):
                    return "100(NZ)" 
                
                if ((getPVC(self)=="25") and getCircuits(self) == "29"):
                    return "100(NZ)" 
                
                if ((getPVC(self)=="25") and getCircuits(self) == "30"):
                    return "100(AUS)"
                if ((getPVC(self)=="70") and getCircuits(self) == "30"):
                    return "150"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "25"):
                    return "100(AUS)"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "30"):
                    return "125"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "38"):
                    return "125"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "45"):
                    return "125"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "45"):
                    return "125"
                
                if ((getPVC(self)=="50") and getCircuits(self) == "40"):
                    return "150"
                
                if ((getPVC(self)=="25") and getCircuits(self) == "60"):
                    return "150"
                
                if ((getPVC(self)=="35") and getCircuits(self) == "50"):
                    return "150"
        
            if (getConduitType(self)=="Medium duty corrugated"):
        
                if ((getPVC(self)=="4" or getPVC(self)=="6" or getPVC(self)=="10" or getPVC(self)=="16") and getCircuits(self) == "1"):
                    return "20"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "2"):
                    return "20"
                if ((getPVC(self)=="6") and getCircuits(self) == "2"):
                    return "25"
                if ((getPVC(self)=="16") and getCircuits(self) == "2"):
                    return "32"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "3"):
                    return "20"
                if ((getPVC(self)=="4") and getCircuits(self) == "3"):
                    return "25"
                if ((getPVC(self)=="16") and getCircuits(self) == "3"):
                    return "32"
            
                if ((getPVC(self)=="1") and getCircuits(self) == "4"):
                    return "20"
                if ((getPVC(self)=="2.5") and getCircuits(self) == "4"):
                    return "25"
                if ((getPVC(self)=="16") and getCircuits(self) == "4"):
                    return "40"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "5"):
                    return "32"
                if ((getPVC(self)=="10") and getCircuits(self) == "5"):
                    return "40"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "6"):
                    return "25"
                if ((getPVC(self)=="6") and getCircuits(self) == "6"):
                    return "32"
                
                if ((getPVC(self)=="1") and getCircuits(self) == "7"):
                    return "25"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "8"):
                    return "32"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "11"):
                    return "32"
                
                if ((getPVC(self)=="1") and getCircuits(self) == "14"):
                    return "32"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "8"):
                    return "40"
                
                if ((getPVC(self)=="1") and getCircuits(self) == "23"):
                    return "40"
                
                if ((getPVC(self)=="1.5") and getCircuits(self) == "19"):
                    return "40"
                
                if ((getPVC(self)=="2.5") and getCircuits(self) == "14"):
                    return "40"
                
                if ((getPVC(self)=="6") and getCircuits(self) == "10"):
                    return "40"
                    
            if (getConduitType(self)=="Medium duty rigid UPVC conduit"):
    
                if ((getPVC(self)=="16") and getCircuits(self) == "0"):
                    return "16"

                if ((getPVC(self)=="2.5" or getPVC(self)=="4" or getPVC(self)=="6" or getPVC(self)=="10") and getCircuits(self) == "1"):
                    return "16"
                if ((getPVC(self)=="6" or getPVC(self)=="10" or getPVC(self)=="16") and getCircuits(self) == "1"):
                    return "20"
                if ((getPVC(self)=="16") and getCircuits(self) == "1"):
                    return "35"
                
                if ((getPVC(self)=="4") and getCircuits(self) == "2"):
                    return "20"
                if ((getPVC(self)=="10") and getCircuits(self) == "2"):
                    return "25"
                
                if ((getPVC(self)=="1" or getPVC(self)=="1.5") and getCircuits(self) == "3"):
                    return "16"
                if ((getPVC(self)=="2.5" ) and getCircuits(self) == "3"):
                    return "20"
                if ((getPVC(self)=="6" ) and getCircuits(self) == "3"):
                    return "25"
                if ((getPVC(self)=="16" ) and getCircuits(self) == "3"):
                    return "32"
                
                if ((getPVC(self)=="1.5" ) and getCircuits(self) == "5"):
                    return "20"
                
                if ((getPVC(self)=="1" ) and getCircuits(self) == "6"):
                    return "20"
                
                if ((getPVC(self)=="4" ) and getCircuits(self) == "4"):
                    return "25"
                
                if ((getPVC(self)=="2.5" ) and getCircuits(self) == "6"):
                    return "25"
                
                if ((getPVC(self)=="1.5" ) and getCircuits(self) == "8"):
                    return "25"
                
                if ((getPVC(self)=="1" ) and getCircuits(self) == "10"):
                    return "25"
                
                if ((getPVC(self)=="10" ) and getCircuits(self) == "4"):
                    return "32"
                
                if ((getPVC(self)=="6" ) and getCircuits(self) == "6"):
                    return "32"
                
                if ((getPVC(self)=="4" ) and getCircuits(self) == "7"):
                    return "32"
                
                if ((getPVC(self)=="2.5" ) and getCircuits(self) == "11"):
                    return "32"
                
                if ((getPVC(self)=="1.5" ) and getCircuits(self) == "14"):
                    return "32"
                
                if ((getPVC(self)=="1" ) and getCircuits(self) == "17"):
                    return "32"

                if ((getPVC(self)=="16" ) and getCircuits(self) == "5"):
                    return "40"
                
                if ((getPVC(self)=="10" ) and getCircuits(self) == "7"):
                    return "40"
                
                if ((getPVC(self)=="6" ) and getCircuits(self) == "10"):
                    return "40"
                
                if ((getPVC(self)=="4" ) and getCircuits(self) == "12"):
                    return "40"
                
                if ((getPVC(self)=="2.5" ) and getCircuits(self) == "17"):
                    return "40"
                
                if ((getPVC(self)=="1.5" ) and getCircuits(self) == "23"):
                    return "40"
                
                if ((getPVC(self)=="1" ) and getCircuits(self) == "28"):
                    return "40"
                

                if ((getPVC(self)=="1" ) and getCircuits(self) == "45"):
                    return "50"
                
                if ((getPVC(self)=="1.5" ) and getCircuits(self) == "38"):
                    return "50"
                
                if ((getPVC(self)=="2.5" ) and getCircuits(self) == "28"):
                    return "50"
                
                if ((getPVC(self)=="4" ) and getCircuits(self) == "20"):
                    return "50"
                
                if ((getPVC(self)=="6" ) and getCircuits(self) == "17"):
                    return "50"
                
                if ((getPVC(self)=="10" ) and getCircuits(self) == "11"):
                    return "50"
                
                if ((getPVC(self)=="16" ) and getCircuits(self) == "8"):
                    return "50"
                    
            else:
                return "null"
        
        self.conduitResult.configure(text="Number of Conduits: \n" + circuitNo(self))
            
master = Tk()
master.title("Number of Conduits. Table C10")
master.geometry("750x175")
app = Application(master)

master.mainloop()



