from tkinter import *
from tkinter.ttk import *


class addWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.addWindow = Toplevel(self.master.root)
        self.addWindow.title("Add a member")
        self.addWindow.geometry("200x200")


        Label(self.addWindow,
              text="Skriv dit navn").pack(pady=2)

        self.add = Entry(self.addWindow)
        self.add.pack(pady=2)

        self.button = Button(self.addWindow, text="tilføj", command= self.addName)
        self.button.pack(pady=2)

        self.options = StringVar(self.addWindow)
        self.options.set("Vælg et navn")
        self.key = self.master.fodboldtur.keys()
        self.keyList = list(self.key)

        # OptionMenu(master,     variable,     value,     *values,     **kwargs    )
        self.dropDown = OptionMenu(self.addWindow, self.options, None, *self.keyList)
        self.dropDown.pack(pady=(20, 2))

        self.removebButton = Button(self.addWindow, text="slet", command=self.removeName)
        self.removebButton.pack(pady=2)

    def addName(self):
        navn= self.add.get()
        self.master.fodboldtur.update({navn: 0})
        self.key = self.master.fodboldtur.keys()
        self.keyList = list(self.key)
        self.refreshOptionMenu()

    def removeName(self):
        self.master.fodboldtur.pop(self.options.get(), None)
        self.key = self.master.fodboldtur.keys()
        self.keyList = list(self.key)
        self.refreshOptionMenu()


    def refreshOptionMenu(self):
        #kill them and remake them :/
        self.dropDown.destroy()
        self.removebButton.destroy()

        self.dropDown = OptionMenu(self.addWindow, self.options, None, *self.keyList)
        self.dropDown.pack(pady=(20, 2))

        self.removebButton = Button(self.addWindow, text="slet", command=self.removeName)
        self.removebButton.pack(pady=2)