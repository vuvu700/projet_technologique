#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:46:19 2022

@author: ludandrieu
"""

class Point():
    
    def __init__(self,x:float,y:float)->None:
        self.setX(x)
        self.setY(y)
    
    def getX(self)->float:
        return self.__x
    
    def getY(self)->float:
        return self.__y
    
    def setX(self,newX:any)->None:
        if type(newX)==float:
            self.__x=newX
        elif type(newX)==int:
            self.__x=float(newX)
        elif type(newX)==str:
            try:
                tmp=float(newX)
                self.__x=tmp
            except :
                raise Exception(f"value error:{newX}")
        else: raise TypeError(f"type error:{type(newX)}")
        
    def setY(self,newY:any)->None:
        if type(newY)==float:
            self.__y=newY
        elif type(newY)==int:
            self.__y=float(newY)
        elif type(newY)==str:
            try:
                tmp=float(newY)
                self.__y=tmp
            except :
                raise Exception(f"value error:{newY}")
        else: raise TypeError(f"type error:{type(newY)}")
        
        
