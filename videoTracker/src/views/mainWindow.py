import tkinter

class MasterView(tkinter.Frame):

    def __init__(self,parent)->None:
        super().__init__(parent)
        self.parent=parent
    
    #exemple
    """def Update_menue_N(self,newContent:"list[str]|str")->None:
        self.menue_N.config(...=...)
    """
