# importing tkinter module
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #image stuff - install package: Pillow


class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("600x700")
        canvas= Canvas(self.listWindow, width= 600, height= 700, bg="SpringGreen2")

        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()
        
        # img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
        # panel = Label(self.listWindow, image=img)
        # panel.image = img
        # panel.pack(side="bottom", fill="both", expand="yes")

        yCoord = 1 # yPosition for teksten
        
        xPos = 300 # Statisk x Position for alt tekst i vinduet
    
        try:
            for k,v in self.master.fodboldtur.items():
                if v < 4500:
                    paymentRemaining = 4500 - v
                    canvas.create_text(xPos, (50 * yCoord), text=f'{k} har betalt {v} og mangler at betale {paymentRemaining}kr.-', fill="black", font=('Helvetica 11 bold'))

                    yCoord += 1 # Stepper tekstens y position til næste run af for loop'et
                else:
                    canvas.create_text(xPos, (50 * yCoord), text=f'{k} har betalt {v} og er færdig med at betale', fill="black", font=('Helvetica 11 bold'))
                    
                    yCoord += 1 # Stepper tekstens y position til næste run af for loop'et
        except:
            messagebox.showerror(parent=self.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!\n MANGLER Betalinger.pk!!")

        canvas.pack()