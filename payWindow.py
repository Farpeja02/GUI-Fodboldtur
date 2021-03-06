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
              text="Indbetal").pack(pady=(5,15))

        self.options = StringVar(self.payWindow)
        self.options.set("Vælg et navn")
        key = self.master.fodboldtur.keys()
        keyList = list(key)

        #DropDown creates a list of options
        #OptionMenu(master,     variable,     value,     *values,     **kwargs    )
        self.dropDown = OptionMenu(self.payWindow, self.options, None, *keyList)
        self.dropDown.pack()

        self.money = Entry(self.payWindow)
        self.money.pack(padx=30, pady=2)

        self.button = Button(self.payWindow, text="betal", command= self.addMoney)
        self.button.pack(pady=2)

    #Adds the number decieded in Entry, and then assigned it to the name from dropdown, and updates progressbar.
    def addMoney(self):
        try:
            self.master.fodboldtur[self.options.get()] += int(self.money.get())
        except:
            messagebox.showerror(parent=self.payWindow , title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total = sum(self.master.fodboldtur[item] for item in self.master.fodboldtur)
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
