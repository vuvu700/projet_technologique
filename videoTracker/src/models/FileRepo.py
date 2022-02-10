#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:49:46 2022

@author: ludandrieu
"""




class FileRepo():
    
    def __init__(self)->None:
        pass
    
    def exportDataToString(self,dataTime:"Liste",dataPoints:"Liste",separator:str=";")->str:
        textResult=""
        ptrTime=dataTime.head
        ptrPoint=dataPoints.head
        while ptrTime!=None:
            if ptrPoint==None:raise ValueError("les tailles des listes ne sont pas identiques")
            textResult+=f"{ptrTime.value}{separator}{ptrPoint.value.getX()}{separator}{ptrPoint.value.getY()}\n"
            ptrTime=ptrTime.next
            ptrPoint=ptrPoint.next
        
        if ptrPoint!=None:raise ValueError("les tailles des listes ne sont pas identiques")
        return textResult
    
    def exportDataToCSV(self,dataTime:"Liste",dataPoints:"Liste",filename:str,separator:str=";")->None:
        textToExport=self.exportDataToString(dataTime,dataPoints,separator)
        if not filename.endswith(".csv"):filename+=".csv"
        with open(filename,mode="w") as file:
            file.write(textToExport)
        
        