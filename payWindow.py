# importing tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow,
              text="Indbetal").pack()

        self.options = StringVar(self.payWindow)
        self.options.set("Vælg et navn") #Virker ikke...?
        key = self.master.fodboldtur.keys()
        keyList = list(key)

#OptionMenu(master,     variable,     value,     *values,     **kwargs    )
        self.dropDown = OptionMenu(self.payWindow, self.options, None, *keyList)
        self.dropDown.pack()

        self.money = Entry(self.payWindow)
        self.money.pack()

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack()

    def addMoney(self):

            #amount = abs(int(self.money.get())) #HUSK AT VALIDERE INPUT!, kun positive heltal!
        previousAmount = self.master.fodboldtur[self.options.get()]

        self.master.fodboldtur[self.options.get()] += int(self.money.get())
        #except:
            #messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            #return

        #self.master.total += amount
        #self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        #print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        #self.master.progress['value'] = self.master.total / self.master.target * 100
