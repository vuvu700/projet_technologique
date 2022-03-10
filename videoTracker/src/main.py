# -*- coding: utf-8 -*-

import controllers
import models
import views
import tkinter

import sys
DIR_PATH = __file__.replace("\\", "/").replace("main.py", "")
sys.path.append(DIR_PATH+"/models/point.py")
sys.path.append(DIR_PATH+"/views/")
sys.path.append(DIR_PATH+"/controllers/")


class Application(tkinter.Tk):

    def __init__(self):

        super().__init__()
        self.title('video tracker')

        # create the MVC without any conection beteen eachother
        self.controllerModel = models.ControllerModel(self)
        self.view = views.MasterView(self)
        self.controller = controllers.MasterController(self)

        # self.controller.postInit()
        self.view.postInit()
        # self.controller.startScaleMode()

        """#link the M V C to eachother
        self.__view.updateMVC()
        self.__controllerModel.updateMVC()
        self.__controller.updateMVC()"""


if __name__ == '__main__':
    app = Application()
    app.mainloop()
