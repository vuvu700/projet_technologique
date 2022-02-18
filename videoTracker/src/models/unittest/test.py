#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:08:47 2022

@author: ludandrieu
"""

import sys
sys.path.append("../")
from random import randint,random
from liste import Liste,Cell
from point import Point


def randomPoints(nb_points:int,val_min=0,val_max=255)->Liste:
    listePoints=Liste()
    for _ in range(nb_points):
        newPoint=Point(randint(val_min,val_max))
        cellPoint=Cell(newPoint)
        listePoints.addLast(cellPoint)
    return listePoints

def randomListeFloat(nb_points:int,val_min=0.,val_max=255.)->Liste:
    listeResult = Liste()
    for _ in range(nb_points):
        newCell = Cell(random(val_min,val_max))
        listeResult.addLast(newCell)
    return listeResult
