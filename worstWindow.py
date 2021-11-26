from tkinter import *
from tkinter.ttk import *

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")
        self.fodboldtur = self.master.fodboldtur


        Label(self.worstWindow, text="De værste betalere")

        #returns the lowest values in a dict.
        def lowestThree(self):
            sorteret=(sorted(self.master.fodboldtur.items(), key=lambda item: item[1]))
            return sorteret[0:3]


        templist = lowestThree(self)
        height = len(templist)


        width = 2

        #makes a grid of the lowest 3
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Label(self.worstWindow, text=templist[i][j])
                b.grid(row=i, column=j)

                """if j == 0:

                    text = str(list(templist.keys())[i])
                    b = Label(self.worstWindow, text=text)
                else:
                    b = Label(self.worstWindow, text=str(valueList[i]))
"""







