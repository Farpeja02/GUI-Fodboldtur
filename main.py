# importing tkinter module
from tkinter import *
from tkinter.ttk import *

import pickle
filename = 'betalinger.pk'

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass
from addWindow import addWindowClass

class mainWindow:
    def __init__(self):

        self.target = 4500
        # creating tkinter window
        self.root = Tk()
        self.fodboldtur = {}
        self.root.title("Main")


        try:
            infile = open(filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except:
            ###warn warn popoupupopppp
            print("Noget gik galt i loading a pickle")
        #TEXT
        self.total = sum(self.fodboldtur[item] for item in self.fodboldtur)
        print(self.total)

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        saveButton = Button(self.root,text ="Gem",command = self.savePickleDict)
        saveButton.pack(padx = 20, pady = 10,side=RIGHT)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.total = sum(self.fodboldtur[item] for item in self.fodboldtur)
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20, pady= 10)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 20,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 20,side=LEFT)

        addNameButtom = Button(self.root,text ="Tilføj / Slet",command = lambda: addWindowClass(self))
        addNameButtom.pack(padx = 20, pady = 20,side=LEFT)


        # infinite loop
        mainloop()

    def savePickleDict(self):
        outfile = open(filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("Filen er gemt!")
        print(self.fodboldtur)



if __name__ == '__main__':

    main = mainWindow()

    print("hej")
