from cProfile import label
import tkinter as tk
from tkinter import filedialog
import sys
sys.path.append(__file__.replace("\\", "/").replace("__init__.py", ""))


class MasterView(tk.Frame):

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        
        self.create_menu()

<<<<<<< Updated upstream
    def postInit(self) -> None:
        self.parent.bind("<Button-3>", self.parent.controller.rightClick)

=======
    def create_menu(self):
        self.menubar= tk.Menu(self.parent) 

        self.menuFile = tk.Menu(self.parent, tearoff=0)
        self.menuFile.add_command(label="Open File",command=None)
        self.menuFile.add_command(label="Open Video",command=None)
        self.menuFile.add_command(label="Save",accelerator="CTRL+N",command=self.saveFile)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quit",command=None)
        self.menubar.add_cascade(label="File",menu=self.menuFile)
        

        self.menuView=tk.Menu(self.parent,tearoff=0)
        self.menuView.add_command(label="Show Graph",command=None)
        self.menubar.add_cascade(label="View",menu=self.menuView)
        
        self.menuPoint=tk.Menu(self.parent,tearoff=0)
        self.menuPoint.add_command(label="Def Scale",command=None)
        self.menuPoint.add_command(label="Place Repere",command=None) 
        self.menubar.add_cascade(label="Pointage",menu=self.menuPoint)

        self.menuEdit=tk.Menu(self.parent,tearoff=0)
        self.menuEdit.add_command(label="Print Value",command=None)
        self.menubar.add_cascade(label="Edit",menu=self.menuEdit)

        self.parent.config(menu=self.menubar) 
    def saveFile(self):
        with tk.filedialog.asksaveasfile(mode='w',defaultextension=".csv",initialdir=sys.path,initialfile=__file__) as file:
             #exportDatatocsv(filename = file)
        
>>>>>>> Stashed changes
    # exemple
    """def Update_menue_N(self,newContent:"list[str]|str")->None:
        self.menue_N.config(...=...)
    """
    