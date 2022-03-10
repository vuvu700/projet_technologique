# -*- coding: utf-8 -*-

from io import TextIOWrapper
from typing import Union
import sys
sys.path.append(__file__.replace("\\", "/").replace("fileRepo.py", ""))
import liste  # ligne juste pour le typage
import point  # ligne juste pour le typage


class FileRepo():

    def __init__(self) -> None:
        pass

    def exportDataToString(self, dataTime: "liste.Liste[float]", dataPoints: "liste.Liste[point.Point[float]]") -> str:
        separator = ';'
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

    def exportDataToCSV(self, dataTime: "liste.Liste[float]", dataPoints: "liste.Liste[point.Point]", pathAndFilename: Union[str, TextIOWrapper]) -> None:
        textToExport = self.exportDataToString(dataTime, dataPoints)
        if isinstance(pathAndFilename, TextIOWrapper):
            pathAndFilename.write(textToExport)
        if not pathAndFilename.endswith(".csv"):
            pathAndFilename += ".csv"
        # try:
        with open(pathAndFilename, mode="w", encoding='utf-8') as file:  # verif filename invalide -> crash
            file.write(textToExport)
        # except IOError as error: inutile car python renvois deja les erreurs appropriées
