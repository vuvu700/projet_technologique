import sys
sys.path.append(__file__.replace("\\", "/").replace("masterController.py", ""))
sys.path.append(__file__.replace("\\", "/").replace("controlleurs/masterController.py", ""))
from models.scale import Scale
from models.point import Point

import tkinter
# les events tkinter:<KeyPress event state=Mod2 keysym=a keycode=24 char='a' x=42 y=84>


class MasterController():

    def __init__(self, parent):
        self.parent = parent
        self.scale: "Scale" = Scale()
        self.__flag_ScaleMode: str = "off"  # off on
        self.__flag_scale_point1: str = "off"  # off on done
        self.__flag_scale_point2: str = "off"  # off on done
        self.__flag_scale_dialogue: str = "off"  # off on done
        self.__debug = True

    def _debugFlagsGET(self, listOfFlags: "list[str]") -> "list[any]":
        resultListe = []
        for attr in listOfFlags:
            resultListe.append(getattr(self, attr))
        return resultListe

    def _debugFlagsSET(self, listOfFlags: "dict[str,any]") -> None:
        for attr, value in listOfFlags.items():
            setattr(self, attr, value)

    def startScaleMode(self) -> None:
        """qui permet d'activer le mode échelle en modifiant des flags"""
        self.__flag_ScaleMode = "on"
        self.__flag_scale_point1 = "on"
        self.__flag_scale_point2 = "off"
        self.__flag_scale_dialogue = "off"

    def stopScaleMode(self) -> None:
        """qui permet d'activer le mode échelle en modifiant des flags"""
        self.__flag_ScaleMode = "off"
        self.__flag_scale_point1 = "off"
        self.__flag_scale_point2 = "off"
        self.__flag_scale_dialogue = "off"

    def rightClick(self, event: tkinter.Event) -> None:
        # print(dir(event),type(event))
        if self.__debug:
            print(event.x, event.y, event.widget)
        if self.__flag_ScaleMode == 'on':

            if self.__flag_scale_point1 == "on":
                self.scale.setPoint1(Point(event.x, event.y, int))
                self.__flag_scale_point1 = "done"
                self.__flag_scale_point2 = "on"
                if self.__debug:
                    print("point1 added")

            elif self.__flag_scale_point1 == "done":
                if self.__flag_scale_point2 == "on":
                    self.scale.setPoint2(Point(event.x, event.y, int))
                    self.__flag_scale_point2 = "done"
                    self.__flag_scale_dialogue = "on"
                    if self.__debug:
                        print("point2 added")
                    # self.stopScaleMode()
                else:
                    raise ValueError(f"unexpected flag value: MasterController.__flag_scale_point2 is {self.__flag_scale_point2}")

            else:
                raise ValueError(f"unexpected flag value: MasterController.__flag_scale_point1 is {self.__flag_scale_point1}")
