#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:56:25 2022

@author: ludandrieu
"""

import unittest
import sys
sys.path.append("../")
from liste import Liste,Cell
from test import randomPoints
from point import Point
import filecmp
from fileRepo import FileRepo

class Test_FileRepo(unittest.TestCase):
    
    def setUp(self) -> None:
        self.__FileRepo = FileRepo()
        self.__dataTime = Liste()
        self.__dataPoints = Liste()
        self.__filename:str = ""

    def test_dataToString(self):
        for time_var,x_var,y_var in [[0.1,5,12],[0.2,0,189],[0.5,12,-15]] :
            self.__dataTime.addLast(Cell(time_var))
            self.__dataPoints.addLast(Cell(Point(x_var,y_var)))
        resultStr = self.__FileRepo.exportDataToString(self.__dataTime,self.__dataPoints)
        expectedResult="0.1;5;12\n0.2;0;189\n0.5;12;-15\n"
        self.assertEqual(resultStr,expectedResult)
    

"""
class Test_liste(unittest.TestCase):

    def setUp(self) -> None:
        self.__liste = liste()
        self.__first = cell("first")
        self.__second = cell("second")
        self.__third = cell("third")

    def tearDown(self):
        pass
        
    def test_isEmpty(self):
        self.assertTrue(self.__liste.isEmpty())

    def test_addFirstWithEmptyList(self):
        self.__liste.addFirst(self.__first)
        self.assertTrue(self.__liste.getFirst() is self.__first)

    def test_addLastWithEmptyList(self):
        self.__liste.addLast(self.__second)
        self.assertTrue(self.__liste.getFirst() is self.__second)

    def test_addFirst(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addFirst(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__third)
        self.assertTrue(self.__liste.getLast() is self.__first)

    def test_addLast(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addLast(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__second)
        self.assertTrue(self.__liste.getLast() is self.__third)

    def test_insertionOrder(self):
        self.__liste.addFirst(self.__first)
        self.assertEqual(self.__liste.getFirst(),self.__first)
        self.assertEqual(self.__liste.getLast(),self.__first)
        self.__liste.addFirst(self.__second)
        self.assertEqual(self.__liste.getFirst(),self.__second)
        self.assertEqual(self.__liste.getLast(),self.__first)
        self.__liste.addFirst(self.__third)
        self.assertEqual(self.__liste.getFirst(),self.__third)
        self.assertEqual(self.__liste.getLast(),self.__first)
    
    def test_str(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addFirst(self.__third)
        self.assertEqual(str(self.__liste),"third -> second -> first -> ")
"""     
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
