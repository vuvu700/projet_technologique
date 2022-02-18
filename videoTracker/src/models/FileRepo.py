#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:49:46 2022

@author: ludandrieu
"""

import liste
import point


class FileRepo():
    
    def __init__(self)->None:
        pass
    
    def exportDataToString(self,dataTime:"liste.Liste[float]",dataPoints:"liste.Liste[point.Point]",separator:str=";")->str:
        textResult=""
        ptrTime=dataTime.getFirst()
        ptrPoint=dataPoints.getFirst()
        while ptrTime!=None:
            if ptrPoint==None: raise ValueError("les tailles des listes ne sont pas identiques")
            textResult+=f"{ptrTime.getValue()}{separator}{ptrPoint.getValue().getX()}{separator}{ptrPoint.getValue().getY()}\n"
            ptrTime=ptrTime.getNext()
            ptrPoint=ptrPoint.getNext()
        
        if ptrPoint!=None: raise ValueError("les tailles des listes ne sont pas identiques")
        else: return textResult
    
    def exportDataToCSV(self,dataTime:"liste.Liste[float]",dataPoints:"liste.Liste[point.Point]",filename:str,separator:str=";")->None:
        textToExport=self.exportDataToString(dataTime,dataPoints,separator)
        if not filename.endswith(".csv"): filename+=".csv"
        with open(filename,mode="w") as file:
            file.write(textToExport)
        
        