# -*- coding: utf-8 -*-
import sys
sys.path.append(__file__.replace("liste.py",""))

from typing import Union

class Cell():

    def __init__(self: "Cell", value: any = None, next: Union["Cell", None] = None) -> None:
        self.setValue(value)
        self.setNext(next)

    def setNext(self, next: Union["Cell", None]) -> None:
        self.__next = next

    def getNext(self) -> Union["Cell", None]:
        return self.__next

    def getValue(self) -> any:
        return self.__value

    def setValue(self, value: any) -> None:
        self.__value = value


class Liste():

    def __init__(self) -> None:
        self.__head = None
        self.__last = None

    def isEmpty(self) -> None:
        return self.__head == None

    def addFirst(self, cell: Cell) -> None:
        if self.isEmpty():
            self.__head = cell
            self.__last = cell

        else:
            ptr = self.__head
            self.__head = cell
            cell.setNext(ptr)

    def addLast(self, cell: Cell) -> None:
        if self.isEmpty():
            self.__head = cell
            self.__last = cell
        else:
            self.__last.setNext(cell)
            self.__last = cell

    def __str__(self) -> str:
        resultat = ""
        ptr = self.__head
        while ptr != None:
            resultat = resultat + str(ptr.getValue()) + ' -> '
            ptr = ptr.getNext()
        return resultat

    def getLast(self) -> Union["Cell", None]:
        return self.__last

    def getFirst(self) -> Union["Cell", None]:
        return self.__head
