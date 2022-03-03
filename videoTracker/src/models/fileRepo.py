#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append(__file__.replace("\\", "/").replace("fileRepo.py", ""))

import liste  # ligne juste pour le typage
import point  # ligne juste pour le typage

class FileRepo():

    def __init__(self) -> None:
        pass

    def exportDataToString(self, dataTime: "liste.Liste[float]", dataPoints: "liste.Liste[point.Point[float]]", separator: str = ";") -> str:
        if dataPoints.isEmpty() or dataTime.isEmpty():
            if dataPoints.isEmpty() and dataTime.isEmpty():
                return ""
            else:
                raise ValueError(
                    "les tailles des listes ne sont pas identiques")
        if dataPoints.getFirst().getValue() == None:
            raise ValueError(
                f"unexpected empty Cell in dataPoints at position {0}")
        if dataTime.getFirst().getValue() == None:
            raise ValueError(
                f"unexpected empty Cell in dataTime at position {0}")
        if not dataPoints.getFirst().getValue().getType() in (float, None):
            raise TypeError(
                f"type of dataPoints:{dataPoints.getFirst().getValue().getType()} was forced, only {float} is accepted")
        if type(dataTime.getFirst().getValue()) != float:
            raise TypeError(
                f"type of dataTime:{type(dataTime.getFirst().getValue())} was given, only {float} is accepted")

        textResult = ""
        ptrTime = dataTime.getFirst()
        ptrPoint = dataPoints.getFirst()
        position = 0
        while ptrTime != None:
            if ptrPoint == None:
                raise ValueError(
                    "les tailles des listes ne sont pas identiques")
            if ptrTime.getValue() == None:
                raise ValueError(
                    f"unexpected empty Cell in dataTime at position {position}")
            if ptrPoint.getValue() == None:
                raise ValueError(
                    f"unexpected empty Cell in dataPoints at position {position}")
            if type(ptrTime.getValue()) != float:
                raise TypeError(
                    f"type of dataTime:{type(ptrTime.getValue())} was given, only {float} is accepted")
            textResult += f"{ptrTime.getValue()}{separator}{ptrPoint.getValue().getX()}{separator}{ptrPoint.getValue().getY()}\n"
            ptrTime = ptrTime.getNext()
            ptrPoint = ptrPoint.getNext()
            position += 1

        if ptrPoint != None:
            raise ValueError("les tailles des listes ne sont pas identiques")
        else:
            return textResult

    def exportDataToCSV(self, dataTime: "liste.Liste[float]", dataPoints: "liste.Liste[point.Point]", pathAndFilename: str, separator: str = ";") -> None:
        if not separator in (",", ";", "/", "§", "_", "|"):
            raise ValueError(
                f"value of separator:{separator} was given, only {(',', ';', '/', '§', '_', '|')} are accepted")

        textToExport = self.exportDataToString(dataTime, dataPoints, separator)
        if not pathAndFilename.endswith(".csv"):
            pathAndFilename += ".csv"
        with open(pathAndFilename, mode="w") as file:  # verif filename invalide -> crash
            file.write(textToExport)
