import sys
sys.path.append(__file__.replace("\\", "/").replace("models/scale.py", ""))
import math
import models.point as point
Point = point.Point


class Scale():

    def __init__(self) -> None:
        self.isSelected: bool = False

        self.__selectedPoint1: Point[int] = None
        self.__selectedPoint2: Point[int] = None
        self.selectedRatio: float = None  # pixel par métre
        self.selectedDistReel: float = None
        self.selectedDistPts: float = None

        self.__tmpPoint1: Point[int] = None
        self.__tmpPoint2: Point[int] = None
        self.__tmpRatio: float = None
        self.__tmpDistReel: float = None
        self.__tmpDistPts: float = None

    def calcDistPoints(self, point1: "Point[int]", point2: "Point[int]") -> float:
        return math.sqrt(math.pow(point1.getX()-point2.getX(), 2) + math.pow(point1.getY()-point2.getY, 2))

    def setDistPoints(self, distPts: float) -> None:
        self.__tmpDistPts = distPts

    def setDistReel(self, distReel: float) -> None:
        self.__tmpDistReel = distReel

    def setRatio(self, ratio: float) -> None:
        self.__tmpRatio = ratio

    def setPoint1(self, point1) -> None:
        self.__tmpPoint1 = point1

    def setPoint2(self, point2) -> None:
        self.__tmpPoint2 = point2

    def arePointsValids(self) -> bool:
        if (self.__tmpPoint2 is None) or (self.__tmpPoint1 is None):  # point non definis
            return False
        elif (self.__tmpPoint1.getType() != int) or (self.__tmpPoint2.getType() != int):
            return False
        elif (self.__tmpPoint1.getX() == self.__tmpPoint2.getX()) and ((self.__tmpPoint1.getY() == self.__tmpPoint2.getY())):  # points confondus
            return False
        else:
            return True

    def isUserDistValide(self, distReel: float) -> bool:
        if not isinstance(distReel, float):
            return False
        elif distReel < 0.:
            return False
        else:
            return True

    def calcRatio(self) -> float:
        return self.__tmpDistPts/self.__tmpDistReel

    def selectScale(self) -> None:
        self.isSelected = True
        self.__selectedPoint1 = self.__tmpPoint1
        self.__selectedPoint2 = self.__tmpPoint2
        self.selectedDistPts = self.__tmpDistPts
        self.selectedDistReel = self.__tmpDistReel
        self.selectedRatio = self.__tmpRatio
        self.__tmpPoint1 = None
        self.__tmpPoint2 = None
        self.__tmpDistPts = None
        self.__tmpDistReel = None
        self.__tmpRatio = None
