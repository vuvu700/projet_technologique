import tkinter
import sys
sys.path.append(__file__.replace("\\", "/").replace("__init__.py", ""))


class MasterView(tkinter.Frame):

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent

    def postInit(self) -> None:
        self.parent.bind("<Button-3>", self.parent.controller.rightClick)

    # exemple
    """def Update_menue_N(self,newContent:"list[str]|str")->None:
        self.menue_N.config(...=...)
    """
