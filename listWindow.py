# importing tkinter module
from tkinter import *
from tkinter.ttk import *



class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")





        height = len(self.master.fodboldtur)
        width = 2
        print(self.master.fodboldtur)
        value = self.master.fodboldtur.values()
        valueList = list(value)

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                if j == 0:

                    text = str(list(self.master.fodboldtur.keys())[i])
                    b = Label(self.listWindow, text=text)
                else:
                    b = Label(self.listWindow, text=str(valueList[i]))
                b.grid(row=i, column=j)