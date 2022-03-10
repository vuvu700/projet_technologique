# -*- coding: utf-8 -*-

import unittest

import sys
sys.path.append(__file__.replace("\\", "/").replace("unittest/test_Point.py", ""))

import point 
Point=point.Point

class Test_FileRepo(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_value_set_get_XY_no_forcedType_multi(self):
        for x, y in [["a", 'b'], [1, 1.], [(0), None], [1.56, 65.], [-1, 15]]:
            point = Point(x, y, forcedType=None)
            self.assertEqual(point.getX(), x)
            self.assertEqual(point.getY(), y)

    def test_value_set_get_XY_forcedType_multi(self):
        for x, y, forcedType, expectedToFail in [["a", 'b', str, False], [1, 1., int, True], [(0), (1), tuple, True], [1.56, 65., float, False], [-1, 15, int, False], [1.99, -45, int, True]]:
            if expectedToFail:
                with self.assertRaises(TypeError):
                    point = Point(x, y, forcedType=forcedType)
            else:
                point = Point(x, y, forcedType=forcedType)
                self.assertEqual(point.getX(), x)
                self.assertEqual(point.getY(), y)

    def test_forcedType_set_get(self):
        for x, y, forcedType in [["a", 'b', str], [15.1, 15, any], [15, 15.1, any], [1.56, 65., float], [-1, 15, int], [15.1, 15, any]]:
            point = Point(x, y, forcedType=forcedType)
            self.assertEqual(point.getType(), forcedType)


if __name__ == '__main__':
    unittest.main(verbosity=2)
