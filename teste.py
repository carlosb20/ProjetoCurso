 
from tkinter import *

class Janela(Tk):
    def __init__(self):
        super().__init__()


        self.label = Label(self,text='ok')
        self.label.pack()



if __name__ == "__main__":
    root = Janela()
    root.geometry('500x500')
    root.mainloop()

print('carlos')