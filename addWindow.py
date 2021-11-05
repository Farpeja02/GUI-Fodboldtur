from tkinter import *
from tkinter.ttk import *


class addWindowClass:

    def __init__(self, master,fodboldturDict):
        self.master = master #reference til main window objektet
        self.addWindow = Toplevel(self.master.root)
        self.addWindow.title("Add a member")
        self.addWindow.geometry("200x200")
        self.fodboldtur = fodboldturDict


        Label(self.addWindow,
              text="tilføj").pack()

        self.add = Entry(self.addWindow)
        self.add.pack()

        self.button = Button(self.addWindow, text="tilføj", command= self.addName())
        self.button.pack()

    def addName(self):
        navn= self.add.get() #HUSK AT VALIDERE INPUT!, kun positive heltal!
        self.fodboldtur.update({navn: 0})

