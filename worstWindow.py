# importing tkinter module
import pickle
from tkinter import *
filename = 'assets/betalinger.pk'

test = False

# Directory til betalinger.pk filen...
fodboldtur ={"./assets/betalinger.pk"}
# Åbner Betalinger.pk
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        # Størrelse af geomatri i vinduet (størrelsen af vinduet)
        self.worstWindow.geometry("450x600")
        # Hvilket vindue canvas'en sidder på, Størrelsen af Canvas og baggrunden
        canvas= Canvas(self.worstWindow, width= 450, height= 600, bg="SpringGreen2")
        Label(self.worstWindow, text="De værste betalere")

        # Variabel til yCoordinate til brug i texten
        yCoord = 1

        #TODONE Fix pickle load / label merge

        #Sorter listen/Filen, Vælger de nederste 3
        top = sorted(fodboldtur.items(), key=lambda item: item[1])
        # Danner par af Key og Value og tager de nederste 3
        for pair in top[:3]:
            # Laver et tekst objekt i canvas'en, Objekterne bliver spacet med 100px mellemrum
            canvas.create_text(150, (100 * yCoord), text=f"{pair[0]} har indbetalt {pair[1]}", fill="black", font=('Helvetica 15 bold'))
            
            yCoord += 1 # Stepper (prep til næste run i for loopet)
        
        canvas.pack() #Pack'er canvasen på siden...

