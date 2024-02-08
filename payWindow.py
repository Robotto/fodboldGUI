# importing tkinter module
from tkinter import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Indbetal").pack()

        Label(self.payWindow,
              text="Vælg Medlem").pack()
        #Dropdown menu
        # Dropdown menu options 
        options = list(self.master.fodboldtur.keys())
            
        # datatype of menu text 
        self.clicked = StringVar() 
            
        # initial menu text 
        self.clicked.set( "Medlem" ) 
            
        # Create Dropdown menu 
        drop = OptionMenu( self.payWindow , self.clicked , *options ) 
        drop.pack() 


        Label(self.payWindow,
              text="Mængde").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

        
    def addMoney(self):
        
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return
        if self.clicked.get() == 'Medlem':
            messagebox.showerror(parent=self.payWindow, title="Vælg et Medlem", message="Du skal vælge et medlem\n før du kan indbetale")
        else:
            self.master.fodboldtur.update({self.clicked.get(): (self.master.fodboldtur[self.clicked.get()] + amount)})
            ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
            self.master.gemFilen()
            self.master.updateVelkomst()

            
        