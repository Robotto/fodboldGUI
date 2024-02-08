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

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

    #Dropdown menu
        # Dropdown menu options 
        options = list(self.master.fodboldtur.keys())
            
        # datatype of menu text 
        clicked = StringVar() 
            
        # initial menu text 
        clicked.set( "Medlem" ) 
            
        # Create Dropdown menu 
        drop = OptionMenu( self.payWindow , clicked , *options ) 
        drop.pack() 
            
        # Create Label 
        label = Label( self.payWindow , text = " " ) 
        label.pack() 


    def addMoney(self, clicked, fodboldtur):
        try:
            amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return
        if clicked.get == 'Medlem':
            messagebox.showerror(parent=self.payWindow, title="Vælg et Medlem", message="Du skal vælge et medlem\n før du kan indbetale")
        else:
            self.master.fodboldtur.update({clicked.get: (fodboldtur[clicked.get] + amount)})
            self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
            print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
            self.master.progress['value'] = self.master.total / self.master.target * 100

            ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
            self.master.gemFilen()