#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import abc
import tkinter

import controllers
import models
import views


class Application(tkinter.Tk):

    def __init__(self):

        super().__init__()
        self.title('video tracker')

        # create the MVC without any conection beteen eachother
        self.__controllerModel = models.ControllerModel(self)
        self.__view = views.MasterView(self)
        self.__controller = controllers.MasterController(self)

        """#link the M V C to eachother
        self.__view.updateMVC()
        self.__controllerModel.updateMVC()
        self.__controller.updateMVC()"""


if __name__ == '__main__':
    app = Application()
    app.mainloop()
