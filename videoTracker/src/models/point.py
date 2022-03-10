# -*- coding: utf-8 -*-

import sys
sys.path.append(__file__.replace("\\","/").replace("point.py",""))

class Point():

    def __init__(self, x: any, y: any, forcedType: any = None) -> None:
        self.__setType(forcedType)
        self.setX(x)
        self.setY(y)

    def getX(self) -> any:
        return self.__x

    def getY(self) -> any:
        return self.__y

    def setX(self, newX: any) -> None:
        if self.__forcedType == None or type(newX) == self.__forcedType:
            self.__x = newX
        else:
            raise TypeError(
                f"type error:{type(newX)} given,{self.__forcedType} was expected")

    def setY(self, newY: any) -> None:
        if self.__forcedType == None or type(newY) == self.__forcedType:
            self.__y = newY
        else:
            raise TypeError(
                f"type error:{type(newY)} given,{self.__forcedType} was expected")

    def __setType(self, newType: any) -> None:
        if newType in (int, float, str, None):
            self.__forcedType = newType
        elif newType == any:
            self.__forcedType = None
        else:
            raise TypeError(
                f"type error:{newType} was given, only {(int,float,str,None,any)} are accepted")

    def getType(self) -> any:
        if self.__forcedType == None:
            return any
        else:
            return self.__forcedType
