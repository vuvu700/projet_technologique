#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:56:25 2022

@author: ludandrieu
"""

import unittest

import sys
from os import remove as removeFile

if '\\' in __file__:
    _MODELES_DIR_PATH = "\\".join(__file__.split('\\')[:-2])+"\\"
    sys.path.append(_MODELES_DIR_PATH)
elif '/' in __file__:
    _MODELES_DIR_PATH = "/".join(__file__.split('/')[:-2])+"/"
    sys.path.append(_MODELES_DIR_PATH)
else:
    raise EnvironmentError(
        f"their is neither '/' or '\\' in the __file__ const:{__file__}")

from liste import Liste, Cell
from point import Point
import filecmp
from fileRepo import FileRepo


class Test_FileRepo(unittest.TestCase):
    """
    ----test listes vides
    - aucun points (non)
    - aucun temps (non)
    - aucun points aucun temps (oui)
    ----

    ----test si une des celules est vides (non)

    ---- test si le data2str avec 
    - des point avec des données int positifs et negatifs (non)
    - des point avec des données float positifs et negatifs (oui)
    - des point avec des données str (non) 
    - des point avec des données any (non)
    ----

    ---- test data2csv avec
    - un filename deja cree (oui: eface puis ecrit les nouveles donnees)
    - un filename invalide (non)
    - un filename non cree (oui:creation et ecriture)
    - un separateur valide[,;/§_|] (oui:le fichier obtenu doit match les fichier test)
    - un separateur invalide (non)
    ---

    """

    def setUp(self) -> None:
        self.__FileRepo = FileRepo()
        self.__dataTime = Liste()
        self.__dataPoints = Liste()
        self.__unittestDirPath: str = _MODELES_DIR_PATH.replace(
            "\\", "/")+"unittest/"

    def test_dataToString_Points_int(self):
        try:
            fail = False
            for time_var, x_var, y_var in [[0.1, 5, 12], [0.2, 0, 189], [0.5, 12, -15]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, int)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except TypeError as error:
            fail = True
            expectedError = "type of dataPoints:<class 'int'> was forced, only <class 'float'> is accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Times_invalides_types(self):
        try:
            fail = False
            for time_var, x_var, y_var in [[0, 5., 12.], [0.2, 0., 189.], [0.5, 12., -15.]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except TypeError as error:
            fail = True
            expectedError = "type of dataTime:<class 'int'> was given, only <class 'float'> is accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)
        self.setUp()
        try:
            fail = False
            for time_var, x_var, y_var in [[0.1, 5., 12.], [0.2, 0., 189.], [0, 12., -15.]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except TypeError as error:
            fail = True
            expectedError = "type of dataTime:<class 'int'> was given, only <class 'float'> is accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Points_str(self):
        try:
            fail = False
            for time_var, x_var, y_var in [[0.1, '5.', "12."], [0.2, '0.', '189.'], [0.5, '12.', '-15.']]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, str)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except TypeError as error:
            fail = True
            expectedError = "type of dataPoints:<class 'str'> was forced, only <class 'float'> is accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Points_any(self):
        try:
            fail = False
            for time_var, x_var, y_var in [[0.1, 5, "12"], [0.2, (0), 189], [0.5, 12, [-15]]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, any)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except TypeError as error:
            fail = True
            expectedError = "type of dataPoints:<built-in function any> was forced, only <class 'float'> is accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Points_float(self):
        for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
            self.__dataTime.addLast(Cell(time_var))
            self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
        strResult = self.__FileRepo.exportDataToString(
            self.__dataTime, self.__dataPoints, separator=";")
        expectedResult = "0.1;5.0;12.5\n0.2;0.1;189.99\n0.5;12.4;-15.6\n"
        self.assertEqual(strResult, expectedResult)

    def test_dataToString_Pts_empty(self):
        try:
            fail = False
            self.__dataTime.addLast(Cell(0.14))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "les tailles des listes ne sont pas identiques"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_time_empty(self):
        try:
            fail = False
            self.__dataPoints.addLast(Cell(Point(0.5, 5.1, float)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "les tailles des listes ne sont pas identiques"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Pts_time_unequalSizes(self):
        try:
            fail = False
            self.__dataTime.addLast(Cell(0.14))
            self.__dataTime.addLast(Cell(0.16))
            self.__dataTime.addLast(Cell(0.16))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.1, float)))
            self.__dataPoints.addLast(Cell(Point(0.5, -5.1, float)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "les tailles des listes ne sont pas identiques"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)
        self.setUp()
        try:
            fail = False
            self.__dataTime.addLast(Cell(0.14))
            self.__dataTime.addLast(Cell(0.16))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.1, float)))
            self.__dataPoints.addLast(Cell(Point(0.5, -5.1, float)))
            self.__dataPoints.addLast(Cell(Point(0.5, -5.1, float)))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "les tailles des listes ne sont pas identiques"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_Pts_and_time_empty(self):
        strResult = self.__FileRepo.exportDataToString(
            self.__dataTime, self.__dataPoints, separator=";")
        expectedResult = ""
        self.assertEqual(strResult, expectedResult)

    def test_dataToString_empty_cell_time(self):
        try:
            fail = False
            self.__dataPoints.addLast(Cell(Point(0.5, 5.1, float)))
            self.__dataPoints.addLast(Cell(Point(0.6, 5.7, float)))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.0, float)))
            self.__dataTime.addLast(Cell(0.14))
            self.__dataTime.addLast(Cell())
            self.__dataTime.addLast(Cell(0.16))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "unexpected empty Cell in dataTime at position 1"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)
        self.setUp()
        try:
            fail = False
            self.__dataPoints.addLast(Cell(Point(0.5, 5.1, float)))
            self.__dataPoints.addLast(Cell(Point(0.6, 5.7, float)))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.0, float)))
            self.__dataTime.addLast(Cell())
            self.__dataTime.addLast(Cell(0.15))
            self.__dataTime.addLast(Cell(0.16))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "unexpected empty Cell in dataTime at position 0"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToString_empty_cell_points(self):
        try:
            fail = False
            self.__dataPoints.addLast(Cell())
            self.__dataPoints.addLast(Cell(Point(0.6, 5.7, float)))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.0, float)))
            self.__dataTime.addLast(Cell(0.14))
            self.__dataTime.addLast(Cell(12.0))
            self.__dataTime.addLast(Cell(0.16))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "unexpected empty Cell in dataPoints at position 0"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)
        self.setUp()
        try:
            fail = False
            self.__dataPoints.addLast(Cell(Point(0.6, 5.7, float)))
            self.__dataPoints.addLast(Cell(Point(0.0, 5.0, float)))
            self.__dataPoints.addLast(Cell())
            self.__dataTime.addLast(Cell(0.14))
            self.__dataTime.addLast(Cell(12.0))
            self.__dataTime.addLast(Cell(0.16))
            self.__FileRepo.exportDataToString(
                self.__dataTime, self.__dataPoints, separator=";")
        except ValueError as error:
            fail = True
            expectedError = "unexpected empty Cell in dataPoints at position 2"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)

    def test_dataToCvs_fileAlredyExist(self):
        for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
            self.__dataTime.addLast(Cell(time_var))
            self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
        targetPath = self.__unittestDirPath+'alredyExist.csv'
        validePath = self.__unittestDirPath+'unittest_coma_dot.csv'
        self.__FileRepo.exportDataToCSV(
            self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator=";")
        self.assertTrue(filecmp.cmp(targetPath, validePath, shallow=False))

    def test_dataToCvs_fileInvalide(self):
        try:
            fail = False
            for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
            targetPath = self.__unittestDirPath+'a0§d2a01..14?%.csv'
            self.__FileRepo.exportDataToCSV(
                self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator=";")
        except IOError as error:
            fail = True
            expectedError = f"[Errno 22] Invalid argument: '{targetPath}'"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)
        self.setUp()
        for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
            self.__dataTime.addLast(Cell(time_var))
            self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
        targetPath = self.__unittestDirPath+'incomplet.pomme'
        self.__FileRepo.exportDataToCSV(
            self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator=";")

    def test_dataToCvs_fileNotAlredyExist(self):
        for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
            self.__dataTime.addLast(Cell(time_var))
            self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
        targetPath = self.__unittestDirPath+'notAlredyExist.csv'
        validePath = self.__unittestDirPath+'unittest_coma_dot.csv'
        self.__FileRepo.exportDataToCSV(
            self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator=";")
        self.assertTrue(filecmp.cmp(targetPath, validePath, shallow=False))
        removeFile(targetPath)

    def test_dataToCvs_valide_invalide_separator(self):
        for separator, filename in [[",", 'coma'], [";", 'coma_dot'], ["/", 'slash'], ["§", 'paragraph'], ["_", 'underscore'], ["|", 'vertical']]:
            self.setUp()
            for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
            targetPath = self.__unittestDirPath+'test.csv'
            validePath = self.__unittestDirPath+'unittest_'+filename+'.csv'
            self.__FileRepo.exportDataToCSV(
                self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator=separator)
            self.assertTrue(filecmp.cmp(targetPath, validePath, shallow=False))
            removeFile(targetPath)
        try:
            fail = False
            self.setUp()
            for time_var, x_var, y_var in [[0.1, 5., 12.5], [0.2, 0.1, 189.99], [0.5, 12.4, -15.6]]:
                self.__dataTime.addLast(Cell(time_var))
                self.__dataPoints.addLast(Cell(Point(x_var, y_var, float)))
            targetPath = self.__unittestDirPath+'test.csv'
            validePath = self.__unittestDirPath+'unittest_'+filename+'.csv'
            self.__FileRepo.exportDataToCSV(
                self.__dataTime, self.__dataPoints, pathAndFilename=targetPath, separator='/***/')
            self.assertTrue(filecmp.cmp(targetPath, validePath, shallow=False))
        except ValueError as error:
            fail = True
            expectedError = "value of separator:/***/ was given, only (',', ';', '/', '§', '_', '|') are accepted"
            self.assertEqual(str(error), expectedError)
        self.assertTrue(fail)


if __name__ == '__main__':
    unittest.main(verbosity=2)
